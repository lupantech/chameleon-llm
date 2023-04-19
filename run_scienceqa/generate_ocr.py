"""
Reference: https://github.com/JaidedAI/EasyOCR 
"""

# ! pip install easyocr


import easyocr
import json
import tqdm

if __name__ == "__main__":

    data_file = "../data/scienceqa/problems.json"
    image_dir = "../data/scienceqa/images"
    output_file = "../data/scienceqa/ocrs.json"

    data = json.load(open(data_file, 'r'))

    reader = easyocr.Reader(['en']) # ocr reader

    img_pids = [pid for pid in data.keys() if data[pid]["image"]]

    results = {
        "model": "easyocr",
        "url": "https://github.com/JaidedAI/EasyOCR",
        "version": "1.1.8",
        "date": "2023-04-06",
        "texts": {}
    }
    for pid in tqdm.tqdm(img_pids):
        split = data[pid]["split"]
        image_file = f"{image_dir}/{split}/{pid}/image.png"

        result = reader.readtext(image_file)
        results["texts"][pid] = str(result)
        # print(result)
        # break

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

