
# 🏭 스마트 팩토리 사고 방지 및 모니터링 시스템: Autory
AI 영상 인식과 IoT 제어를 결합하여 사고 발생 전 기계를 즉시 정지시키는 '능동형' 안전 솔루션 

---


# 📋 Project Overview

<img width="609" height="288" alt="image" src="https://github.com/user-attachments/assets/ef2c7ef2-9835-4b99-a898-a8d331741b26" />

- 제조업 현장에서 빈번하게 발생하는 손 끼임 사고와 불량품 문제를 예방하기 위해 개발된 AI 기반 스마트 팩토리 안전 관리 시스템입니다.
- 기존 사고 후 알림 방식에서 벗어나, AI 감지 즉시 기계 제어 신호를 송신하여 사고를 사전에 차단하는 능동형 구조로 설계했습니다.
- 카메라 기반 손 감지, AI 제품 분류, 공정 모니터링, 환경 센서 분석을 통합하여 위험 요소를 실시간으로 감지합니다.
- 감지 결과를 관리자에게 즉시 전달하고, 공정 상태를 실시간으로 관리할 수 있도록 구현했습니다.

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
#### 🖥 Backend / AI (김주연)
- Python 3.12.0  
- Django REST Framework  
- MySQL  
- Django ORM  
- Gunicorn / Django runserver (local)  
- PyCharm  
- OpenCV, YOLO-based image detection (제조품 불량 감지 / 손 끼임 감지)
- Roboflow

#### 🌐 Frontend (팀원 A)
- HTML / CSS / JavaScript
- React
- Chart.js
- Figma
- 실시간 모니터링 화면 구현

#### 🔌 Hardware / IoT (팀원 B)
- Jetson Nano 기반 객체 감지 시스템 구축
- 컨베이어벨트 / 반죽기 연동 제어
- 센서 기반 온도 및 환경 데이터 수집
- 기계 제어 로직 구현
- 서버 연동 통신 구조 구현

#### 🤖 AI / Computer Vision (공통 영역)
- OpenCV
- YOLO 기반 객체 감지
- CNN 기반 손 인식 모델
- 실시간 영상 처리 파이프라인

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



