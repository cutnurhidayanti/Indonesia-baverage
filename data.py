from roboflow import Roboflow
rf = Roboflow(api_key="TX3REnbs8I3LeAfV3dDt")
project = rf.workspace("recycloroboaiintern").project("indonesia-beverage")
version = project.version(9)
dataset = version.download("yolov8")
                