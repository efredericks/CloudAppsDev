> By the end of this module, you'll gain experience with Kubernetes, Google's orchestration engine for containers.

> Module videos:

* [Kubernetes Overview []]()

> Module labs:

## Docker Blurb

The point of this post isn't necessarily to dig into containers however (we'll assume that's par for the course, though here is an overview on Docker to help you otherwise: [Introduction to Docker](https://medium.com/swlh/introduction-to-docker-96aad5eabb30).

You are arriving at Kubernetes in an interesting time.  As of this posting, it recently announced that Kubernetes is planning to remove `dockershim` support, which enables communication between Docker containers and Kubernetes.  Docker containers will still be supported, however that support is being moved from the Kubernetes codebase.

To understand how a container runtime functions, I recommend you check out [this article](https://medium.com/cri-o/container-runtimes-clarity-342b62172dc3).

As an aside, a great overview of both Docker and Kubernetes can be found here (put together by a former student): [Brian Anstett - K8 Presentation](https://github.com/briananstett/k8-presentation).

## What is Kubernetes?

Kubernetes is an orchestration service for managing containers, their deployments, and their configurations.  Assuming we understand the purpose of the container (i.e., provide a fairly robust method for delivering a seamless application experience across different devices), Kubernetes sits on a layer above to enable oversight on container deployments.

<img style="background: #fff" src="https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg" alt="Kubernetes Overview" title="Kubernetes Overview" />

Kubernetes can be configured via an API for initial/ad-hoc updates or by loading configuration files that specify all the particulars necessary for defining parameters such as namespaces, images, replicates, etc. (see [Kubernetes Configuration](https://kubernetes.io/docs/concepts/configuration/overview/))





## Cloud Build and Cloud Run

> * [Building a SlackBot with Cloud Build, Cloud Run, and Node.js Part 1 [13:20]](https://youtu.be/kYUUEvBT4Ms)
> * [Building a SlackBot with Cloud Build, Cloud Run, and Node.js Part 2 [19:09]](https://youtu.be/xpPTR05Bxdc)

## Additional Resources

* [Introduction to Docker](https://medium.com/swlh/introduction-to-docker-96aad5eabb30)
* [Container Runtime eFunctions](https://medium.com/cri-o/container-runtimes-clarity-342b62172dc3)
* [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Container runtime](https://medium.com/cri-o/container-runtimes-clarity-342b62172dc3)
* [Kubernetes Configuration](https://kubernetes.io/docs/concepts/configuration/overview/)
* [Brian Anstett - K8 Presentation](https://github.com/briananstett/k8-presentation)