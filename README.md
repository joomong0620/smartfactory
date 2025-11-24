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
- 김주연 (Backend / AI) : Django 기반 서버 구축, MySQL DB 설계 및 구축, 손 끼임 감지 AI 모듈 구현, 제품 분류 인식 모델 개발
- 강구빈 (Hardware / AI) : Jetson Nano 기반 반죽기 실시간 감지, 컨베이어 벨트 IoT 센서 구축
- 김소연 (Frontend) : React 기반 관리자 페이지 개발, UI/UX, 대시보드 디자인(Figma)

### ⚙️ 개발 환경
- **Language**: Python 3.12.0  
- **Backend Framework**: Django REST Framework  
- **Database**: MySQL  
- **ORM**: Django ORM  
- **Server Runtime**: Gunicorn / Django runserver (local)  
- **Development Tools**: PyCharm  
- **AI Processing**: OpenCV, YOLO-based image detection (제조품 불량 감지 / 손 끼임 감지)

