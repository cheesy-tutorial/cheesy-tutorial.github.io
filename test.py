## python
# -*- coding: utf-8 -*-
import yaml
test = {"�׽�Ʈ 1": "�׽�Ʈ 1 Value", "�׽�Ʈ 2": "�׽�Ʈ 2 Value"}
with open("test.yaml", 'w', encoding="utf-8") as outfile:
    yaml.dump(test, outfile, default_flow_style=False, allow_unicode=True)
