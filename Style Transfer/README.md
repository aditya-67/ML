# Image Style Transfer in TensorFlow.js

This repository contains an implementation of style transfer running in a browser using TensorFlow.js.

Checkout the [demo](https://aditya-67.github.io/image-style-transfer/)

### Different models used

The original paper uses an Inception-v3 model 
as the style network, which takes up ~36.3MB 
when ported to the browser as a FrozenModel.

In order to make this model smaller, a MobileNet-v2 was
used to distill the knowledge from the pretrained Inception-v3 
style network. This resulted in a size reduction of just under 4x,
from ~36.3MB to ~9.6MB, at the expense of some quality.

For the transformer network, the original paper uses 
a model using plain convolution layers. When ported to
the browser, this model takes up 7.9MB and is responsible
for the majority of the calculations during stylization.

In order to make the transformer model more efficient, most of the
plain convolution layers were replaced with depthwise separable 
convolutions. This reduced the model size to 2.4MB, while
drastically improving the speed of stylization.

This demo lets you use any combination of the models, defaulting
to the MobileNet-v2 style network and the separable convolution
transformer network.

### How big are the models I'm downloading?

The distilled style network is ~9.6MB, while the separable convolution
transformer network is ~2.4MB, for a total of ~12MB. 
Since these models work for any style, you only 
have to download them once!

### How does style combination work?

Since each style can be mapped to a 100-dimensional 
style vector by the style network,
we simply take a weighted average of the two to get
a new style vector for the transformer network.

This is also how we are able to control the strength
of stylization. We take a weighted average of the style 
vectors of *both* content and style images and use 
it as input to the transformer network.

## Running locally for development

This project uses [Yarn](https://yarnpkg.com/en/) for dependencies.

To run it locally, you must install Yarn and run the following command at the repository's root to get all the dependencies.

```bash
yarn install
```

```bash
yarn run prep
```

Then, you can run

```bash
yarn run start
```

You can then browse to `localhost:9966` to view the application.


## Credits

Inspired from [Reiichiro Nakano](https://github.com/reiinakano)'s implementation.
Thank you so much Reiichiro for your contribution towards my knowledge.
