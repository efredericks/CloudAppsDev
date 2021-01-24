> By the end of this module, you'll gain experience with cloud security and provider vs. consumer responsibilities with respect to security.

> Module videos:

> Module labs:

## Cloud Security


## Google Cloud Security Model

For reference, here are links to Amazon's and Microsoft's cloud security models:

* [AWS Security Model](https://docs.microsoft.com/en-us/azure/security/fundamentals/overview)
* [Azure Security Model](https://docs.microsoft.com/en-us/azure/security/fundamentals/overview)

If you were to read through the articles (and I suggest you do ... nice to see what the other providers do as well!), you might notice some similarities.  Most notably the **shared responsibility** model!  What this means is that the cloud provider ...

### IS NOT RESPONSIBLE FOR ALL YOUR SECURITY CONCERNS!!!

Keep this in mind as you have responsibilities as well.  One of the biggest points of weakness in any cloud-based application is in **not understanding how security works**.  By this point you should realize that security is a concern; I am certain you all have heard of data leaks, hacks, etc., in large companies or cloud hosts.  Private data being leaked, pictures stolen, backdoors discovered, etc.  All of these problems tend to stem from weak security rather than coordinated efforts (though such efforts do exist, let's not trivialize that). 

Now, the provider does have some responsibility in this matter and does provide you the capabilities to secure your applications.  However, if you do something silly like set a trivial password for your virtual machines then all that sophisticated security is useless.  

> Personal example!  I had a group of students learning on temporary Windows virtual machines and had them set a password of `Temp12345` for a login.  Oddly enough, some of the machines were hacked and turned into a Bitcoin-mining botnet.  Google quickly realized what was happening and shut down the machines and sent me and the students a nasty-gram, however it was a sobering learning experience.  How were the machines discovered, you might ask?  Well, there tend to be a lot of bots on the internet constantly scanning for weakpoints, poor passwords, etc.  They most likely were targeting Google-specific IP address ranges and were testing for points of failure.  Well, they found one! 

The point of this little diversion is that your cloud provider will do its best to provide a good perimeter defense against attacks. However, you are just as important in this chain of security as your users and your provider are.  The provider can sandbox your services/tools such that others aren't impacted, but those services/tools/virtual machines/etc. that you make publicly available sure can be impacted.  Essentially, you yourself must configure security appropriately.  You must understand how the tools work, understand the current best practices, **continually keep learning and understanding how security threats evolve over time**, and educate your users to not needlessly expose themselves to attack.  

(The reason I added the bold font in that last sentence was that security attacks and threats are always evolving -- so too must you as the architect of your cloud applications!)

Keep in mind that lost data not only introduces technical concerns, but the trust you may have built with your users is completely lost.  Would you trust a company with your business if they can't be bothered to practice basic security principles?  

Ok, soapboxing complete.  Let's look at what Google does from a security perspective.   Figure X (c/o Google) presents a view of their infrastructure security layers:

![Google Infrastructure Security Layers](/CloudAppsDev/assets/images/8-google-layers.png "Google Infrastructure Security Layers")

> Figure X: Google Infrastructure Security Layers

This figure demonstrates that security must be built into **every single layer of the system as a whole**, from hardware to operational security.  Essentially, security must be distributed throughout all aspects of a project, thereby reducing single points of failure!

## Encryption

## Cloud Identity and Access Management (IAM)

## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.