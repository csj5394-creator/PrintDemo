# 🖐️ MediaPipe Hands & Image Segmentation
Google **MediaPipe**를 활용한 손 감지(Hand Detection) 및 이미지 분할(Image Segmentation) 실습 프로젝트입니다.  
실시간 웹캠 또는 동영상 입력을 통해 **손의 움직임**과 **배경 흐리기 효과**를 테스트할 수 있습니다.

![배너 이미지](assets/banner.png)

---

## 목차
- [소개](#소개)
- [설치](#설치)
- [손 감지 테스트](#손-감지-테스트)
- [이미지 세그멘테이션 테스트](#이미지-세그멘테이션-테스트)
- [추가 기능](#추가-기능)
- [예시](#예시)
- [기여](#기여)
- [라이선스](#라이선스)

---

## 소개
이 프로젝트는 **MediaPipe**의 기본 기능을 직접 실습하기 위해 제작되었습니다.  
- 손가락 관절의 **랜드마크 추적**
- 인물 영상의 **배경 흐림 효과 적용**
- **OpenCV**를 통한 영상 입력 처리 및 실시간 렌더링

이 코드를 통해 MediaPipe의 구조와 영상 처리 파이프라인을 이해할 수 있습니다.

---

## 설치

필요한 라이브러리를 설치합니다:






```bash
pip install mediapipe opencv-python
"""
MediaPipe Hands 실습 예제
========================
이 코드는 Google MediaPipe를 이용해 손을 감지하고,
손가락의 관절(랜드마크)을 시각화하는 예제입니다.

👉 실행 방법:
    1. pip install mediapipe opencv-python
    2. python hand_detector.py
    3. ESC 키로 종료
"""

import cv2
import mediapipe as mp

# ============================
# 📷 카메라 혹은 동영상 연결
# ============================
# 카메라가 연결되어 있다면:
# cap = cv2.VideoCapture(0)

# 카메라가 없다면 준비된 hand.mp4 파일로 테스트:
cap = cv2.VideoCapture("hand.mp4")

# ============================
# 🖐️ MediaPipe Hands 초기화
# ============================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Hands 객체 생성 (정확도, 감지 모드 조정 가능)
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# ============================
# 🎥 영상 프레임 반복 처리
# ============================
while True:
    success, frame = cap.read()
    if not success:
        print("❌ 영상 입력을 불러올 수 없습니다.")
        break

    # 좌우 반전 (셀카 형태로 보기)
    frame = cv2.flip(frame, 1)

    # BGR → RGB 변환 (MediaPipe는 RGB 입력 필요)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 손 감지 수행
    result = hands.process(rgb_frame)

    # 감지된 손 랜드마크가 있다면 시각화
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )

    # 결과 표시
    cv2.imshow("🖐️ MediaPipe Hand Detector", frame)

    # ESC 키로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ============================
# 🔚 종료 및 자원 해제
# ============================
cap.release()
cv2.destroyAllWindows()

"""
MediaPipe Selfie Segmentation 실습 예제
======================================
이 코드는 사람의 배경을 인식하고 흐리게(Blur) 처리하는 예제입니다.

👉 실행 방법:
    1. pip install mediapipe opencv-python
    2. python selfie_segmentation.py
    3. ESC 키로 종료
"""

import cv2
import mediapipe as mp

# ============================
# 📷 카메라 연결
# ============================
cap = cv2.VideoCapture(0)  # 또는 영상 파일 경로 입력 가능

# ============================
# 🧍 MediaPipe Segmentation 초기화
# ============================
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

# ============================
# 🎥 영상 프레임 반복 처리
# ============================
while True:
    success, frame = cap.read()
    if not success:
        print("❌ 영상 입력 불가")
        break

    # 좌우 반전 (셀카 보기)
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 배경 분리 수행
    result = segment.process(rgb_frame)
    mask = result.segmentation_mask

    # ============================
    # 🌫️ 배경 흐림 (Blur)
    # ============================
    # 배경 부분만 블러 처리
    blurred = cv2.GaussianBlur(frame, (55, 55), 0)  # ← 여기서 강도 조절 가능
    condition = mask > 0.5  # True=사람, False=배경

    # 배경과 전경 합성
    output = frame.copy()
    output[~condition] = blurred[~condition]

    # ============================
    # 💡 결과 표시
    # ============================
    cv2.imshow("🎨 Selfie Segmentation (ESC to quit)", output)

    # ESC 키로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ============================
# 🔚 종료 및 자원 해제
# ============================
cap.release()
cv2.destroyAllWindows()

