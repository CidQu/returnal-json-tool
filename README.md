# returnal-json-tool
JSON Exporter and Importer for Returnal Game

# extract.py

Just use extract.py with json file near it. Json file name should be Subtitles.json

You will get diyaloglar.txt as output:

```
Konuşan: Selene
Cümle [0]: Scout Log: Atropos.
Cümle [1]: Elapsed time… Thirty minutes since last crash.
Cümle [2]: Whole areas of this forest are rearranging themselves like…
Cümle [3]: a fluid puzzle after each of my…
Cümle [4]: When— whenever I return.
Cümle [5]: Per “Astra Protocol”,
Cümle [6]: I will not be recovered until I reach the broadcast signal.
Cümle [7]: If you're hearing this, you are stuck here too.
--------BİTTİ DİĞER DİYALOG-------
```

You can translate Speaker, and lines.

# import.py

Just use this with diyaloglar.txt and subtitles.json, it will update the json file then create a new one.
