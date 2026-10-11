# /SECONDSOCIAL — FINAL BASELINE

The Second Half Guide social engagement engine.

## Permanent operating rule
One story at a time:
1. Rank topical candidates.
2. Activate one story only.
3. Freshly verify against current primary/issuing sources.
4. Generate platform-specific creative from the locked News Style.
5. Run mandatory preflight QA.
6. Human approval of the exact creative and copy.
7. Automatic exact-article live URL check.
8. Schedule/publish only to connected, approved networks.
9. Mark campaign complete.
10. Only then unlock the next story.

## Locked visual standard
- News Style / consumer-newsroom aesthetic.
- No Medicare-ad aesthetic.
- No fake clickable buttons.
- No compressed or colliding headlines.
- No duplicated brand/footer information.
- Do not fill whitespace by crowding content; use deliberate hierarchy and useful supporting structure.
- Static square designs are built natively as square designs.
- Reel/TikTok/Shorts are built natively in 9:16. Never float a square carousel card inside a tall frame as the production design.
- One idea per vertical scene.
- CTA appears where useful, with one final CTA/end frame rather than repeated blocks.

## Locked three-line brand treatment
1. TheSecondHalfGuide.com
2. Real information for what's next.
3. PLAIN FACTS • CHECKED AND DATED

All three must be readable. They appear once per static asset or once in the appropriate end/footer treatment. Never duplicate them on the same scene.

## Exact-link standard
The destination for a story is the exact article, not the homepage.

For the current story:
https://thesecondhalfguide.com/medicare-90-payment

Platform behavior:
- Facebook Page: exact clickable URL in post text.
- Facebook Groups: exact URL if the group rules allow it.
- Threads: exact clickable URL in post text.
- Instagram Feed/Carousel: Link in bio. Put the active story as the first profile link.
- Instagram Story: native Link sticker directly to the exact article.
- Instagram Reel: Link in bio.
- TikTok: Link in bio/profile where available.
- YouTube Shorts: direct viewers to the first channel-profile link.
- Where useful, show the readable exact article path on the final graphic/frame.

## Mandatory preflight QA
A creative is not ready for approval unless:
- no overlapping or clipped text;
- headline has adequate breathing room;
- all content stays inside platform safe areas;
- both tagline/trust lines are present and legible;
- branding is not duplicated;
- source and checked date are present;
- correct platform dimensions are used;
- native 9:16 layouts are used for vertical video;
- exact article destination/link instructions are mapped;
- facts match the current verification record;
- mobile readability is acceptable.

## Current campaign
The $90 Medicare Payment: Who Gets It and Who Doesn’t
- Primary sources: CMS + Medicare.gov.
- Article URL: https://thesecondhalfguide.com/medicare-90-payment
- Live check: PASSED, HTTP 200, canonical verified, indexable.
- Creative: FINAL and user-approved.
- Preflight: PASSED.
- Status: ready for social-account connection and final scheduling/publishing.
- Next story remains locked.

## Current Metricool state
Brand exists (blogId 6788930). No social networks are connected yet.

## Facebook Groups
Group discovery can be automated. Posting cannot be mass automated.
Every group must have:
- approved-group status;
- current rules check;
- topic fit;
- per-post approval.

## Architecture
- /secondsocial/ — production queue / preflight / approval UI
- /secondsocial/setup.html — setup/connect checklist
- /secondsocial/queue.json — ranked queue state
- /secondsocial/campaigns/ — campaign verification records
- /secondsocial/connections.json — connection state
- /secondsocial/groups.json — group rules/approval registry
- /api/secondsocial/check-url.js — exact article live validator
- Metricool — scheduling/publishing/analytics after account authorization
