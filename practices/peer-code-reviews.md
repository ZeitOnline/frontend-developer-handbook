# How we use and conduct pull requests and peer code reviews
A so called _peer code review_ is in our case, a recurring action of having your code controlled for mistakes, errors or omissions by at least one better more colleagues before the code gets merged into the main code base. We believe code reviews lead to better code understanding by both parties, prevent malicious code from entering the code base and help to learn better coding skills for all participants. Additionally, it is a nice place for getting on board if you are new to the team.

## How pull requests are handled
Every code that ends in the code base of projects (at ZEIT ONLINE) has to be seen or controlled by at least four eyes. To apply this rule we generally use code reviews on _pull requests_ in github.

When we place a pull request against the master branch, we automatically request a code review. The request is automatically posted to the suitable channel in _Slack_ for instance _#website_. Pull requests are also discussed and distributed for review by colleagues if necessary in a daily meeting.

The requester usually just places the pull request, using a supplied pull request template if applicable. The _PR_ contains information about: 

- what the PR does, 
- where to start the review
- how things can be tested
- relevant stories or tickets
- and actions needed pre or post the deployment.

The title of the PR should be usable as a copy and pasted line for the record file of CHANGES of the project.

The reviewer(s) conduct a code review using the review tools of github and either comment on line, suggest changes or add code to the pull request themselves in accordance with the original requester. After the pull request is approved, the (initial) reviewer adds the description of the change (at best the title of the PR) and pre or/and post deploy actions to the `CHANGES.txt` of the project. After this, the reviewer merges the pull request. In some cases he also directly initiates a release and staging deployment and if reasonable informs the responsible person(s) for quality assurances purposes.

## What things need to be done before code is merged
Discussions about the question _what has to be done in code reviews_ almost always lead to the question _what rules, standards and qualities code should supply_ before being pull requested or rather before being merged. The peer code review on the one hand controls if these qualities are found in the supplied code.

### All code should be tested
Though we most of the time don't follow the rules of test driven development (when writing frontend code), all components on the website have to be tested for their functionality and acceptance.

### All code must be valid
All html and css must follow the applicable web standards.

### The outcome must work in all targeted browsers
Requesters have to test their code on all targeted browsers regularly during development (we supply tools for this). Nonetheless, testing this again during the review in case of suspicion is good practice. Remember: the website needs to work in all browsers does not explicitly mean it has to look the same in all browsers.

### The coding guidelines must be followed
We supply our coding guidelines, most of the time these rules (and some more) are automatically enforced by linting during the build process.

### The definition of done must be fulfilled
Does the code fulfill all points of the DoD is sometimes not a silly question.

### The non functional requirements should be fulfilled
We implemented rules for writing better code and producing morally better websites or software by placing our non functional requirements in the process. These rules involve things like placement of accessability rules, use of progressive enhancement, better performance, some of the things listed above and additionally rules about tracking and search engine optimization.

## What should be checked during code review
All the above things can be checked or rechecked during a review but there is more.

### Is the code comprehensible?
Does the code what is advertised? Is all the code needed to do this? Are there unused loops, missing ends, patterns used that are hard to understand or covering things up or hiding things?

Walk through the code, follow the path of the program if applicable.

It may also be tested if all code changes are correctly scoped to the task the code should obtain or if there are unrelated changes to other parts of the code.

### Test for complexity
Is the code as easy as needed or does it solve problems we do not had in the first place? Are there dependencies that are not needed or out of date. Did the authors embrace all possible impacts on other parts of the code base?

On the other hand, is the code _well written_, for instance by naming things properly and commenting parts that need to be commented and solely these?

### Is the code solid?
Do some _destructive tests_ with overly long texts, wrong typed user input, missing parameters. Does it work with the content management system (as opposite of: works only with the test files). If we have a module, how does this work on the website. Can multiple instances of the module placed on one page? Test for quantity, does the module work on a vast variety of page types and environments.

### Test for accessibility
Are the a11y tests written. Test the code with a11y plug-ins in the browser. Test with at least with _Voice Over_ and look for semantic markup and WAI-ARIA landmarks and attributes if needed. How does the module behave when we change font-size on user side or when high contrast mode is activated. Test all this in mobile and desktop environment.

### Test for performance
Does the code lower the overall performance of the webpage? What could be done to perform better, where can things be spared or omitted, which tactics regarding dom using, page re-/rendering and file loading can be used? Are all best practices considered?

### Test for security
Does the code in any manner introduce security problems for the user or its data or open the site for attacks like cross site scripting and the like?

## How do we handle code reviews
The code we write is owned by all the authors and team members but at the same time every pull request needs to be respected as a contribution of the individual to the collective outcome. Often there is no right or wrong, just taste but often it is completely the other way round. For many contentious issues we developed rules to obey but apart from this all coders foster their own style. To respect the approach of others and on the other side don't get defensive about change requests is the challenge of every code review.

Requester and reviewer need to meet one another midway. To help us on this way, we recommend the following approach:

- as reviewer: reserve enough time for the PR and give it your full attention
- as requester: be open and available for questions
- use the reviewing tools
- sequential arrangement: first discuss things that are not understood, then parts that do not work, at last questions of coding style and code quality
- communicate before requesting changes
- do not request changes if there is no reason
- learn from the code, learn from the discussion, learn from the requested changes
- explain everything
- plan changes and the future of the feature together, plan the deployment and the upcoming quality check by other departments
