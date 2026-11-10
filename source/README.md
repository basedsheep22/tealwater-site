# Tealwater Capital — website

Static single-page site. No build step, no dependencies.

Source files are `_src.html` and `styles.css`; `python3 build.py` combines them
into `index.html`. Deploy `index.html`.

`index.html` is **fully self-contained** — the CSS and both logos are embedded
in the file itself. Open it directly in a browser, email it, drop it anywhere:
it renders correctly with no supporting files. `styles.css` and `assets/` are
kept alongside as the editable originals.

**Headshots:** the cropped photos live in `assets/team/` as `person-1.jpg`
(Robert Sr.), `person-2.jpg` (Robert Jr.), `person-3.jpg` (Barrow) and
`person-4.jpg` (Benjamin). `build.py` embeds them into `index.html`. To swap
one, replace the file (4:5 portrait) and rebuild.

## Deploying

Push this folder to a GitHub repo, then in Vercel: **Add New → Project →
Import** that repo. Framework preset **Other**; leave build command and output
directory empty. Point the domain at it under **Settings → Domains**.

Local preview: `python3 -m http.server 8000`, then open `localhost:8000`.

## Positioning

The page describes Tealwater as a family investment group that deploys its own
capital across real estate, operating businesses, and a small number of
early-stage investments — not as an acquirer of mid-market companies. Keep it
that way. Every claim on the page should be one a counterparty can verify.

The page is deliberately broad: no check sizes, no criteria table, no deal
terms. That keeps it accurate while things are still taking shape, but it puts
the entire credibility burden on the team section and on "Where our capital
is." Those two sections have to be specific and real, because nothing else on
the page is doing that job.

Sections, in order: hero, investment ventures (power & energy, real estate, operating businesses, other), team, contact.

## Brand tokens

From the Tealwater brand sheet, set as CSS variables at the top of `styles.css`.
Type is Montserrat via Google Fonts.

| Token | Hex | Use |
|---|---|---|
| `--teal` | `#6B8E9C` | Eyebrows, rules, labels |
| `--teal-dark` | `#2C4F5A` | Hero, contact band, footer |
| `--teal-light` | `#9DB4BE` | Secondary text on dark |
| `--orange` | `#BF5700` | Calls to action only — deliberately sparse |
| `--cream` | `#F5F5F0` | Alternating section backgrounds |
| `--charcoal` | `#2D3235` | Body text |

## Placeholders

Everything in `[SQUARE BRACKETS]`. Search `index.html` for `[` to find them all.

**Blocking**

- [ ] A higher-resolution original of Robert Jr.'s headshot (current is 400px)

**Open in the bios**

- [ ] Confirm "co-founded" is the right word for Robert Sr. and Softdocs
- [ ] Confirm each LinkedIn URL is on the right person before publishing
- [ ] Robert Sr. should approve his own bio before it publishes

**Decisions**

- [ ] The Operating Businesses copy says the firm will raise additional
      capital for acquisitions. Publicly advertising capital raises can
      implicate securities rules — worth a short call with counsel before
      this publishes.
- [ ] Whether to add anything back about what you're looking for. Right now
      the only statement of appetite is two sentences in the contact section.

## Notes

- Power & Energy is the first row under Investment Ventures. No partner is named.
- The wave motif in the hero and the section divider come from the brand
  sheet's wave mark. They are the only decoration.
- Responsive to 390px, keyboard focus visible, reduced motion respected.
