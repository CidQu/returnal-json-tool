import json

def write_dialogues_to_file(json_data, filename):
    with open(filename, "w", encoding='utf-8') as f:
        for en_key in find_all_en_keys(json_data):
            speaker = en_key["speaker"]
            f.write(f'Konuşan: {speaker}\n')
            for i, line in enumerate(en_key["lines"]):
                text = line["text"]
                f.write(f'Cümle [{i}]: {text}\n')
            f.write("--------BİTTİ DİĞER DİYALOG-------\n")

def find_all_en_keys(json_data):
    en_keys = []
    if isinstance(json_data, dict):
        for k, v in json_data.items():
            if k == "en":
                if isinstance(v, dict) and "lines" in v:
                    en_keys.append(v)
            else:
                en_keys.extend(find_all_en_keys(v))
    elif isinstance(json_data, list):
        for item in json_data:
            en_keys.extend(find_all_en_keys(item))
    return en_keys

with open("Subtitles.json", "r", encoding='utf-8') as f:
    json_data = json.load(f)
    write_dialogues_to_file(json_data, "diyaloglar.txt")