# /SECONDSOCIAL

Locked baseline for The Second Half Guide social engagement engine.

## Operating rule
One story at a time:
1. Rank topical candidates.
2. Activate one story.
3. Re-verify against current primary/issuing sources.
4. Generate platform-specific News Style creative.
5. Apply Footer Option B:
   - TheSecondHalfGuide.com
   - Real information for what's next.
   - PLAIN FACTS • CHECKED AND DATED
6. Human approval of exact assets and copy.
7. Automatic live production URL check.
8. Schedule/publish only to connected, approved networks.
9. Mark campaign complete.
10. Unlock next story.

## Never
- Never publish before fresh verification.
- Never treat a failed fetch as proof of a live article.
- Never auto-post the same item across Facebook Groups.
- Never allow the next story to become active while the current one is incomplete.
- Never retain approval after facts/copy/creative are materially regenerated.

## Current current-story blocker
The intended production URL https://thesecondhalfguide.com/medicare-90-payment returned HTTP 404 on Oct. 10, 2026. Publishing must remain blocked until the article exists and passes the automatic check.

## Current Metricool state
Brand exists (blogId 6788930) but no social networks are connected.

## Production architecture
- /secondsocial/ — production queue/approval UI
- /secondsocial/setup.html — setup/connect checklist
- /secondsocial/queue.json — topical queue seed/state
- /api/secondsocial/check-url.js — live destination validator
- Metricool — scheduling/publishing/analytics after user authorization
- Facebook Groups — discovery + rules + human approval; not mass automation
