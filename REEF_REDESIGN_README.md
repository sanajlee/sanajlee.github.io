# Soft Retro Web × Little Reef — homepage prototype

This is a **homepage-only** redesign on top of the uploaded Jekyll source.

## Files changed
- `index.html`: same hero information, research copy, selected-paper Liquid loop, and **original Supabase stamp logic**, with a new reef scene and retro-window containers.
- `_sass/_reef_home.scss`: new homepage-specific styling and responsive rules.
- `assets/css/main.scss`: imports the new stylesheet.
- `_layouts/default.html`: adds `reef-home` class only on the homepage.
- `_includes/main/header.html`, `_includes/main/footer.html`: display sea-creature sprites only on the homepage; other pages retain their previous artwork.
- `assets/img/reef-fish.svg`, `assets/img/reef-jelly.svg`: original SVG pixel sprites.

## Preserved
- All existing data files and page bodies; publications are still rendered from `_data/publications.yml`.
- `daily_stamps` Supabase table, anonymous sign-in, loading/upsert code, element IDs, stamp image paths. No backend migration.
- The existing Paper-Reef project is untouched.

## Before deployment
1. Run `bundle install` and `bundle exec jekyll serve` in the root folder, then open `http://localhost:4000`.
2. Verify layout on desktop and mobile, visit every navigation link, and exercise the stamp picker. **Testing real stamps writes to the existing live backend** unless you arrange a test environment.
3. Publish only after testing; this package intentionally omits generated `_site`, `.git`, and macOS metadata.

## Limitations
- The prototype is a CSS-based interpretation of the approved mockup, not the exact painted background from the image.
- Jekyll build and live Supabase interactions were not executed in this environment.
