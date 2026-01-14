import base64
import os

import cv2
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status

from autorysf import settings
from .models import production, sensor, ovensensor, post, HandDetection, manager, web
from .serializer import managerSerializer, productionSerializer, sensorSerializer, ovensensorSerializer, PostSerializer, \
    HandDetectionSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
import json
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
import logging

logger = logging.getLogger(__name__)
# 저장할 이미지 폴더 경로
#IMAGE_FOLDER = os.path.join(settings.MEDIA_ROOT, "uploaded_images")
#os.makedirs(IMAGE_FOLDER, exist_ok=True)  # 폴더가 없으면 생성

import json
import os
import base64
from datetime import datetime
from io import BytesIO
from PIL import Image
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from ultralytics import YOLO
import numpy as np
# 모델 경로와 이미지 저장 경로
MODEL_PATH = "C:/sf/autorysf/models/best.pt"
IMAGE_DIR = "C:/sf/autorysf/media/uploaded_images"
OUTPUT_DIR = "C:/sf/autorysf/media/output_images"  # 바운딩 박스 이미지 저장 경로

# 모델 로드
model = YOLO(MODEL_PATH)

# 클래스 매핑
CLASSES = model.names  # {0: 'bread'}
MODEL_PATH = "C:/sf/autorysf/models/best.pt"
IMAGE_DIR = "C:/sf/autorysf/media/uploaded_images"
OUTPUT_DIR = "C:/sf/autorysf/media/output_images"  # 바운딩 박스 이미지 저장 경로

# 모델 로드
model = YOLO(MODEL_PATH)

# 클래스 매핑
CLASSES = model.names  # {0: 'bread'}

@csrf_exempt
@api_view(['POST'])
def process_image(request):
    try:
        # 요청 데이터에서 업로드된 파일 가져오기
        uploaded_file = request.FILES.get('image')
        if not uploaded_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        # 업로드된 파일을 저장
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        unique_filename = f"uploaded_{timestamp}.jpg"
        image_path = os.path.join(IMAGE_DIR, unique_filename)

        if not os.path.exists(IMAGE_DIR):
            os.makedirs(IMAGE_DIR)

        with open(image_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # 현재 처리 중인 이미지 출력
        print(f"Processing image: {image_path}")

        # 이미지 로드
        image = cv2.imread(image_path)
        if image is None:
            return JsonResponse({'error': 'Failed to load the image'}, status=400)

        # YOLO 모델로 이미지 감지
        results = model(image, conf=0.9, iou=0.4)  # 신뢰도와 IOU 설정

        # "bread" 클래스만 필터링
        filtered_boxes = [
            box for box in results[0].boxes
            if int(box.cls[0]) == 0 and CLASSES[int(box.cls[0])] == 'bread'
        ]

        # 감지 여부 확인
        bread_detected = len(filtered_boxes) > 0

        if bread_detected:
            # 신뢰도가 가장 높은 "bread" 객체만 선택
            best_box = max(filtered_boxes, key=lambda box: float(box.conf[0]))
            x_min, y_min, x_max, y_max = map(int, best_box.xyxy[0].tolist())
            confidence = float(best_box.conf[0])
            class_name = CLASSES[int(best_box.cls[0])]

            # 바운딩 박스 추가
            image_with_boxes = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.rectangle(image_with_boxes, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(image_with_boxes, f"{class_name} {confidence:.2f}", (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 바운딩 박스 이미지 저장
            output_path = os.path.join(OUTPUT_DIR, f"boxed_{timestamp}.jpg")
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)
            cv2.imwrite(output_path, image_with_boxes)
        else:
            # "bread" 클래스가 감지되지 않으면 바운딩 박스 이미지를 생성하지 않음
            output_path = None

        # 결과 반환
        return JsonResponse({
            'detected_value': 0 if bread_detected else 1,  # 0: bread 감지, 1: 감지 안 됨
            'output_image_path': output_path
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET', 'PATCH'])
def update_profile(request):
    """
    사용자 프로필 업데이트 API
    """
    if request.method == "GET":
        try:
            # JSON 데이터 파싱
            data = json.loads(request.body)
            email = data.get("email")
            name = data.get("name")
            phone = data.get("phone")
            company_name = data.get("com_name")
            profile_image = request.FILES.get("profile_image")

            # 사용자 확인
            user_manager = manager.objects.filter(email=email).first()
            if not user_manager:
                return JsonResponse({"error": "해당 사용자가 존재하지 않습니다."}, status=404)

            # 이메일 중복 체크
            new_email = data.get("new_email")
            if new_email and new_email != user_manager.email:
                # 중복 이메일 확인
                if manager.objects.filter(email=new_email).exists():
                    return JsonResponse({"error": "중복된 이메일이 존재합니다."}, status=400)
                else:
                    user_manager.email = new_email

            # 사용자 정보 업데이트
            user_manager.name = name if name else user_manager.name
            user_manager.phone = phone if phone else user_manager.phone
            user_manager.com_name = company_name if company_name else user_manager.com_name

            # 프로필 이미지 업데이트
            if profile_image:
                user_manager.profile_image.save(profile_image.name, profile_image)

            # 변경 사항 저장
            user_manager.save()

            return JsonResponse(
                {"message": "프로필이 성공적으로 업데이트되었습니다."},
                status=200,
                json_dumps_params={'ensure_ascii': False}
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "잘못된 JSON 데이터입니다."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "허용되지 않은 메서드입니다."}, status=405)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def postViewSet(request):
    logger.debug("Received request data: %s", request.data)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.debug("Image upload successful")
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    logger.debug("Image upload failed: %s", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_sensor_data(request):
    """
    온습도 데이터를 반환하는 API
    """
    sensors = sensor.objects.all().order_by('-date')[:10]  # 최신 10개 데이터 반환
    serializer = sensorSerializer(sensors, many=True)
    return JsonResponse(serializer.data, safe=False)


last_value = None  # 최근 값 저장용 변수

@api_view(['POST'])
def hand_detection(request):
    """

    하드웨어에서 데이터를 POST 요청으로 보내는 API
    """
    try:
        # 하드웨어에서 보낸 값 (0 또는 1)
        value = request.data.get('status')

        if value is None:
            return Response({'error': 'Status is required'}, status=status.HTTP_400_BAD_REQUEST)

        # 값 저장
        hand_detected = bool(int(value))

        # 최근 값 업데이트
        global last_value
        last_value = int(value)

        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def hand_detection2(request):
    """
    하드웨어에서 데이터를 POST 요청으로 보내는 API
    """
    try:
        # 하드웨어에서 보낸 값 (0 또는 1)
        value = request.data.get('status')

        if value is None:
            return Response({'error': 'Status is required'}, status=status.HTTP_400_BAD_REQUEST)

        # 값 저장
        hand_detected = bool(int(value))

        # 최근 값 업데이트
        global last_value
        last_value = int(value)
        # 데이터베이스에 값 저장
        detection = HandDetection(hand_detected=hand_detected)
        detection.save()

        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_hand_detection(request):
    """
    최근 하드웨어 값을 반환하는 API
    """
    try:
        # 타임스탬프 기준으로 최신 데이터 가져오기
        latest_detection = HandDetection.objects.latest('timestamp')
        hand_detected = 1 if latest_detection.hand_detected else 0  # Boolean 값을 0 또는 1로 변환

        return Response({
            'status': 'success',
            'id': latest_detection.id,
            'value': hand_detected,  # 프론트엔드가 받을 값
            'timestamp': latest_detection.timestamp  # 타임스탬프 추가
        }, status=status.HTTP_200_OK)
    except HandDetection.DoesNotExist:
        # 데이터가 없는 경우 기본값 0 반환
        return Response({
            'status': 'success',
            'id': None,
            'value': 0,  # 기본값
            'timestamp': None  # 기본값
        }, status=status.HTTP_200_OK)
    except Exception as e:
        # 에러 로깅
        print(f"An error occurred: {str(e)}")
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def web_hand(request):
    """
    최근 하드웨어 값을 반환하는 API
    """
    try:
        # 타임스탬프 기준으로 최신 데이터 가져오기
        latest_detection = HandDetection.objects.latest('timestamp')
        hand_detected = 1 if latest_detection.hand_detected else 0  # Boolean 값을 0 또는 1로 변환

        return Response({
            'status': 'success',
            'id': latest_detection.id,
            'value': hand_detected,  # 프론트엔드가 받을 값
            'timestamp': latest_detection.timestamp  # 타임스탬프 추가
        }, status=status.HTTP_200_OK)
    except HandDetection.DoesNotExist:
        # 데이터가 없는 경우 기본값 0 반환
        return Response({
            'status': 'success',
            'id': None,
            'value': 0,  # 기본값
            'timestamp': None  # 기본값
        }, status=status.HTTP_200_OK)
    except Exception as e:
        # 에러 로깅
        print(f"An error occurred: {str(e)}")
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
def check_email(request):
    try:
        email = request.data.get('email')  # request.data 사용
        logger.debug("check_email: Received email: %s", email)

        if manager.objects.filter(email=email).exists():
            logger.debug("check_email: Email already exists")
            return JsonResponse({'valid': False})
        else:
            logger.debug("check_email: Email is available")
            return JsonResponse({'valid': True})
    except Exception as e:
        logger.error("check_email: An error occurred: %s", str(e))
        return JsonResponse({'error': 'An unexpected error occurred'}, status=500)


@api_view(['POST'])
def login_view(request):
    try:
        # 요청 본문에서 JSON 데이터 로드
        body = json.loads(request.body)
        email = body.get('email')
        password = body.get('password')

        if not email or not password:
            logger.debug("login_view: Missing email or password")
            return JsonResponse({'status': 'fail', 'message': 'Email and password are required'}, status=400)

        # 사용자 조회
        try:
            user = manager.objects.get(email=email)
            # 평문 비밀번호 대조 (보안에 취약함)
            if password == user.password:  # 평문 비교
                logger.debug("login_view: Successful login for user %s", email)
                return JsonResponse({'status': 'success'})
            else:
                logger.debug("login_view: Incorrect password for user %s", email)
                return JsonResponse({'status': 'fail', 'message': '비밀번호 오류'}, status=401)
        except manager.DoesNotExist:
            logger.debug("login_view: User with email %s does not exist", email)
            return JsonResponse({'status': 'fail', 'message': '이메일 오류'}, status=401)
    except json.JSONDecodeError:
        logger.debug("login_view: Invalid JSON received")
        return JsonResponse({'status': 'fail', 'message': 'Invalid JSON'}, status=400)
    except Exception as e:
        logger.error("login_view: An unexpected error occurred: %s", str(e))
        return JsonResponse({'status': 'fail', 'message': 'An unexpected error occurred'}, status=500)

class manageViewSet(viewsets.ModelViewSet):
    queryset = manager.objects.all()
    serializer_class = managerSerializer


manage_list = manageViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
manage_detail = manageViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

class prodViewSet(viewsets.ModelViewSet):
    queryset = production.objects.all()
    serializer_class = productionSerializer

prod_list = prodViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
prod_detail = prodViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()
    serializer_class = sensorSerializer

sensor_list = sensorViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
sensor_detail = sensorViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

class ovensensorViewSet(viewsets.ModelViewSet):
    queryset = ovensensor.objects.all()
    serializer_class = ovensensorSerializer

ovensensor_list = ovensensorViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
ovensensor_detail = ovensensorViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer

post_list = sensorViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
post_detail = sensorViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

