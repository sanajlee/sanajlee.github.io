# Little Reef v3

Homepage-only design update. Original Supabase stamp save/load JavaScript remains unchanged, as do `_data/publications.yml` and existing research content.

## Changes
- `index.html`: visitor stamp board moved out of `research-section` into its own window immediately below the hero; original board interior and controls unchanged.
- `_sass/_reef_safe.scss`: desktop/mobile styling for homepage; stamp board fixed at the original 440×300 coordinate dimensions. Narrow screens scroll horizontally in the board container rather than rescaling existing stamp positions.
- `assets/img/reef-scene.svg`: underwater pixel-style coral/seagrass background behind original small fish and jellyfish.

## Test before pushing
1. In the repository: `bundle exec jekyll serve`.
2. Visit `http://127.0.0.1:4000/` at desktop and mobile widths (390px and 768px).
3. Verify the stamp board is in its own window, and previously posted stamps still appear.
4. Click **leave a stamp**, choose a stamp, place it; verify it persists after refresh (note: this creates a real Supabase record).
5. Confirm the Research and Papers links and lower-page content.

The CSS only targets `body.reef-home`. No deployment was performed.
