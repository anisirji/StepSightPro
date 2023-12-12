

# from roboflow import Roboflow
# rf = Roboflow(api_key="P0IdQ8jZWlbmmKyNSMwg")
# project = rf.workspace("aniket-fpzba").project("outdoordetection")
# dataset = project.version(1).download("yolov8")



from roboflow import Roboflow
rf = Roboflow(api_key="P0IdQ8jZWlbmmKyNSMwg")
project = rf.workspace("aniket-fpzba").project("outdoordetection")
dataset = project.version(2).download("yolov8")
