#!/bin/bash

nohup streamlit run --server.port=8901 --server.baseUrlPath=sample src/sample/app.py &
nohup streamlit run --server.port=8902 --server.baseUrlPath=get_sample_size src/get_sample_size/app.py &
service nginx start
