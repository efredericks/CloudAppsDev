> By the end of this module, you'll gain experience with cloud networking, virtual private clouds, and IP addressing.

> Module videos:

> Module labs:

## Cloud Networking

Time to discuss networking!  Sure would be a shame if all those nifty services you're working on couldn't talk to the rest of the world, right?  Well, here we're going to cover how to get them all talking. 

Take what you know of standard networking and scale it up significantly, and you have cloud networking.  Sandboxed networks?  Yep.  Subnets?  Yep.  Network partitioning and load balancing?  Sure!

Plus a lot more, time to get into it.

## Networking Background

A quick refresher on terminologies:

* Devices in a *single location* are connected via local-area network (LAN).  Only devices participating in this network can talk to each other (VPN connections are considered to be 'local,' though can be treated differently).
* Wide-area networks (WAN) connect multiple LANs together, enabling a wider range of communication.

We'll skip the less-commonly-used metropolitan-area network.  Just consider that, in present times, most devices are connected to the Internet, which is effectively just a WAN of massive scale.

![LAN vs. MAN vs. WAN (c/o Viva Differences)](https://vivadifferences.com/wp-content/uploads/2019/07/LAN-VS-MAN-VS-WAN.png "LAN vs. MAN vs. WAN - c/o Viva Differences")

> LAN vs. MAN vs. WAN (c/o Viva Differences)

With networking at scale comes the benefit of being able to work with your infrastructure and devices remotely (i.e., if a fire (either literally or figuratively) starts in the middle of the night, all you need to do is login and remotely fix the problem).

Figure X (c/o Google) shows an image of their private network and access points as of 2020.  AWS and Azure provide similar capabilities; if you want to have a fast response from your cloud provider then you will need nearby access!

![Google Cloud Network](/CloudAppsDev/assets/images/9-gc-network.png "Google Cloud Network")

> Figure X: Google Cloud Network

Let's say that you want to connect your infrastructure to Google Cloud (or similar).   To do so you will need to provide some sort of connectivity between your servers and your cloud provider's.  Figure X (c/o Google) shows their strategy for doing so.  Here, you'll notice how a service-oriented cloud architecture can hook into yours.  For instance, your data center can connect to [Google Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect) (a service for extending your network to Google's) and then to [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview) (a service for connecting to a virtual private cloud network).  Alternatively, your servers and/or your clients can connect directly to the various cloud services as well.   These can be supported by name resolution services (i.e., [Cloud DNS](https://cloud.google.com/dns)) and load balancing (i.e., [Cloud Load Balancer](https://cloud.google.com/load-balancing)) for distributing traffic amongst servers.

![Google Cloud Networking](/CloudAppsDev/assets/images/9-gc-networking.png "Google Cloud Networking")

> Figure X: Google Cloud Networking

## Virtual Private Cloud (VPC)

A VPC network is essentially a small sandboxed network for your projects to live in.  They are built on top of the Google private networking environment.  Here, you can apply many of your "usual" techniques for securing a network (firewalls, access control, etc.).  VPCs are software-defined network (SDN) constructs that can be used for deploying services such as compute instances, containers, etc.  There are no 'real' IP address ranges  (they must be defined as subnets and then internal ranges tend to be 10.* and external are at the whim of Google).  VPCs are global in nature as well, meaning you can access your VPC from any location that has Internet access.  You can also create sub-networks (subnets) as well in particular regions or zones for partitioning your VPC network.

Figure X (c/o Google) shows an overview of a VPC network, comprising subnets that are region/zone specific.  Here, you can see how an on-prem (or remote) client can connect remotely to a VPC network to access Compute VM instances in various regions.

![Google Cloud VPC Network](/CloudAppsDev/assets/images/9-vpc.png "Google Cloud VPC Network")

> Figure X: Google Cloud VPC Network

The figure above shows how subnets are *regional resources*.  If you want a usable set of IP address ranges, then a subnet must be created (otherwise, you get the 'default' IP address range). Interestingly, virtual machines in different zones, but in the same region, can share the same subnet!

Back to Figure X, you see `subnet` defined as `10.240.0.0/24` in `us-west1`.  There are two virtual machine instances in zone `us-west1-a`.  Their IP address assignments come from the range specified for `subnet1`.

`subnet2` is defined as `192.168.1.0/24` in `us-east1` (region).  There are two virtual machine instances in zone `us-east1-a`, where their IP addresses are defined from `subnet2`.  

Now, `subnet3` is set to be `10.2.0.0/16`, but also within the `us-east1` region.  There is one virtual machine in zone `us-east1-a` and another in zone `us-east1-b`, where both virtual machines get their IPs from the range available to `subnet3`.  They may each have their own network interface (as a result of being a *regional resource*), however still can talk to each other as they're on the same subnet.

Figure X (c/o Google) shows how resources in different regions *yet the same VPC* can communicate.  For instance, `VM1` and `VM2` can communicate locally as they both reside within `VPC Network 1`.  They are separated geographically (`us-east1` and `asia-east1`), however by merit of being in the same VPC network they can directly talk.  However, for resources in different VPC networks an Internet connection must be made.  For example, if `VM3` and `VM4` want to talk they will need to use their **public** IP addresses rather than their **private** IP addresses (even though they're in the same region).  

![Network Behavior](/CloudAppsDev/assets/images/9-network-behavior.png "Network Behavior")

> Figure X: Network Behavior

### Subnet Creation Modes

Subnets can be created automatically or via custom rules.  While we're not going to spend *too* much time on this topic, note that automated creation tends to be good for proof-of-concept builds, whereas the finer-grained control (and less hand-holding) of the custom build is more suitable for production (Figure X, c/o Google).

![Auto vs. Custom Subnets](/CloudAppsDev/assets/images/9-auto-v-custom.png "Auto vs. Custom Subnets")

> Figure X: Auto vs. Custom Subnets

### IP Address Ranges

Let's take another trip down networking basics and talk about IP address ranges (as you should be specifying them as part of your subnets).  



## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.