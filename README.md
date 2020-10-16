# pkmn-music-generator
Google Magenta's PolyphonyRNN model trained on pkmn music from the GBA/NDS era games (FRLG, RSE, DPPt, HGSS, BW) to generate new pkmn music.  for MAIS202 hosted by the McGill AI Society.

## PolyphonyRNN
From [Google Magenta](https://magenta.tensorflow.org/), PolyphonyRNN is a Recurrent Neural Network with cells implementing Long-Short-Term-Memory (LSTM) to improve the RNN’s ability to learn longer-term structures as are common in music. 

Detailed information about the implementation and how to train your own model can be found [here](https://github.com/magenta/magenta/tree/master/magenta/models/polyphony_rnn)

## Dataset

14 hours of pkmn music. Detailed graphics and data cleanup to come.

## Training Attempt 1

### Hyperparameters
```
num_training_steps=20000
batch_size=64
rnn_layer_sizes=[256,256,256]
```
### Results

After 1000 steps (bundle created):
```
Accuracy = 0.7160278
Global Step = 1018
Loss = 1.701793
Perplexity = 5.483771
```

After 1000 steps the model starts overfitting the data and the results suffer.

Batch upload of generated tracks will be uploaded at a later date. [Here](https://soundcloud.com/maya-sl-743088155/700-mp-209n-03) are two examples of the generated music.

