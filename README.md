# YOLOv8 Live Project

This project uses YOLOv8 for live object detection. Below are the steps to set up and run the project.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/anusornc/yolov8-live.git
    cd yolov8-live
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Run the application:**

    ```sh
    streamlit run app.py
    ```

2. **Open your browser and go to:**

    ```
    http://localhost:8501
    ```

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenCV-Python-Headless
- Ultralytics
- NumPy


| Class ID | Object         | Class ID | Object         | Class ID | Object         |
|----------|---------------|----------|---------------|----------|---------------|
| 0  | person          | 27 | tie            | 54 | donut          |
| 1  | bicycle         | 28 | suitcase       | 55 | cake           |
| 2  | car             | 29 | frisbee        | 56 | chair          |
| 3  | motorcycle      | 30 | skis           | 57 | couch          |
| 4  | airplane        | 31 | snowboard      | 58 | potted plant   |
| 5  | bus             | 32 | sports ball    | 59 | bed            |
| 6  | train           | 33 | kite           | 60 | dining table   |
| 7  | truck           | 34 | baseball bat   | 61 | toilet         |
| 8  | boat            | 35 | baseball glove | 62 | TV             |
| 9  | traffic light   | 36 | skateboard     | 63 | laptop         |
| 10 | fire hydrant    | 37 | surfboard      | 64 | mouse          |
| 11 | stop sign       | 38 | tennis racket  | 65 | remote         |
| 12 | parking meter   | 39 | bottle         | 66 | keyboard       |
| 13 | bench           | 40 | wine glass     | 67 | cell phone     |
| 14 | bird            | 41 | cup            | 68 | microwave      |
| 15 | cat             | 42 | fork           | 69 | oven           |
| 16 | dog             | 43 | knife          | 70 | toaster        |
| 17 | horse           | 44 | spoon          | 71 | sink           |
| 18 | sheep           | 45 | bowl           | 72 | refrigerator   |
| 19 | cow             | 46 | banana         | 73 | book           |
| 20 | elephant        | 47 | apple          | 74 | clock          |
| 21 | bear            | 48 | sandwich       | 75 | vase           |
| 22 | zebra           | 49 | orange         | 76 | scissors       |
| 23 | giraffe         | 50 | broccoli       | 77 | teddy bear     |
| 24 | backpack        | 51 | carrot         | 78 | hair drier     |
| 25 | umbrella        | 52 | hot dog        | 79 | toothbrush     |
| 26 | handbag         | 53 | pizza          |    |               |

```python
if class_id in [0, 1, 2]:  # 0 = person, 1 = bicycle, 2 = car
```
อ่านต่อ v11 ได้ที่ https://docs.ultralytics.com/models/yolo11/
## License

This project is licensed under the MIT License.
