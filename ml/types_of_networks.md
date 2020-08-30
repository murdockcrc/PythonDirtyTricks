# Dense networks

Learn global patterns in their input feature space.

# Convolutional nets

Learn local patterns. If a pattern is identified at the bottom-right corner of an image, this same pattern can later be recognized in any other part of the image. A dense network can't do that.

The lower levels of the convnet layers learn the most basic patterns (like edges on a picture). The next layer in the network is an aggregation of those shapes (like forming an eye). This is a representation of the hierarchical nature of vision.

## Structure of the tensors

Tensors are 3D:

* Height
* Width
* Channels (depth of 3 for colored images due to RGB channels, depth of 1 for grayscale)

## Max pooling

These layers are used to aggressively downsample the image. This is done to force the network to look at broader parts of the image, thus being able to form the hierarchy of patterns which is characteristic of vision. If we did not downsample, then the higher layers in the hierarchy will be looking at very focused parts of the image, and fail to see the broader patterns.