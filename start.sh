#!/bin/bash
docker-compose up -d redis
./install_dependencies.sh
source .venv/bin/activate
python3 main.py