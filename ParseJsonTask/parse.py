# ----------------------------
# Test task by Slava K.
#
# Date
# 2/18/2020
# ----------------------------
import json

filename = "ts_info.json"
with open(filename) as TS_file_info:
    try:
        def recursive_iter(obj, keys=()):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    yield from recursive_iter(v, keys + (k,))
            elif any(isinstance(obj, t) for t in (list, tuple)):
                for idx, item in enumerate(obj):
                    yield from recursive_iter(item, keys + (idx,))
            else:
                yield keys, obj

        TS_file_json_data = json.load(TS_file_info)
        for keys, item in recursive_iter(TS_file_json_data):
            str_audio_bool = True if 'Audio' == keys else False
            str_video_bool = True if 'Video' == keys else False
            has_a_logo = True if str_video_bool == True else False
            number_of_logos = 0
            if has_a_logo:
                number_of_logos += 1

        # Audio condition
        if str_audio_bool:
            print('TS file has audio')
        else:
            print('TS file has no audio')

        # Number of logos condition
        if has_a_logo:
            print('TS file has {} logos'.format(number_of_logos))
        else:
            print('TS file has no logos in video')

        # # Logo location condition
        # x = dict_from_parsed_json[key]
        # if x <= 860:
        #     print('The log is on the left part of the screen')
        # else:
        #     print('The log is on the right part of the screen')

        # # Video PID in hex format
        # PID = 32
        # print('\\' + hex(PID)[1:])

    finally:
        TS_file_info.close()