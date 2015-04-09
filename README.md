# Student Voting Framework
The Student Voting Framework or STF is an online voting framework/application specifically tailored for the needs of a
student government election. In student elections there are often numerous issues with online voting. Existing systems 
lack many key features that are necessary for proper online elections, namely the following:

* They can be very expensive, something students will struggle to afford
* Difficult to properly authenticate with existing school logins
* Don't have the ability to use non-standard voting systems (eg. STV or any run-off voting system)
* Those that do exist often can't handle very large spikes of traffic

We solve this we using what is effectivly meta programming. You can generate your own voting client
from STF by creating a configuration file and a candidate list plus some set of data used for validating voters. This 
allows us to do a lot that wouldn't otherwise be possible such as:

* The page is static only making API calls for authentication and voting. This is fairly cheap for your server and means
the majority of our requests can be handled by CDNs. This means that you can host this on a fairly cheap server (or 
even free server) without having poor performance.
* High degree of modularity with regards to authentication, allowing the user to use a wide variety of authentication
systems, or to build there own domain specific one for their schools servers

This is very much a work in progress and how many of these goals will be accomplished have not yet been determined. If
you're interested in this project and are interested in using it for your own organization feel free to get in touch 
with me. All my relevent contact info is at my website: http://webbdev.ca/