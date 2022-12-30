# img2ue: Changelog

### 2022-08-26

- [x] v1: for detected objects, convert to Unreal Engine Advanced Search string and automatically copy to clipboard
- [x] v2: automated Megascans assets downloader
- [x] v3: "Make Level" EUW button (creates Level > opens it > parses img2ue-clipboard string to add assets to level e.g. static meshes, Procedural Foliage volume)
- [x] show dialog window when img2ue-bridge script completed

### 2022-08-23

- [x] use content browser Search Filter Advanced queries: for all detected objects in image - format text as `fence || tree || bench`
- [x] copy object detections to clipboard
- [x] DELETE FROM PRINT OUTPUT: image number, filename, and image dimensions - ref: `image 1/1 C:\Users\Me\Downloads\_DATA_new\github\img2ue\yolov5\input\city-of-london-gc53de9e1e_1920.jpg: 448x640`
- [x] remove `||` if only 1 object detected in image
- [x] "bicycle" (yolo) = "bike" (megascans asset) - how to map words to synonyms?
  - if string2 contains "bicycle", append "bike" + " ||" to string2
- [x] for each detected object, add `' '` around each class (especially multiple words) - e.g. change `traffic light` to `'traffic light'`