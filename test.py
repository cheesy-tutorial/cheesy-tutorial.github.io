## python
# -*- coding: utf-8 -*-
import yaml
test = {"테스트 1": "테스트 1 Value", "테스트 2": "테스트 2 Value"}
with open("test.yaml", 'w', encoding="utf-8") as outfile:
    yaml.dump(test, outfile, default_flow_style=False, allow_unicode=True)
