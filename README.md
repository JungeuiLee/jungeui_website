# Jungeui Lee Portfolio

Personal portfolio site built with Next.js 16, React 19, and Tailwind CSS 4 — a single dark-themed page covering experience, projects, skills, and contact details.

![Screenshot of the homepage](public/jungeuiPortfolio.png)

**Live:** [jungeui-website.vercel.app](https://jungeui-website.vercel.app/)

## Highlights
- Hero section with live clocks for Minneapolis and Seoul
- Custom alternating experience timeline; each entry opens a detail modal with the technologies used and key achievements
- Project cards linking straight out to repositories, the App Store listing, and written work
- Fully responsive dark UI styled with Tailwind CSS 4
- App Router setup deployable as a static build — no backend services required

## Tech Stack
- **Framework**: Next.js 16 (App Router)
- **Language**: TypeScript with React 19
- **Styling**: Tailwind CSS 4, PostCSS
- **Icons**: lucide-react
- **Images**: next/image optimization

## Project Structure
```
src/
├── app/
│   ├── layout.tsx      # Root layout, metadata, navbar
│   ├── page.tsx        # Single-page composition
│   └── globals.css     # Tailwind entry point and theme tokens
└── components/
    ├── Hero.tsx        # Intro with live time-zone clocks
    ├── About.tsx       # Background summary
    ├── Experience.tsx  # Alternating timeline + detail modals
    ├── Projects.tsx    # Project cards with external links
    ├── Skills.tsx      # Grouped skill listing
    ├── Contact.tsx     # Contact links
    └── Navbar.tsx      # Section navigation
```
