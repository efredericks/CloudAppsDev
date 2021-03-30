> By the end of this module, you'll gain experience with Kubernetes, Google's orchestration engine for containers.

> Module videos:

* [Kubernetes Overview []]()

> Module labs:

* [Qwiklabs - Kubernetes in Google Cloud Quest [25 credits]](https://www.qwiklabs.com/quests/29)

## Docker Blurb

The point of this post isn't necessarily to dig into containers however (we'll assume that's par for the course, though here is an overview on Docker to help you otherwise: [Introduction to Docker](https://medium.com/swlh/introduction-to-docker-96aad5eabb30)).

You are arriving at Kubernetes in an interesting time.  As of this posting, it recently announced that Kubernetes is planning to remove `dockershim` support, which enables communication between Docker containers and Kubernetes.  Docker containers will still be supported, however that support is being moved from the Kubernetes codebase.

To understand how a container runtime functions, I recommend you check out [this article](https://medium.com/cri-o/container-runtimes-clarity-342b62172dc3).

As an aside, a great overview of both Docker and Kubernetes can be found here (put together by a former student): [Brian Anstett - K8 Presentation](https://github.com/briananstett/k8-presentation).

## What is Kubernetes?

> Note, much of this overview comes from the following two articles:
> * [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
> * [What is Kubernetes? The Complete Guide](https://phoenixnap.com/kb/what-is-kubernetes)

> Module video: [Kubernetes Overview []]()

Kubernetes is an orchestration service for managing containers, their deployments, and their configurations.  Assuming we understand the purpose of the container (i.e., provide a fairly robust method for delivering a seamless application experience across different devices), Kubernetes sits on a layer above to enable oversight on container deployments.

<img style="background: #fff" src="https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg" alt="Kubernetes Overview" title="Kubernetes Overview" />

Kubernetes can be configured via an API for initial/ad-hoc updates or by loading configuration files that specify all the particulars necessary for defining parameters such as namespaces, images, replicates, etc. (see [Kubernetes Configuration](https://kubernetes.io/docs/concepts/configuration/overview/))

Kubernetes comprises three aspects: a master node, worker nodes, and pods.  

* **Master node**: manages the deployed cluster, supporting networking, API calls, scheduling, etc.
* **Worker node(s)**: performs tasks running containers and their workloads
* **Pods**: wrapper for containers

Typically, scalability is enabled by adding pods (scaling up) or removing pods (scaling down).  Let's take a look at the architecture.  Figure 1 (c/o kubernetes.io) shows all the components of a Kubernetes cluster:

<img style="background:#fff" src="https://v1-18.docs.kubernetes.io/images/docs/components-of-kubernetes.png" title="Kubernetes Components" alt="Kubernetes Components" />

> Figure 1: Kubernetes Components (c/o kubernetes.io)

In Figure 1 we see the *Master node* (i.e., Control Plane) on the left comprising multiple managing services (i.e., `kube-api-server`, etc.) and `etcd`, the key-value store that manages Kubernetes cluster data.  On the right we see the *Worker nodes*, where the *pods* are internal to the worker nodes.

Since we've been talking about pods, Figure 2 (c/o WikiPedia) shows a view of how they fit in with the Kubernetes scheme (the [WikiPedia article](https://en.wikipedia.org/wiki/Kubernetes) is pretty good as well if you want another perspective):

<img style="background:#fff" src="https://upload.wikimedia.org/wikipedia/commons/6/63/Pod-networking.png" title="Pod/Service Interaction" alt="Pod/Service Interaction" />

> Figure 2: Pod/Service Interaction (c/o WikiPedia)

Here, you see that each pod has its own IP address and encapsulates a number of containers.  Essentially, the pod is the **scheduling unit** of Kubernetes -- it is in charge of managing and running the containerized applications.  Of note here is that each pod is a separate entity; containers within a pod can talk to each other directly (i.e., via `localhost`)   but must access remote containers (i.e., within a different pod) via the other pod's IP address.

### Managing Kubernetes Clusters

We can interact with Kubernetes via the `kubectl` command - you'll have used this when working with `GKE` and you'll be getting more experience with it in this module.  It is similar to `gcloud` in that we will be pretty much exclusively using it to manage our deployments (following all the initial `gcloud` setup commands for Kubernetes, that is).  Now, there are a few more terms to discuss with respect to the types of things you'll need to configure and manage when setting up and deploying GKE clusters:

**Namespaces**

**Labels**

**Replication Controllers**

These are just three of the highlights for setting up a deployment.  For an in-depth guide on the considerations you'll need (including examples of how to setup an `nginx` deployment), see this article: [The beginners guide to creating Kubernetes manifests](https://prefetch.net/blog/2019/10/16/the-beginners-guide-to-creating-kubernetes-manifests/)

It will be best to gain some experience with setting up a basic deployment.  The following Codelab and video are a good starting point for this:

> * Module video: [Spring Boot Kubernetes Deployment Demo []]()
> * Codelab: [Spring Boot Kubernetes Deployment](https://codelabs.developers.google.com/codelabs/cloud-springboot-kubernetes)

The lab you need to do here (for credit, still attempt the Codelab above for practice!) is the Kubernetes Qwiklabs quest.  It will take you through building up a Docker container to deploying a Kubernetes cluster.  Definitely good practice!

* Module lab: [Qwiklabs - Kubernetes in Google Cloud Quest [25 credits]](https://www.qwiklabs.com/quests/29)

## Cloud Build and Cloud Run

We have looked at Cloud Build and Cloud Run in the past (see [Automation](/CloudAppsDev/_posts/10-Automation.md)), however it is worth discussing again in the context of container orchestration.  

TBD

> * [Building a SlackBot with Cloud Build, Cloud Run, and Node.js Part 1 [13:20]](https://youtu.be/kYUUEvBT4Ms)
> * [Building a SlackBot with Cloud Build, Cloud Run, and Node.js Part 2 [19:09]](https://youtu.be/xpPTR05Bxdc)

## Additional Resources

* [Introduction to Docker](https://medium.com/swlh/introduction-to-docker-96aad5eabb30)
* [Container Runtime eFunctions](https://medium.com/cri-o/container-runtimes-clarity-342b62172dc3)
* [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [What is Kubernetes? The Complete Guide](https://phoenixnap.com/kb/what-is-kubernetes)
* [Container runtime](https://medium.com/cri-o/container-runtimes-clarity-342b62172dc3)
* [Kubernetes Configuration](https://kubernetes.io/docs/concepts/configuration/overview/)
* [Brian Anstett - K8 Presentation](https://github.com/briananstett/k8-presentation)
* [The beginners guide to creating Kubernetes manifests](https://prefetch.net/blog/2019/10/16/the-beginners-guide-to-creating-kubernetes-manifests/)
* [WikiPedia - Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)