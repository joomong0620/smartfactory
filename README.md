
# 🏭 스마트 팩토리 사고 방지 및 모니터링 시스템: Autory
AI 영상 인식과 IoT 제어를 결합하여 사고 발생 전 기계를 즉시 정지시키는 '능동형' 안전 솔루션 

---


# 📋 Project Overview

<img width="609" height="288" alt="image" src="https://github.com/user-attachments/assets/ef2c7ef2-9835-4b99-a898-a8d331741b26" />

#### 동기
- 제조 현장에서 빈번하게 발생하는 손 끼임 사고와 불량률 문제를 예방하기 위함
- 기존 사후 알림 중심 대응 방식에서 벗어나 사전 차단 구조 필요성 인식
- AI 기반 실시간 감지를 통해 산업 안전 관리 체계 고도화 목표

#### 목표
- YOLOv5 기반 시리간 손 끼임 감지 모델 구축
- Django REST Framework 기반 API 서버와 AI 모델 통합
- MySQL 기반 데이터 구조 설계 및 실시간 모니터링 환경 구축
- 센서 데이터와 영상 데이터를 통합 관리하는 스마트 안전 시스템 구현





---

## 🕰️ Period
24.03.02일 ~ 24.12.25일 (9개월)

## 👩‍💻 멤버구성
| 성명     | 역할 (Role)            | 담당 업무 (Responsibility) |
|----------|------------------------|----------------------------|
| 김주연   | Backend / AI (Lead)    | Django REST Framework 기반 서버 및 RESTful API 설계, MySQL DB 구축, YOLOv5 기반 실시간 손 끼임 감지 및 제품 분류 AI 모델 개발, 데이터셋 라벨링 및 학습 정제 총괄 |
| 팀원 A   | Hardware / AI          | Jetson Nano 기반 객체 감지 시스템 구현, IoT 환경 센서(온습도/미세먼지) 네트워크 구축, 하드웨어 제어 로직 및 서버 연동 |
| 팀원 B   | Frontend / UIUX        | React 기반 실시간 모니터링 대시보드 개발, Figma 활용 UI/UX 디자인 및 데이터 시각화(Chart.js) 구현, 데이터셋 라벨링 참여 |


## ⚙️ Development Environment
﻿• Backend: Python 3.12, Django REST Framework, MySQL, Gunicorn
• AI: YOLOv5, OpenCV, CNN 기반 객체 탐지, Roboflow(Dataset 관리)
• Hardware: Jetson Nano, IoT 센서(온습도/미세먼지)
• Frontend: React, Chart.js<img width="680" height="188" alt="image" src="https://github.com/user-attachments/assets/aa6c4d64-fc2f-4d5c-bbd3-049cb0a6c62b" />

---


## 📌 My Role 

#### DB 구축 - [상세 보기 - WIKI 이동](https://github.com/joomong0620/smartfactory/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(DB-%EA%B5%AC%EC%B6%95))
- MySQL 기반 테이블 설계 및 구축
- 관리자 / 생산 데이터 / 센서 / 오븐 / 손 감지 / 게시물 등 전체 스키마 구성
- Django ORM 기반 모델 정의
- DB 마이그레이션 및 연동


#### API 구축 - [상세 보기 - WIKI 이동](https://github.com/joomong0620/smartfactory/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(API-%EA%B5%AC%EC%B6%95))
- 관리자 관리 API (CRUD)
- 생산 데이터 관리 API
- 공장 센서값 관리 API(온도·습도·미세먼지)
- 오븐 센서 데이터 관리 API
- 손 감지 데이터 POST / 최신값 GET API
- 이미지 업로드 기반 AI 분석 API
- 사용자 프로필 관리 API


#### 불량품 데이터 처리 (AI) - [상세 보기 - WIKI 이동](https://github.com/joomong0620/smartfactory/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(%EB%B6%88%EB%9F%89%ED%92%88-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%98%EB%A6%AC-(AI)))
- 업로드 이미지 → YOLO 모델로 불량품 감지
- bread 클래스만 필터링하여 정상/불량 판별
- 바운딩 박스 added 이미지 생성 및 저장
- 감지 결과를 JSON으로 반환


#### 손 감지 데이터 처리 (AI) - [상세 보기 - WIKI 이동](https://github.com/joomong0620/smartfactory/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(%EC%86%90-%EA%B0%90%EC%A7%80-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%98%EB%A6%AC-(AI)))
- 손 감지 상태(status) 값을 서버에서 수신
- 감지 여부 DB 저장
- 가장 최근 손 감지 상태 조회 API 제공
- 모니터링 화면에서 실시간 확인


--- 


## 기술 문제 해결 경험 및 직무 적용 역랑

﻿■ 실시간 추론 지연 문제 개선
• 문제: Jetson Nano 환경에서 YOLO 추론 지연(평균 1초 이상) 발생
• 분석: 입력 이미지 해상도 및 모델 weight 크기로 인한 병목 확인
• 조치: 이미지 리사이징 및 경량화 모델 적용, 불필요한 후처리 제거
• 결과: 추론 속도 1.1초 → 0.5초로 약 55% 개선
• 직무 적용점: 실시간 처리 시스템에서 Latency 최소화 설계 역량 확보

■ DB 병목 및 데이터 구조 개선
• 문제: 감지 데이터 단일 테이블 저장으로 조회 속도 저하 발생
• 분석: JOIN 빈도 증가로 DB I/O 병목 확인
• 조치: 데이터 분리 설계 및 인덱스 추가
• 결과: 조회 속도 약 40% 개선
• 직무 적용점: 데이터 흐름 기반 DB 구조 설계 및 성능 최적화 경험 확보

■ 시스템 통합 설계 경험
• AI 모델 → API 서버 → DB 저장 → 모니터링 대시보드까지 End-to-End 구조 설계
• 센서 데이터와 영상 데이터 통합 처리 구조 설계
• 직무 적용점: AI–Backend 통합 아키텍처 설계 및 산업 환경 적용 가능 역량 보유




## 🎯 Performance & Results

경진대회 수상: 2024 캡스톤디자인 경진대회 대상 수상.

| 지표 (Metric)        | 결과 (Result)     | 비고 |
|----------------------|-------------------|------|
| 손 인식 정확도       | 99%               | 다양한 조명 및 각도 데이터 학습 결과 |
| 기계 정지 성공률     | 98%               | 위험 감지 즉시 제어 신호 송신 성공률 |
| 평균 응답 속도       | 0.5초 이내        | 실시간 영상 처리 및 서버 통신 최적화 |
| 연속 가동 테스트     | 10시간 이상       | 장시간 구동 시 시스템 안정성 및 DB 부하 검증 |


## 💡 Lessons Learned
하드웨어-AI-백엔드가 결합된 복합 시스템을 개발하며, 백엔드 개발자가 단순히 데이터만 전달하는 것이 아니라 전체 시스템의 지연(Latency)과 에러를 조율하는 컨트롤 타워 역할을 해야 함을 깊이 체득했습니다.




