# Is it a bird?
A program that recognizes pictures of birds using the [fastai](https://www.fast.ai/) library.

First, run (download_data.py)[download_data.py] to download images of birds and forests (not birds) using the DuckDuckGo APIs.

Secondly, run [train.py](train.py) to train the model and test whether the images [bird.jpg](bird.jpg) and [forest.jpg](forest.jpg) contain a bird.

<p>
    <img src="bird.jpg" width=250 height=200>
    <figcaption>bird.jpg</figcaption>
</p>
```
This is a: bird.                                                                           
Probability it's a bird: 1.0000
```

<p>
    <img src="forest.jpg" width=250 height=200>
    <figcaption>forest.jpg</figcaption>
</p>
```
This is a: forest.                                                                         
Probability it's a bird: 0.0000
```





