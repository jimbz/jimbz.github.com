Title: Thesis
Date: 2013-10-28
Order: 20

My thesis' goal is the design of an augmented reality system. This broad subject led me to two main directions.

# Optical-See-Through Augmented Reality
![Our optical see-through prototype][ost-system]
Augmented Reality could be of great help for critical applications such as driving or surgery assistance. However in these cases every millisecond counts and the user cannot afford to add any latency to reality. This dismisses all _video see-through_ solutions for _optical see-through_ ones, where virtual augmentations are layered onto the reality thanks to a semi-transparent display. This adds new constraints on the system for proper alignment with reality. We focused on a tablet-like system composed of a transparent LCD screen and two localization devices (one to compute the pose relative to the environment and the other to locate the user). We believe this kind of systems would be more practical to the user (well-delimited window, no heavy head-mounted device) and the designer (less constraint on the weight, slower motion) relative to current head-mounted displays.

[ost-system]: {filename}/images/seethrough/system.jpg

# Combining Direct and Feature-Based Costs for Optical Flow and Stereovision
The estimation of a dense motion field (optical flow) is a very important building block for many computer vision tasks such as 3d reconstruction. We introduce a new framework allowing to leverage the information provided by sparse feature matches (point or segment) to guide a dense iterative optical flow estimation out of local minima. This allows to vastly increase the convergence basin without any loss of accuracy. A wide range of application is then possible, without modification, such as wide-baseline stereovision or non-rigid surface registration.

![Reference image][Daisy1] ![Second image][Daisy2] ![Depth][Daisy3]
{: .standalone }

[Daisy1]: {filename}/images/daisy/4.png "Reference image"
[Daisy2]: {filename}/images/daisy/2.png "Second image"
[Daisy3]: {filename}/images/daisy/42.png "Computed depth map with detected self-occlusions in green"
