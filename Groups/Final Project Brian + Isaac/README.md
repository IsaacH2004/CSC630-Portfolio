Please note: This write-up for our final project was written by Brian, not by me. 

# Commons

**[here](https://my.matterport.com/models/mQdFyk2eydi?cta_origin=all_spaces_page&section=media) is the link to the final**

In this project, we hoped to create a live and intractable infographic of the data of commons. 

*this did not work out super well*

However there were incredibly valuable takeaways from this project beyond just the end result. I have broken them down into the following categories:

# 1. DATA COLLECTION:

One of the biggest and earliest problems we faced was how to collect the data. Initially we though our problem was going to be “how can we most effectively distribute this to a community, of *uninterested* participants”, and so we brainstormed ways to maximize the advertisement, the placement, and a bunch of other community variables to get out survey in the most hands as possible.

Once we decided this rollout strategy, we focused on designing a quick, but in depth survey. This went through a bunch of revision between the two of us to get it to be the perfect balance of engagingly quick, while still giving us all the interesting data we wanted.

This led us to our *actual* problem. Thinking we should be polite, and asked someone in commons if we could throw our flyers up. **This was a mistake** We were then promptly met with a bureaucratic slowness that rivals the speed of the mighty sloth. We were forced to wait for emails that the replier had not interest in sending, and for meetings that the host had no interest in attending, and ultimately, after like two and a half weeks of just waiting, were met with the almighty **no response**

Experiencing the grand suspicion of data collection, processing, and sharing, we learned how difficult it is to collect data that someone thinks either isnt anonymous, or can hurt them in someway. Regardless of your ability to debate, or disprove their worry, a distributor will always go with their gut suspicion. 

And so we transitioned into the power of **data faking**. We plugged in some sample numbers, and sample questions into **[Mockaroo](https://www.mockaroo.com)**. And while this was great for testing the visualizations, because the form of the data it exported was the neatness excel spreadsheet you’ve ever seen, we weren’t forced to deal with and adapt to the more ‘real-world’ messy data files we would have otherwise encountered. 

# 2. THE VISUALIZATION ENVIRONMENT:

When it came time to actually visualize the data, I turned to what I have been using most of this term, and subsequently know best: **Altair**. However, considering our initial goal: to render data visualizations with changeable series (corresponding to various demographics such as food allergies or religion), I soon found out Altair lacked the capabilities to handle this demand. 

needing to find an alternative, I read up on various other popular python visualization tools, and found that all lacked in some critical area, ranging form no interaction, to no customization, to just plain bad. I eventually settled on [plotly](https://plotly.com), as it seemed to accomplish everything that i needed. However, I soon discovered the very outdated, and incongruous systems that plotly was built upon. 

There were many different ways to render the same data, but with both structures, there were key advantages and disadvantages. Though this is fine in principle, when I needed the interactive capabilities of ```graph objects``` I was quite disappointed to find out I could only render sundials with ```plotly express```.  And the two were just barely compatible. And so I grew to appreciate what it was like to work with a structure that has only added to its initial system, never revised it (and also has the worst documentation in the world, seriously what is [this](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html))

Though I did not end up learning much plotly, (really just enough to make slightly worse, and less diverse visualizations than I had hoped), I did learn a lot about the current landscape of python visualization tools: that like many other convinience-based products, there is no single product that combines the best of every other: there will always be something missing in your tool belt. 

# 3. THE FREE SERVICE PARADIGME

The final thing we learned was when we were scanning commons. Unable to use the 4K, (probably very expensive camera) that accompanied the software for creating virtual spaces, we decided to use their free alternative, your phone! We were initially very excited that this company had considered not everyone can afford their high end camera, but may still want or need their service, and so put a smaller, lower quality camera version into an app on a phone.

However, as we learned, the free alternative to this expensive service is not accessible or viable. The app had many glitches, and crashed a few times. It had difficulty aligning images, and often rejected our scans, forcing us to do them 3 or 4 times over. And despite being well lit, random areas of the building were pitch black. tough these on their own were not terrible, working with them on such a large scale made it nearly impossible to get any of the scanne we needed.

Though we both understand the technical powers and challenges that it takes to do something as advanced as what this company does, it is disappointing to see such a lousy, “accessible” alternative. 

# CONCLUSION 

Though our final is not the fancy AR experience we had hoped for, the real-world lessons that we were able to take away from the entire length of this project were very valuable! 

And so now, go enjoy a poor quality render of commons with some links on it ;))
