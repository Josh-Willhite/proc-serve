import sys
import json
sys.path.append('../src')

from proc_serve import get_info, proc_to_dict


def test_proc_to_dict():
    for proc_file in ['cpuinfo', 'meminfo']:
        info_raw = get_info(proc_file)
        info = proc_to_dict(info_raw)

        with open('./{}.json'.format(proc_file), 'r') as f:
            expected = json.load(f)

        assert len(set(info.items()) & set(expected.items())) == len(expected)
