# img2ue: README

Tools to help convert an image to an Unreal Engine 5 (UE5) scene. Uses YOLOv5 image object detection.

#### Modules

- [x] img2ue-clipboard: given an image, this detects objects and outputs the result into a Unreal Engine-compatible string (automatically copied to the Clipboard) - to then be manually pasted in the UE editor Content Browser search panel. For example:
	* The default YOLOv5 output: `image 1/1 C:\Users\Me\Downloads\yolov5\input\city-of-london-gc53de9e1e_1920.jpg: 448x640 23 persons, 2 bicycles, 2 cars, 1 bus, 4 traffic lights, 3 backpacks, 3 handbags` 
	* img2ue-clipboard output: `'person' || 'bicycle' || 'car' || 'bus' || 'traffic light' || 'backpack' || 'handbag' || 'bike'`
	* img2ue also adds detected objects' synonyms e.g. if a "bicycle" (YOLOv5 class) is detected, it adds "bike" to our string so we can more accurately find all related assets within UE.
- [x] img2ue-bridge: for each detected object in a given image, automatically search Bridge (filtered for 3D Assets). If an asset exists, download then import to project.
- [x] img2ue-designer: procedurally create a new Level using the downloaded Bridge assets.

## Installation

1. Install [Dependencies](#Dependencies) 
2. Drag-and-drop `detect_img2ue.py` to `yolov5` root folder.

### Dependencies

* Unreal Engine 5
* Python
	* [YOLOv5](https://pypi.org/project/yolov5/) - open source package for object detection, with pre-trained models. (I personally use the Anaconda installation method on Windows).
	* `pyperclip` - to copy text to clipboard.
	* FUTURE: ~~PyAutoGUI - Unreal Editor automation~~

## How to Run

1. `cd yolov5`
2. `python detect_img2ue.py --weights yolov5x.pt --source input --exist-ok` - assuming image is in the `yolov5/input/` folder.

## References

* [Unreal Engine 5: Advanced Search Syntax](https://docs.unrealengine.com/5.0/en-US/advanced-search-syntax-in-unreal-engine/)
* <https://forums.unrealengine.com/t/inside-unreal-simplifying-tool-creation-with-blueprints-python/629768>
* [yolo how to access class name?](https://github.com/ultralytics/yolov5/issues/5294) -  <https://github.com/ultralytics/yolov5/discussions/2032> - <https://github.com/ultralytics/yolov5/issues/5426>

## Resources

* UE5 Python tools plugin: <https://github.com/daltondotgd/UtilityToolkit>
* regex to remove trailing ` || `: `/( \|\| )$/g`
* regex to remove preceding image count and filename: `/(.*): /g` - ref: [Match Everything Before Last Occurence](https://regexland.com/regex-to-match-everything-before-a-specified-character-or-symbol/)

## SOP: Workflow: high-level:

1. run img2ue-clipboard
2. run img2ue-bridge
3. run img2ue-designer

## SOP: Workflow: low-level:

1. open Unreal Engine 5 project (and make sure "Bridge" window tab is visible)
2. open Anaconda Prompt
3. run in Anaconda Prompt:
```python
conda activate yolov5
cd C:\Users\Me\Downloads\img2ue\yolov5
python detect_img2ue.py --weights yolov5x.pt --source input --exist-ok
python ../src/img2ue-bridge.py
python img2ue-designer.py
```

## Notes

* MY CUSTOM RUN COMMAND: `python detect_img2ue.py --weights yolov5x.pt --source input --exist-ok`
* WORKING: `s2 = re.search(r"(?:\: )(.*)", )`  -  OUTPUT: `person || bicycle || car || bus || traffic light || backpack || handbag || `
* WORKING BEST: `s2 = re.search(r"(?:\: )(.*)(?: \|\| )$", s)`  -  OUTPUT: `person || bicycle || car || bus || traffic light || backpack || handbag`
* `pyperclip.copy(s2[1]) # copy string to clipboard`
* Requirements: meant to be used on scenic photograph, one (1) image at a time