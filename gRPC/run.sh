#!/bin/bash

ports=(5550 5551 5552 5553 5554 5555 5556 5557)

for port in "${ports[@]}"; do
    python variance_sampling_server.py -p "$port" &
done

python variance_sampling_client.py -p "${ports[@]}"
