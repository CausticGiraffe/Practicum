Retraining Inception using Docker

path Practicum/tf_cancer/train

#link images to docker container
docker run -it -v $HOME/tf_cancer:/train/ gcr.io/tensorflow/tensorflow:latest-devel

cd tensorflow

git pull

python retrain.py \
  --bottleneck_dir=bottlenecks \ #cache outputs of lower layers
  --how_many_training_steps=500 \ #run for 500 iterations
  --model_dir=~/Practicum/tf_cancer/inception \ #store trained model
  --output_graph=~/Practicum/tf_cancer/retrained_graph.pb \ #output graph view in tensorboard
  --output_labels=~/Practicum/tf_cancer/retrained_labels.txt \ #output labels
  --image_dir ~/Practicum/tf_cancer/train #image directory

import tensorflow as tf, sys
image_path = sys.argv[1]

#read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read

#loads label file, strips off carriage return
label_lines = [line.rstrip() for line in tf.gfile.GFile("/tf_cancer/retrained_labels.txt")]

#unpersists graph from file
with tf.gfile.FastGFile(".tf_cancer/retrained_graph.pb", 'rb') as f:
  graph_def = tf.GraphDef()
  graph_def.ParseFromString(f.read())
  _ = tf.import_graph_def(graph_def, name='')

#create tensorflow session
with tf.Session() as sess:
  #feed the image_data as input to the graph and get first prediction
  softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

  prediction = sess.run(softmax_tensor, \
        {'DecodeJpeg/contents:0': image_data})

  #sort to show labels of first prediction in order of confidence
  top_k = predictions[0].argsor()[-len(predictions[0]):][::-1]

  for node_id in top_k:
      human_string = label_lines[node_id]
      score = predictions[0][node_id]
      print('%s (score = %.5f)' % (human_string, score))
