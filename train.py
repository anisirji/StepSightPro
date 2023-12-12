from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model 

# Train the model
results = model.train(data="./outdoorDetection-2/data.yaml", imgsz=800, batch=8, epochs=50, plots=True)