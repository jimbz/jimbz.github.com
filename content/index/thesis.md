Title: Research
Date: 2013-10-28
Order: 20

The goal of my thesis is the design and implementation of an augmented reality system. This broad subject led me to two main directions.

# Optical-See-Through Augmented Reality
![Our optical see-through prototype][ost-system]
Augmented Reality could be of great help for critical applications such as driving or surgery assistance. However in these cases every millisecond counts and the user cannot afford to add any latency to reality. This dismisses all _video see-through_ solutions for _optical see-through_ ones, where virtual augmentations are layered onto the reality thanks to a semi-transparent display. This adds new constraints on the system for proper alignment with reality. We focused on a tablet-like system composed of a transparent LCD screen and two localization devices (one to compute the pose relative to the environment and the other to locate the user). We believe this kind of systems would be more practical to the user (well-delimited window, no heavy head-mounted device) and the designer (less constraint on the weight, slower motion) relative to current head-mounted displays.

[ost-system]: {filename}/images/seethrough/system.jpg

# Combining Direct and Feature-Based Costs for Optical Flow and Stereovision
The estimation of a dense motion field (optical flow) is a very important building block for many computer vision tasks such as 3d reconstruction. We introduce a new framework allowing to leverage the information provided by sparse feature matches (point or segment) to guide a dense iterative optical flow estimation out of local minima. This allows to vastly increase the convergence basin without any loss of accuracy. A wide range of application is then possible, without modification, such as wide-baseline stereovision or non-rigid surface registration. Our method is one of the top ranking methods on the [KITTI][] benchmark.

![Wide-baseline stereo][Daisy]{: style="width:auto;height:200px;" } ![Wide-baseline non-rigid registration][Michelle]{: style="width:auto;height:200px;" }
{: .standalone }

[KITTI]: http://www.cvlibs.net/datasets/kitti/eval_stereo_flow_detail.php?benchmark=flow&error=3&eval=all&result=5ca150bba490fec5afa8ee7beaeeed8f0fc585ac
[Daisy]: {filename}/images/dense_matching/daisy25.gif "Wide-baseline stereo"
[Michelle]: {filename}/images/dense_matching/michelle.gif "Wide-baseline non-rigid registration"
