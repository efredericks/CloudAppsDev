> By the end of this module, you'll gain experience in scheduling tasks and look to the future.

> Module videos:

> Module labs:

## Cloud Scheduler

![Cloud Scheduler](https://lh3.googleusercontent.com/7Tj7GbCtbDs0Wi3bumiWp7SqPZr59YiRahFiiaomfAnR9yXdNn4Hahid7flm9mT1gYKIBG8tjqHT=e14-rj-sc0xffffff-w2540 "Cloud Scheduler")

> Cloud Scheduler

[Cloud Scheduler](https://cloud.google.com/scheduler) is basically a managed cron service -- meaning that it is used for scheduling repeated tasks (though now task scheduling is a service as a well).  If you are not aware of [cron](https://opensource.com/article/17/11/how-use-cron-linux), it is a service you use on a workstation or server to schedule tasks that are to be performed more than once (i.e., repetitively).  Examples could be log rotation, triggering software updates, security scanning, etc.  A similar service is available in Windows environments as well, though we'll call them Scheduled Tasks there.  Regardless, Cloud Scheduler takes this notion and elevates it to a cloud service.

Why is this important?  Managing scheduled tasks can be a necessary part of any IT service and/or developed application, and moving scheduling to the cloud enables you to manage them all from a central interface without needing to go into each and every separate service to trigger your cron jobs.  Moreover, you can trigger them in multiple ways, from endpoints (i.e., Cloud Endpoint), to a Pub/Sub message, to a RESTful service call. 

It is also possible to support retry activities as well, meaning that if a job failed you can have it automatically retry to complete its task.  

Let's take a look at scheduling a few tasks, then you'll get some experience with it as well.  Figure X shows the page you get when you visit the Cloud Scheduler (as always, search for it with the top bar or check the hamburger menu on the left ... it is towards the bottom of the list).

![Cloud Scheduler Creation](/CloudAppsDev/assets/images/15-scheduler.png "Cloud Scheduler Creation")

> Figure X: Cloud Scheduler Creation

You first are asked to pick a region for the scheduler (the regions should look familiar by now) and then to provide the particulars of the job.  Figure X shows the particulars of a job.  Note that if you're familiar with cron syntax you should have no issue here.  If you have no idea what cron is I highly suggest you look into a tool like [this one](https://crontab.guru/) for helping you with its syntax.  Double note: Google provides a [separate page for their cron syntax as well](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules#defining_the_job_schedule).

![Cloud Scheduler Job](/CloudAppsDev/assets/images/15-job.png "Cloud Scheduler Job")

> Figure X: Cloud Scheduler Job

Figure X next shows you what targets are currently available to be triggered via the Cloud Scheduler.  Note that you will need whatever service receiving the job to have been previously setup (e.g., if you're using Pub/Sub, you should already have a Pub/Sub environment up and running and ready to execute whatever command you're scheduling!).

![Cloud Scheduler Job Target](/CloudAppsDev/assets/images/15-jobtarget.png "Cloud Scheduler Job Target")

> Figure X: Cloud Scheduler Job Target

The payload options will change based on which type of target you select.  For example, Pub/Sub will be looking for a topic and payload (terms you should know from the Pub/Sub section).  HTTP (as shown in Figure X) looks for a URL, method (GET, POST, etc.), and the body of the message.

![Cloud Scheduler Job Target - HTTP](/CloudAppsDev/assets/images/15-jobhttp.png "Cloud Scheduler Job Target - HTTP")

> Figure X: Cloud Scheduler Job Target - HTTP

Why would we use this service other than for the obvious reason of centralizing our repetitive tasks?  There is a nice list of use cases in [this article (Task Scheduling made easy by Google Cloud Scheduler — A managed cron service)](https://medium.com/pankaj-khuranas-blog/task-scheduling-made-easy-by-google-cloud-scheduler-a-managed-cron-service-136bdf8b3111) (that I highly recommend you read).  

Next, we'll take a look at Cloud Tasks (and, how it is different from Cloud Scheduler).

## Cloud Tasks

## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.

* [Cloud Scheduler](https://cloud.google.com/scheduler)
* [Cloud Tasks](https://cloud.google.com/tasks)
* [Cloud Tasks vs. Cloud Scheduler](https://cloud.google.com/tasks/docs/comp-tasks-sched)
* [Task Scheduling made easy by Google Cloud Scheduler](https://medium.com/pankaj-khuranas-blog/task-scheduling-made-easy-by-google-cloud-scheduler-a-managed-cron-service-136bdf8b3111)