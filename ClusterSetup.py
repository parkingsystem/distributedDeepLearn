__author__ = 'Bhavin.Parekh'
import sys
task_number = 0#int(sys.argv[1])

import tensorflow as tf

cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
server = tf.train.Server(cluster, job_name="local", task_index=task_number)

print("Starting server #{}".format(task_number))

server.start()
server.join()