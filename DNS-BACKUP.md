# DNS backup — nutricam.app

Captured 2026-08-26. A cutover to Vercel was attempted and **reverted the same
day** — the domain stays on GitHub Pages. The records below are the live config,
not a historical snapshot. See "Why the Vercel move was abandoned" at the end.
Registrar: Namecheap (`dns1.registrar-servers.com` / `dns2.registrar-servers.com`).

## A records — LIVE (GitHub Pages)

| Type | Host | Value | TTL |
|---|---|---|---|
| A | @ | 185.199.108.153 | 1800 (Automatic) |
| A | @ | 185.199.109.153 | 1800 (Automatic) |
| A | @ | 185.199.110.153 | 1800 (Automatic) |
| A | @ | 185.199.111.153 | 1800 (Automatic) |

## AAAA records — LIVE (GitHub Pages IPv6)

| Type | Host | Value | TTL |
|---|---|---|---|
| AAAA | @ | 2606:50c0:8000::153 | 1800 (Automatic) |
| AAAA | @ | 2606:50c0:8001::153 | 1800 (Automatic) |
| AAAA | @ | 2606:50c0:8002::153 | 1800 (Automatic) |
| AAAA | @ | 2606:50c0:8003::153 | 1800 (Automatic) |

No `www` record existed.

## Records NOT part of the website — leave alone

**Rule: the only records the website owns are the apex `A` and `AAAA` entries
above. Everything else in the Namecheap list stays, whatever it looks like.**

Email runs on Namecheap PrivateEmail and there is more of it than is obvious:

| Type | Host | Purpose |
|---|---|---|
| MX | @ | `mx1.privateemail.com` / `mx2.privateemail.com`, priority 10 |
| TXT | @ | SPF — `v=spf1 include:spf.privateemail.com ~all` |
| CNAME | mail | `privateemail.com` (webmail) |
| TXT | mail | SPF + two `google-site-verification=` tokens |
| TXT | default._domainkey | DKIM public key (long RSA blob) |

Deleting any of these breaks sending, receiving, or deliverability. DKIM in
particular fails silently — mail still sends, it just starts landing in spam.

No CAA record exists, which is what lets GitHub Pages (and any future host)
issue a cert. If you ever add one, authorize whichever CA your host uses or
HTTPS breaks.

## Why the Vercel move was abandoned

DNS was pointed at Vercel's apex IP `216.198.79.1` and the static site deployed
fine, but the domain never verified and no TLS cert issued. `http://nutricam.app`
came back `Server: Vercel` with `Vary: rsc, next-router-state-tree` and a
`Set-Cookie: dub_id_nutricam.app__root` — a Next.js / Dub.co app, not this site.
Another Vercel project already holds a claim on `nutricam.app`, so Vercel
demanded an ownership TXT challenge at `_vercel.nutricam.app`. That TXT was
never added; the records were restored to GitHub Pages instead.

The domain has been detached from the Vercel project, so nothing there is
competing for it now.

## If you retry Vercel later

1. Point apex `A @` at `216.198.79.1` (Vercel has no apex AAAA — delete the four
   GitHub AAAA records, since clients prefer IPv6 and any leftover AAAA silently
   keeps traffic on GitHub Pages).
2. Resolve the Dub.co / other-project claim first, or add the `_vercel` TXT
   ownership challenge Vercel hands you at that time. The old challenge value is
   dead — request a fresh one.
3. The deployment itself already works: `nutricam-sandy.vercel.app`, project
   `mklgrws-projects/nutricam`, config in `vercel.json` (`cleanUrls`).
