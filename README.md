# 🏭 스마트 팩토리 사고 방지 및 자동화 관리 시스템
AI 기반 실시간 안전 감지 & 공정 자동화 모니터링 프로젝트


----
## 📂 프로젝트 소개
제조업 사망사고 중 가장 많은 비중을 차지하는 사고는 끼임 사고이며
이는 지속적으로 증가하고 있습니다.
<img width="609" height="288" alt="image" src="https://github.com/user-attachments/assets/ef2c7ef2-9835-4b99-a898-a8d331741b26" />


본 프로젝트는 제조업 생산 공정에서 가장 빈번하게 발생하는 손 끼임 사고,
불량품 발생, 작업 현황 파악 문제를 해결하기 위해 제작된
AI 기반 스마트 팩토리 안전·자동화 관리 시스템입니다.

카메라 기반 손 끼임 감지, AI 제품 분류, 공정 모니터링,
온습도/미세먼지 이상 감지 등 다양한 위험 요소를 자동으로 분석하여
관리자에게 실시간으로 전달합니다.


## 🕰️ 개발 기간
24.03.02일 ~ 24.12.25일

### 👩‍💻 멤버구성
- 김주연 (Backend / AI) : Django 기반 서버 구축, MySQL DB 설계 및 구축, 손 끼임 감지 AI 모듈 구현, 제품 분류 인식 모델 개발, 데이터셋 라벨링
- 강구빈 (Hardware / AI) : Jetson Nano 기반 반죽기 실시간 감지, 컨베이어 벨트 IoT 센서 구축
- 김소연 (Frontend) : React 기반 관리자 페이지 개발, UI/UX, 대시보드 디자인(Figma), 데이터셋 라벨링

### ⚙️ 개발 환경
- **Language**: Python 3.12.0  
- **Backend Framework**: Django REST Framework  
- **Database**: MySQL  
- **ORM**: Django ORM  
- **Server Runtime**: Gunicorn / Django runserver (local)  
- **Development Tools**: PyCharm  
- **AI Processing**: OpenCV, YOLO-based image detection (제조품 불량 감지 / 손 끼임 감지)
- **Labeling Tool** : Roboflow


## 📌 주요 기능

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


#### 손 감지 데이터 처리 (AI) - [상세 보기 - WIKI 이동](https://github.com/joomong0620/smartfactory/wiki/%EC%86%90-%EA%B0%90%EC%A7%80-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%98%EB%A6%AC-(AI))
- 손 감지 상태(status) 값을 서버에서 수신
- 감지 여부 DB 저장
- 가장 최근 손 감지 상태 조회 API 제공
- 모니터링 화면에서 실시간 확인




