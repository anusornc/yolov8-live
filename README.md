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


Class ID	ชื่อ Object	Class ID	ชื่อ Object	Class ID	ชื่อ Object
0	person	27	backpack	54	carrot
1	bicycle	28	umbrella	55	hot dog
2	car	29	handbag	56	pizza
3	motorcycle	30	tie	57	donut
4	airplane	31	suitcase	58	cake
5	bus	32	frisbee	59	chair
6	train	33	skis	60	couch
7	truck	34	snowboard	61	potted plant
8	boat	35	sports ball	62	bed
9	traffic light	36	kite	63	dining table
10	fire hydrant	37	baseball bat	64	toilet
11	stop sign	38	baseball glove	65	TV
12	parking meter	39	skateboard	66	laptop
13	bench	40	surfboard	67	mouse
14	bird	41	tennis racket	68	remote
15	cat	42	bottle	69	keyboard
16	dog	43	wine glass	70	cell phone
17	horse	44	cup	71	microwave
18	sheep	45	fork	72	oven
19	cow	46	knife	73	toaster
20	elephant	47	spoon	74	sink
21	bear	48	bowl	75	refrigerator
22	zebra	49	banana	76	book
23	giraffe	50	apple	77	clock
24	hat	51	sandwich	78	vase
25	backpack	52	orange	79	scissors
26	handbag	53	broccoli	80	teddy bear

```
if class_id in [0, 1, 2]:  # 0 = คน, 1 = จักรยาน, 2 = รถ
```
## License

This project is licensed under the MIT License.