import streamlit as st
import cv2
import torch
from ultralytics import YOLO
import numpy as np

# โหลดโมเดล YOLOv8
model = YOLO("yolov8n.pt")  # ใช้โมเดลขนาดเล็ก

# ฟังก์ชันสำหรับดึงภาพจากเว็บแคม
def detect_objects():
    cap = cv2.VideoCapture(0)
    stframe = st.empty()  # สร้างพื้นที่สำหรับแสดงผลวิดีโอ

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.warning("ไม่สามารถเปิดเว็บแคมได้")
            break

        # ใช้โมเดล YOLO ตรวจจับวัตถุ
        results = model(frame)
        detected_persons = 0

        # วาดกรอบและนับจำนวนคน
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                if class_id == 0:  # class_id=0 หมายถึง "person" ใน YOLO
                    detected_persons += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, "Person", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # แสดงจำนวนคนบนภาพ
        cv2.putText(frame, f"People: {detected_persons}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # แสดงภาพใน Streamlit
        stframe.image(frame, channels="BGR")

    cap.release()

# UI ใน Streamlit
st.title("Webcam Object Detection - Count People")
if st.button("เริ่มตรวจจับ"):
    detect_objects()
