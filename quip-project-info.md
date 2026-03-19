# Quip

This is something I've been working on and off since early 2022. It's a microblogging app, pretty similar to Twitter of the old times, with some little features I've always wanted included, and some other stuff intentionally excluded.

It uses SolidJS for front-end and Fastify + MongoDB for back-end.

It might not be as super cool or maybe even as useful as many projects others have done, but it was super fun creating something like this from scratch, and I learned a lot of things through the process. Even my first ever NPM package, [Formzilla](https://www.npmjs.com/package/formzilla), was created as a companion project to this because existing form data handler plugins for Fastify failed to do what I needed. So, please be a bit easy with any criticism, alright?

Nifty Features:

---

- Non-English languages may use grapheme clusters as building blocks of a word rather than individual characters. The app calculates character count using that logic; so the 256 character limit would allow even longer strings than the 280 of Twitter for such languages.
- Polls have a NOTA (None of the Above) option that allows a user to forfeit their vote and just view the results. NOTA votes are not counted towards the total number of votes polled.
- A user can edit a post. But editing is allowed only once, and it will remove all the stars and reposts, plus invalidate any replies and quotes that are not from the post author themselves. The rationale for this is that (a) editing should be used for only correcting minor errors and (b) someone should not be able to post something, get a reaction from another user, and then edit their post to make it look like the other user said something they had not intended.
- When a user blocks/mutes someone, they can optionally specify a reason for doing so, and see that reason later when looking at their profile.
- Following/followers count and favourited posts are private (a decision made long before Twitter made likes private).
- Mentions are public! With existing microblogs, the search feature would allow anyone to see the mentions to anyone else, so I decided to include that in the profile itself.
- No notifications. You have to go to your profile to see if anyone new followed you or replied to one of your posts. Why? To reduce distractions. You should be the one using social media and not the other way around.
- No doom-scrolling. Having a "Load More" button instead of automatically loading the next batch of posts allows the user to choose when they are done.

Issues:

---

- Poor accessibility: My sincere apologies to people using assistive technologies. I was not a UI guy when I started building the front end and didn't know about the importance of accessibility. I learned a lot about it recently and this is what I consider the most important problem that needs to be addressed.
- Search is currently very limited. The API allows a lot of operators but only a small subset have been tested and implemented.
- The emoji picker is broken as heck. It may seem OK at first but you'll notice the issues if you use the site frequently enough.
- There might be any number of other UI/API bugs that I haven't caught yet.
- So much stuff to add: bookmarks, votes, activity timeline (anyone remember back around in 2010 when Twitter had it?), top posts (public/user-wise), hashtags, user settings, email verification, password change/recovery, protected profiles, follow requests, lists, profile deactivation … the endpoints are all there but no UI.
- Direct messaging: My initial plan was to not have it at all, but I'm having second thoughts, yet still on the fence about it.

UI repo: [https://github.com/FlameWolf/quip](https://github.com/FlameWolf/quip)

API repo: [https://github.com/FlameWolf/quip-api-v2](https://github.com/FlameWolf/quip-api-v2)