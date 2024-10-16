from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.pt")  # Load a pretrained model
    model.train(data="data.yaml", batch=6, epochs=50, workers=4 , device="0")
    # model.to('cuda')

if __name__ == '__main__':
    train_model()  # Call the function inside the main block
