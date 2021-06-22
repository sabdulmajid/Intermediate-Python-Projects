# DownloadingMultipleFiles.py
import os
import requests
from time import time
from multiprocessing.pool import ThreadPool


def url_response(url):
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)



urls = [("Event1", "https://www.python.org/events/python-events/805/"),

        ("Event2", "https://www.python.org/events/python-events/801/"),
        ("Event3", "https://www.python.org/events/python-events/790/"),
        ("Event4", "https://www.python.org/events/python-events/798/"),
        ("Event5", "https://www.python.org/events/python-events/807/"),
        ("Event6", "https://www.python.org/events/python-events/807/"),
        ("Event7", "https://www.python.org/events/python-events/757/"),
        ("Event8", "https://www.python.org/events/python-user-group/816/")]

start = time()

ThreadPool(9).imap_unordered(url_response, urls)

print(f"Time to download: {time() - start}")

urls5 = [("Event1",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-English-0844-October-2016-Paper-1-MS.pdf"),

         ("Event2",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-English-0844-October-2016-Paper-1.pdf"),
         ("Event3",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-English-0844-October-2016-Paper-2-Insert.pdf"),
         ("Event4",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-English-0844-October-2016-Paper-2-MS.pdf"),
         ("Event5",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-English-0844-October-2016-Paper-2.pdf"),
         ("Event6",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-Mathematics-0845-October-2016-Paper-1-MS.pdf"),
         ("Event7",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-Mathematics-0845-October-2016-Paper-1.pdf"),
         ("Event8",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-Mathematics-0845-October-2016-Paper-2-MS.pdf"),
         ("Event9",
          "https://www.tutorsmalaysia.com/wp-content/uploads/2019/03/Primary-Checkpoint-Mathematics-0845-October-2016-Paper-2.pdf")]
