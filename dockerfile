FROM python:3.9


WORKDIR /app

COPY . /app

RUN chmod +x /app/*.py

RUN python -m pip install --upgrade pip
RUN pip install aiohttp
RUN pip install pytest
RUN pip install asyncio
RUN pip install pytest-asyncio
RUN pip install numpy
RUN pip install cython
RUN pip install pillow 
RUN python setup.py build_ext --inplace



