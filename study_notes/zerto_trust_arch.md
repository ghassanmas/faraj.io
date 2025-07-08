
Well in essence it seems, the whole idea of this arch started as response of mistrust of networking physical attributes.

Which is understandable, given wi-fi connneciton, adoption of internet (WAN), ip spoofing, thus a device (or assest  as they call it in NIST), cannot be trusted based **on it's location** or whatever location allebly it's claiming.  

### Notes
- Also one noticable  pattern of arch, is that everything is treated as **a resource**, which remind me of how AWS, treats everything as a resource, as unsuprisingly the whole document by NIS is aimed to be used as a implmentation ref for civilain uncalssifed enteripsie (which is what AWS is).   
- In ZTA, even in private network, (VPN in today's cloud?), a device is not trusted, it will always assume by default it's attacked (this probably where the ref in pillars is not accurate), _it assume an attacker is masqudaring a device not that a device is comprised?_ [^1]
	- Ref 2.2.1 page 8 of res A

And a response to that is "Authtincation & Authorizaiion", session baseed...etc. Which seems to be related to what is typically used in WEB? 

**One main question arise**?: 
_Doesn't treating of all request as outsider and only trust other attriubtes like sessions and other also opens the door for other attacks..., i.e. an attacker dosen't need to know detalis of the private network, as long as they have access session's metadata?_

**In regard of pillar article?**
Still not sure if it assume device is comprised, it mostly just s


### Trivia 
- PEP abbreviation to Policiy enforcment point in ZTA, not to be cofused with Pyhon Enhancment proposal

Resources:
-A:  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf 

[^1]: Page 8 point 1 in section 2.2 page 8 of NIST SP800-207 