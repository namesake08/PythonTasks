#!/usr/bin/python
import json

FILENAME = "ts_info.json"


def get_json():
    with open(FILENAME) as TS_file_info:
        ts_info = json.load(TS_file_info)
        print(ts_info)
        return ts_info


def check_audio(ts_objects_):
    for i in ts_objects_:
        if i.get('Audio'):
            return True


def check_logos(ts_objects_):
    for i in ts_objects_:
        logos_ = i.get("Video", {}).get("Content", {}).get("Logos", {})
        if logos_:
            return logos_.get("LogoOnList")


def get_coordinates(logos):
    for i in logos:
        print(i.get("X", {}))
        x = i.get("X", {})
        if x <= 860:
            print('The log is on the left part of the screen')
        else:
            print('The log is on the right part of the screen')


def print_hex(ts_objects_):
    for i in ts_objects_:
        es_list = i.get("PMT", {}).get("ProgramInfo", {}).get("ElementStream", {})
    es_pid = es_list[0].get("PID", {})
    print('\\' + hex(es_pid))


if __name__ == '__main__':
    # ts_info = get_json()
    ts_objects = get_json().get('TransportStream')
    has_audio = check_audio(ts_objects)
    if has_audio:
        print("TS object has audio")
    else:
        print("TS object has no audio")

    logos = check_logos(ts_objects)
    if logos:
        print(f"TS file has video with {len(logos)} logo")
    else:
        print("TS file has no video with logo")

    get_coordinates(logos)
    print_hex(ts_objects)





    # knights = dict_with_dicts.get('TransportStream')
    # print(dict_of_dicts.get("LogoOnList"))
    # for k, v in knights.items(): #только со словаря
    #     print(k, v)
    #
    #     need_value = json.get('first_key', {}).get('second_key', None)
    #     if not need_value:
    #         print('There is no key "need_value" in passed JSON')