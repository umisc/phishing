phishing
========

Resources and a simple Python server demonstrating password phishing.

Concept
-------

Phishing is, in a modern sense, a social engineering attack using emails, instant messaging, and the like to try to get a victim to do something. In a traditional sense, this "something" is usually to divulge some information: most commonly a username and password combination. In a more modern sense, the user may also be tricked into doing something like running a malicious payload.

Spear phishing is the same attack but researched and delivered personally to a specific target. This kind of attack is very successful and accounts for the majority of successful attacks on corporate as of 2017.

Mitigation
----------

Similar to most, if not all, social engineering attacks, phishing exploits the user rather than the business and therefore mitigation may not be possible. In the case of stealing usernames and passwords, little can be done without affecting usability: forcing Two-Factor Authentication is a possible solution. A better idea is to ensure your customers know about about these kinds of attacks and how to prevent them, though obviously this will not be completely effective.

Most of the "effective" mitigation for phishing is actually a mitigation for when information is leaked. As with other social engineering attacks, a business should have structures and routines in place for the handling of sensitive information and should teach this well to all employees and users.

Installation
------------

Included with this repository is a simple phishing page run on Flask. It is intended to demonstrate a phishing page during a MISC session.

You must have:

-	python >= 2.7, >= 3.5
-	Flask

After cloning the repository and `cd`ing into the legitbank.org directory, simply run:

```bash
$ sudo python run.py
```

Ensure you do not have anything else listening on port 80. Because this is such a simple app with a number of security flaws, I do not recommend hosting it using a web server such as nginx: just run it as a Python app and tear it down when you're done.

Security
--------

-	Rate limiting is not enabled.
-	Log rotation is not enabled.
	-	Coupled with a lack of rate limiting, if the server is left up for longer than required, the logs can take up a significant part of disk space very quickly.
-	Inputs are not checked or sanitised.
	-	Severity varies by Flask version.
