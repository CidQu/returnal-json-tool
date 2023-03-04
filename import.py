import json

main_json = 'Subtitles.json'
output_txt = 'diyaloglar.txt'
updated_json = 'Subtitles_updated.json'

with open(main_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(output_txt, 'r', encoding='utf-8') as f:
    dialogues = f.read().split('--------BİTTİ DİĞER DİYALOG-------\n')

en_keys = [key for key in data['entries'] if 'en' in data['entries'][key]['languages']]
for i, en_key in enumerate(en_keys):
    speaker = dialogues[i].split('\n')[0].split(': ')[1]
    lines = [line.split(': ')[1] for line in dialogues[i].split('\n')[1:-1]]
    data['entries'][en_key]['languages']['en']['speaker'] = speaker
    for j, line in enumerate(lines):
        data['entries'][en_key]['languages']['en']['lines'][j]['text'] = line

with open(updated_json, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
