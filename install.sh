#!/bin/bash
npm config set registry https://mirrors.tencent.com/npm/
cd web && npm install && npm run build || exit 1
cd ../server && python3 -m pip install -r ./requirements.txt -i https://mirrors.tencent.com/pypi/simple || exit 1