import os

# Categories and their details
CATEGORIES = [
    # Trending
    {
        "slug": "the-linen-look",
        "title": "The Linen Look",
        "badge": "Trending Collection",
        "desc": "Lightweight, breathable, and refined. Elegant linen garments crafted for effortless summer style.",
        "products": [
            {"brand": "LORO PIANA", "title": "Tailored Linen Blazer", "price": "$890.00", "image": "assets/jacket.png", "tag": "MUST HAVE"},
            {"brand": "GUCCI", "title": "Artisanal Summer Loafers", "price": "$780.00", "image": "assets/loafers.png", "tag": "BEST SELLER"},
            {"brand": "LORO PIANA", "title": "Linen Knit Throw", "price": "$480.00", "image": "assets/pillow.png", "tag": "LIMITED"},
            {"brand": "LORO PIANA", "title": "Champagne Summer Aviators", "price": "$620.00", "image": "assets/sunglasses.png", "tag": "NEW"}
        ]
    },
    {
        "slug": "warm-palette-suits",
        "title": "Warm Palette Suits",
        "badge": "Trending Collection",
        "desc": "Rich ochres, soft creams, and terracotta hues. Tailored suiting that commands a premium presence.",
        "products": [
            {"brand": "MONCLER", "title": "Amber Wool Blazer", "price": "$1,420.00", "image": "assets/jacket.png", "tag": "POPULAR"},
            {"brand": "AUDEMARS PIGUET", "title": "Classic Gold Chronograph", "price": "$24,900.00", "image": "assets/watch.png", "tag": "EXCLUSIVE"},
            {"brand": "GUCCI", "title": "Caramel Suede Loafers", "price": "$890.00", "image": "assets/loafers.png", "tag": "NEW SEASON"}
        ]
    },
    {
        "slug": "monochrome-essentials",
        "title": "Monochrome Essentials",
        "badge": "Trending Collection",
        "desc": "Timeless off-white, slate grey, and deep off-black. Minimalist foundations for the modern wardrobe.",
        "products": [
            {"brand": "KHAITE", "title": "Aethel Onyx Tote", "price": "$1,450.00", "image": "assets/tote.png", "tag": "BEST SELLER"},
            {"brand": "MONCLER", "title": "Obsidian Leather Jacket", "price": "$2,850.00", "image": "assets/jacket.png", "tag": "POPULAR"},
            {"brand": "BANG & OLUFSEN", "title": "Beoplay H95 Matte Black", "price": "$1,250.00", "image": "assets/headphones.png", "tag": "MUST HAVE"}
        ]
    },
    {
        "slug": "minimalist-leather",
        "title": "Minimalist Leather",
        "badge": "Trending Collection",
        "desc": "Fine grain leathers, structural shapes, and zero clutter. Premium accessories and garments.",
        "products": [
            {"brand": "KHAITE", "title": "Aethel Structured Tote", "price": "$1,450.00", "image": "assets/tote.png", "tag": "NEW COLLECTION"},
            {"brand": "MONCLER", "title": "Shearling Leather Aviator", "price": "$2,850.00", "image": "assets/jacket.png", "tag": "LIMITED STOCK"},
            {"brand": "GUCCI", "title": "Handcrafted Leather Loafers", "price": "$890.00", "image": "assets/loafers.png", "tag": "ARTISANAL"}
        ]
    },
    {
        "slug": "summer-knitwear",
        "title": "Summer Knitwear",
        "badge": "Trending Collection",
        "desc": "Open weave knits, lightweight cashmere, and premium cotton blends designed for summer nights.",
        "products": [
            {"brand": "FRETTE", "title": "Cashmere Knit Cushion", "price": "$480.00", "image": "assets/pillow.png", "tag": "ATELIER ONLY"},
            {"brand": "MONCLER", "title": "Knit Sleeve Windbreaker", "price": "$1,250.00", "image": "assets/jacket.png", "tag": "NEW SEASON"}
        ]
    },

    # Women
    {
        "slug": "tailored-coats",
        "title": "Tailored Coats",
        "badge": "Women's Collection",
        "desc": "Stunning silhouettes, structure, and luxurious warmth. The quintessential outer layers.",
        "products": [
            {"brand": "MONCLER", "title": "Shearling Aviator Coat", "price": "$2,850.00", "image": "assets/jacket.png", "tag": "MUST HAVE"},
            {"brand": "KHAITE", "title": "Oversized Leather Duster", "price": "$3,200.00", "image": "assets/tote.png", "tag": "NEW SEASON"}
        ]
    },
    {
        "slug": "silk-shirts-and-tops",
        "title": "Silk Shirts & Tops",
        "badge": "Women's Collection",
        "desc": "Fluid mulberry silk, delicate drapes, and premium tailored cuts. Luxurious base layers.",
        "products": [
            {"brand": "MAISON D'ÉLÉGANCE", "title": "Aurelia Eau de Parfum", "price": "$340.00", "image": "assets/perfume.png", "tag": "ESSENTIAL"},
            {"brand": "LORO PIANA", "title": "Silk Chiffon Overshirt", "price": "$920.00", "image": "assets/sunglasses.png", "tag": "NEW"}
        ]
    },
    {
        "slug": "structured-trousers",
        "title": "Structured Trousers",
        "badge": "Women's Collection",
        "desc": "Perfect pleats, high waists, and clean lines. Trousers built for sophisticated day-to-night transitions.",
        "products": [
            {"brand": "GUCCI", "title": "Horsebit Velvet Slipper", "price": "$890.00", "image": "assets/loafers.png", "tag": "POPULAR"}
        ]
    },
    {
        "slug": "summer-dresses",
        "title": "Summer Dresses",
        "badge": "Women's Collection",
        "desc": "Flowing fabrics, bright neutrals, and elegant draping. Made for sunny days and boutique events.",
        "products": [
            {"brand": "LORO PIANA", "title": "Champagne Aviator Sunglasses", "price": "$620.00", "image": "assets/sunglasses.png", "tag": "NEW"}
        ]
    },
    {
        "slug": "leather-handbags",
        "title": "Leather Handbags",
        "badge": "Women's Collection",
        "desc": "From daily structured totes to evening clutch bags. Premium leather accessories.",
        "products": [
            {"brand": "KHAITE", "title": "Aethel Leather Tote", "price": "$1,450.00", "image": "assets/tote.png", "tag": "BEST SELLER"},
            {"brand": "GUCCI", "title": "Embroidered Clutch Bag", "price": "$1,890.00", "image": "assets/loafers.png", "tag": "EXCLUSIVE"}
        ]
    },

    # Men
    {
        "slug": "overcoats-and-jackets",
        "title": "Overcoats & Jackets",
        "badge": "Men's Collection",
        "desc": "From heavy structure wool overcoats to modern utility shearling jackets.",
        "products": [
            {"brand": "MONCLER", "title": "Shearling Leather Jacket", "price": "$2,850.00", "image": "assets/jacket.png", "tag": "BEST SELLER"},
            {"brand": "BANG & OLUFSEN", "title": "Beoplay H95 Case & Headphone", "price": "$1,250.00", "image": "assets/headphones.png", "tag": "POPULAR"}
        ]
    },
    {
        "slug": "fine-knit-sweaters",
        "title": "Fine Knit Sweaters",
        "badge": "Men's Collection",
        "desc": "Superfine merino, luxurious cashmere, and cotton silk knit sweaters for every season.",
        "products": [
            {"brand": "FRETTE", "title": "Royal Silk Weave Cushion", "price": "$480.00", "image": "assets/pillow.png", "tag": "ATELIER ONLY"}
        ]
    },
    {
        "slug": "tailored-shirts",
        "title": "Tailored Shirts",
        "badge": "Men's Collection",
        "desc": "Crisp poplin, premium linen, and structured oxfords custom-tailored for peak refinement.",
        "products": [
            {"brand": "MAISON D'ÉLÉGANCE", "title": "Aurelia Oud Scent", "price": "$340.00", "image": "assets/perfume.png", "tag": "ESSENTIAL"}
        ]
    },
    {
        "slug": "casual-chinos",
        "title": "Casual Chinos",
        "badge": "Men's Collection",
        "desc": "Garment-dyed stretch cotton chinos in earth tones, tailored with clean modern fits.",
        "products": [
            {"brand": "GUCCI", "title": "Classic Velvet Loafers", "price": "$890.00", "image": "assets/loafers.png", "tag": "POPULAR"}
        ]
    },
    {
        "slug": "chrono-watches",
        "title": "Chrono Watches",
        "badge": "Men's Collection",
        "desc": "Exquisite watch craftsmanship. Chronographs and automatic timepieces from elite makers.",
        "products": [
            {"brand": "AUDEMARS PIGUET", "title": "Royal Oak Chronograph", "price": "$24,900.00", "image": "assets/watch.png", "tag": "EXCLUSIVE"},
            {"brand": "BANG & OLUFSEN", "title": "Beoplay H95 Atelier Gold", "price": "$1,250.00", "image": "assets/headphones.png", "tag": "LIMITED EDITION"}
        ]
    },

    # New Collection: The Neutral Tone
    {
        "slug": "the-neutral-tone",
        "title": "The Neutral Tone",
        "badge": "New Collection",
        "desc": "Curating a sophisticated palette of soft beiges, warm oats, and charcoal blacks. Effortless minimalist luxury.",
        "products": [
            {"brand": "KHAITE", "title": "Aethel Leather Tote Bag", "price": "$1,450.00", "image": "assets/tote.png", "tag": "NEW"},
            {"brand": "MONCLER", "title": "Shearling Leather Jacket", "price": "$2,850.00", "image": "assets/jacket.png", "tag": "LIMITED"},
            {"brand": "GUCCI", "title": "Embroidered Velvet Loafers", "price": "$890.00", "image": "assets/loafers.png", "tag": "POPULAR"},
            {"brand": "FRETTE", "title": "Royal Silk Pillow", "price": "$480.00", "image": "assets/pillow.png", "tag": "EXCLUSIVE"},
            {"brand": "LORO PIANA", "title": "Champagne Gold Aviators", "price": "$620.00", "image": "assets/sunglasses.png", "tag": "MUST HAVE"}
        ]
    }
]

# Map of text in Megamenu / Mobile Menu to replacement URLs
URL_REPLACEMENTS = {
    'href="#"': {
        "The Linen Look": "the-linen-look.html",
        "Warm Palette Suits": "warm-palette-suits.html",
        "Monochrome Essentials": "monochrome-essentials.html",
        "Minimalist Leather": "minimalist-leather.html",
        "Summer Knitwear": "summer-knitwear.html",
        "Tailored Coats": "tailored-coats.html",
        "Silk Shirts & Tops": "silk-shirts-and-tops.html",
        "Structured Trousers": "structured-trousers.html",
        "Summer Dresses": "summer-dresses.html",
        "Leather Handbags": "leather-handbags.html",
        "Overcoats & Jackets": "overcoats-and-jackets.html",
        "Fine Knit Sweaters": "fine-knit-sweaters.html",
        "Tailored Shirts": "tailored-shirts.html",
        "Casual Chinos": "casual-chinos.html",
        "Chrono Watches": "chrono-watches.html",
        
        # Mobile Menu specifics
        "Women's Collection": "tailored-coats.html",
        "Men's Apparel": "overcoats-and-jackets.html",
        "Leather Goods": "leather-handbags.html",
        "Jewelry & Watches": "chrono-watches.html"
    }
}

HTML_DIR = "/Users/mahmoudmohamed/Documents/المشاريع/shopelar"

def update_menu_links(file_path):
    print(f"Updating links in {os.path.basename(file_path)}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update logo links to point to index.html
    content = content.replace('href="#" class="brand-logo" id="nav-logo"', 'href="index.html" class="brand-logo" id="nav-logo"')
    content = content.replace('href="#" class="brand-logo drawer-logo"', 'href="index.html" class="brand-logo drawer-logo"')
    
    # 2. Update home links to point to index.html
    content = content.replace('href="#" class="nav-link active" id="link-home"', 'href="index.html" class="nav-link active" id="link-home"')
    content = content.replace('href="#" class="nav-link" id="link-home"', 'href="index.html" class="nav-link" id="link-home"')
    content = content.replace('href="#" class="mobile-nav-link active"', 'href="index.html" class="mobile-nav-link active"')
    content = content.replace('href="#" class="mobile-nav-link"', 'href="index.html" class="mobile-nav-link"')

    # 3. Replace megamenu items
    for label, target_url in URL_REPLACEMENTS['href="#"'].items():
        target_patterns = [
            f'href="#" class="dropdown-item">{label}</a>',
            f'href="#">{label}</a>',
            f'href="#" class="active">{label}</a>'
        ]
        
        for pattern in target_patterns:
            if pattern in content:
                if "class=" in pattern:
                    if 'class="dropdown-item"' in pattern:
                        replacement = f'href="{target_url}" class="dropdown-item">{label}</a>'
                    else:
                        replacement = f'href="{target_url}" class="active">{label}</a>'
                else:
                    replacement = f'href="{target_url}">{label}</a>'
                content = content.replace(pattern, replacement)
                
    # 4. Replace "The Neutral Tone" promo card CTA (Explore Now) link
    promo_target = '<a href="#" class="card-cta">Explore Now</a>'
    promo_replacement = '<a href="the-neutral-tone.html" class="card-cta">Explore Now</a>'
    content = content.replace(promo_target, promo_replacement)
    
    # 5. Replace "The Linen Series" footer link
    footer_linen_target = '<li><a href="#">The Linen Series</a></li>'
    footer_linen_replacement = '<li><a href="the-linen-look.html">The Linen Series</a></li>'
    content = content.replace(footer_linen_target, footer_linen_replacement)

    # 6. Replace About and Contact links
    content = content.replace('href="#" class="nav-link" id="link-about"', 'href="about.html" class="nav-link" id="link-about"')
    content = content.replace('href="index.html" class="mobile-nav-link">About</a>', 'href="about.html" class="mobile-nav-link">About</a>')
    content = content.replace('href="#" class="nav-link" id="link-contact"', 'href="contact.html" class="nav-link" id="link-contact"')
    content = content.replace('href="index.html" class="mobile-nav-link">Contact</a>', 'href="contact.html" class="mobile-nav-link">Contact</a>')

    # 7. Replace Profile Dropdown links
    content = content.replace('href="#" class="dropdown-item">My Profile</a>', 'href="profile.html" class="dropdown-item">My Profile</a>')
    content = content.replace('href="#" class="dropdown-item">My Orders</a>', 'href="orders.html" class="dropdown-item">My Orders</a>')
    content = content.replace('href="#" class="dropdown-item">Saved Addresses</a>', 'href="addresses.html" class="dropdown-item">Saved Addresses</a>')
    
    # 8. Replace Mobile Profile links
    content = content.replace('href="#" class="mobile-account-link"', 'href="profile.html" class="mobile-account-link"')
    
    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_category_pages():
    # Load index.html after it is updated to extract the shell
    with open(os.path.join(HTML_DIR, "index.html"), "r", encoding="utf-8") as f:
        index_content = f.read()

    # Extract shell before and after main page-container
    main_start_tag = '<main class="page-container">'
    main_end_tag = '</main>'
    
    start_idx = index_content.find(main_start_tag)
    end_idx = index_content.find(main_end_tag)
    
    if start_idx == -1 or end_idx == -1:
        raise ValueError("Could not find <main class='page-container'> structure in index.html")
        
    shell_before = index_content[:start_idx]
    shell_after = index_content[end_idx + len(main_end_tag):]

    # Process each category
    for cat in CATEGORIES:
        filename = f"{cat['slug']}.html"
        file_path = os.path.join(HTML_DIR, filename)
        print(f"Generating {filename}...")
        
        local_before = shell_before
        # Replace Home active
        local_before = local_before.replace('class="nav-link active" id="link-home"', 'class="nav-link" id="link-home"')
        local_before = local_before.replace('class="mobile-nav-link active"', 'class="mobile-nav-link"')
        
        # Highlight category link in Megamenu (desktop) and Submenu (mobile)
        desktop_target = f'href="{filename}">{cat["title"]}</a>'
        desktop_replacement = f'href="{filename}" class="active-category" style="color: var(--color-accent-gold);">{cat["title"]}</a>'
        local_before = local_before.replace(desktop_target, desktop_replacement)
        
        mobile_target = f'href="{filename}">{cat["title"]}</a>'
        mobile_replacement = f'href="{filename}" class="active" style="color: var(--color-text-primary);">{cat["title"]}</a>'
        local_before = local_before.replace(mobile_target, mobile_replacement)
        
        # Build the main body content
        main_content = f"""  <main class="page-container">
    
    <!-- Elegant Collection Hero Header -->
    <header class="collection-hero">
      <div class="collection-hero-content">
        <span class="collection-badge">{cat['badge']}</span>
        <h1 class="collection-title">{cat['title']}</h1>
        <p class="collection-subtitle">{cat['desc']}</p>
      </div>
    </header>

    <div class="collection-main">
      
      <!-- Interactive Filter Bar -->
      <div class="filter-sort-bar">
        <div class="filter-controls">
          <div class="filter-item">
            <span>Sort By:</span>
            <select class="filter-select">
              <option value="featured">Featured</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
            </select>
          </div>
        </div>
        <div class="results-count">Showing {len(cat['products'])} Pieces</div>
      </div>

      <!-- Products Grid -->
      <div class="scroll-card-grid">
"""
        # Add products
        for prod in cat["products"]:
            main_content += f"""        <!-- Product: {prod['title']} -->
        <div class="product-card">
          <div class="product-card-image-wrapper">
            <span class="card-badge-tag">{prod['tag']}</span>
            <img src="{prod['image']}" alt="{prod['title']}" class="product-card-image" loading="lazy">
            <button class="product-add-cart-btn" aria-label="Add {prod['title']} to cart">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                stroke-linejoin="round" class="cart-btn-icon">
                <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <path d="M16 10a4 4 0 0 1-8 0"></path>
              </svg>
              Quick Shop
            </button>
          </div>
          <div class="product-card-info">
            <span class="product-card-brand">{prod['brand']}</span>
            <h3 class="product-card-title">{prod['title']}</h3>
            <span class="product-card-price">{prod['price']}</span>
          </div>
        </div>
"""
            
        main_content += """      </div>
    </div>
  </main>"""

        full_content = local_before + main_content + shell_after
        
        # Replace title tag
        full_content = full_content.replace("<title>Shopelar — Premium E-Commerce Navigation</title>", f"<title>{cat['title']} — Shopelar</title>")
        full_content = full_content.replace('<meta name="description"\n    content="Experience Shopelar\'s premium, responsive, and elegant navigation bar, featuring modern design trends and smooth micro-interactions.">', f'<meta name="description" content="{cat["desc"]}">')
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_content)

def generate_about_and_contact_pages():
    # Load index.html after it is updated to extract the shell
    with open(os.path.join(HTML_DIR, "index.html"), "r", encoding="utf-8") as f:
        index_content = f.read()

    # Extract shell before and after main page-container
    main_start_tag = '<main class="page-container">'
    main_end_tag = '</main>'
    
    start_idx = index_content.find(main_start_tag)
    end_idx = index_content.find(main_end_tag)
    
    if start_idx == -1 or end_idx == -1:
        raise ValueError("Could not find <main class='page-container'> structure in index.html")
        
    shell_before = index_content[:start_idx]
    shell_after = index_content[end_idx + len(main_end_tag):]

    # --- ABOUT PAGE ---
    about_filename = "about.html"
    about_path = os.path.join(HTML_DIR, about_filename)
    print("Generating about.html...")

    about_before = shell_before
    # Set Home inactive
    about_before = about_before.replace('class="nav-link active" id="link-home"', 'class="nav-link" id="link-home"')
    about_before = about_before.replace('class="mobile-nav-link active"', 'class="mobile-nav-link"')
    # Set About active
    about_before = about_before.replace('class="nav-link" id="link-about"', 'class="nav-link active" id="link-about"')
    about_before = about_before.replace('href="about.html" class="mobile-nav-link"', 'href="about.html" class="mobile-nav-link active"')

    about_body = """  <main class="page-container">
    <header class="collection-hero">
      <div class="collection-hero-content">
        <span class="collection-badge">Our Story</span>
        <h1 class="collection-title">About Shopelar</h1>
        <p class="collection-subtitle">A heritage of conscious luxury, artisanal craftsmanship, and modern minimalism.</p>
      </div>
    </header>

    <div class="collection-main">
      <section class="about-story" style="max-width: 800px; margin: 0 auto 60px; text-align: center; line-height: 1.8;">
        <h2 style="font-family: var(--font-logo); font-size: 28px; margin-bottom: 20px; color: var(--color-text-primary); font-weight: 500;">Slow Luxury & Purposeful Design</h2>
        <p style="color: var(--color-text-secondary); font-size: 16px; margin-bottom: 20px; font-weight: 300;">
          Founded on the values of timeless refinement and conscious curation, Shopelar offers a sanctuary of minimalist lifestyle garments and premium objects. We believe that true luxury lies in the details—the choice of fluid mulberry silk, structural Italian leather, or handcrafted premium chronographs.
        </p>
        <p style="color: var(--color-text-secondary); font-size: 16px; margin-bottom: 20px; font-weight: 300;">
          Every collection is designed to integrate seamlessly into a modern capsule wardrobe, celebrating pure lines, rich neutral tones, and architectural silhouettes that transcend the seasonal cycle.
        </p>
      </section>

      <div class="scroll-card-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 60px;">
        <div style="background-color: var(--color-bg-secondary); padding: 40px; border-radius: 4px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.02); transition: transform 0.3s ease;">
          <h3 style="font-family: var(--font-logo); font-size: 20px; margin-bottom: 15px; color: var(--color-accent-gold); font-weight: 500;">Artisanal Heritage</h3>
          <p style="color: var(--color-text-secondary); font-size: 14px; line-height: 1.6; font-weight: 300;">We partner exclusively with multi-generational family ateliers who hold centuries of craftsmanship expertise in leatherwork, fine tailoring, and precision watchmaking.</p>
        </div>
        <div style="background-color: var(--color-bg-secondary); padding: 40px; border-radius: 4px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.02); transition: transform 0.3s ease;">
          <h3 style="font-family: var(--font-logo); font-size: 20px; margin-bottom: 15px; color: var(--color-accent-gold); font-weight: 500;">Conscious Curation</h3>
          <p style="color: var(--color-text-secondary); font-size: 14px; line-height: 1.6; font-weight: 300;">By producing in limited capsules, we eliminate seasonal waste and focus entirely on sourcing certified organic cotton, recycled linen, and eco-tanned leathers.</p>
        </div>
        <div style="background-color: var(--color-bg-secondary); padding: 40px; border-radius: 4px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.02); transition: transform 0.3s ease;">
          <h3 style="font-family: var(--font-logo); font-size: 20px; margin-bottom: 15px; color: var(--color-accent-gold); font-weight: 500;">Architectural Lines</h3>
          <p style="color: var(--color-text-secondary); font-size: 14px; line-height: 1.6; font-weight: 300;">Our aesthetic draws inspiration from mid-century structural architecture, resulting in silhouettes that feel sculptural, clean, and effortlessly elegant.</p>
        </div>
      </div>
    </div>
  </main>"""

    about_content = about_before + about_body + shell_after
    about_content = about_content.replace("<title>Shopelar — Premium E-Commerce Navigation</title>", "<title>About Us — Shopelar</title>")
    about_content = about_content.replace('<meta name="description"\n    content="Experience Shopelar\'s premium, responsive, and elegant navigation bar, featuring modern design trends and smooth micro-interactions.">', '<meta name="description" content="Learn more about Shopelar - slow luxury, conscious curation, and artisanal heritage.">')

    with open(about_path, "w", encoding="utf-8") as f:
        f.write(about_content)

    # --- CONTACT PAGE ---
    contact_filename = "contact.html"
    contact_path = os.path.join(HTML_DIR, contact_filename)
    print("Generating contact.html...")

    contact_before = shell_before
    # Set Home inactive
    contact_before = contact_before.replace('class="nav-link active" id="link-home"', 'class="nav-link" id="link-home"')
    contact_before = contact_before.replace('class="mobile-nav-link active"', 'class="mobile-nav-link"')
    # Set Contact active
    contact_before = contact_before.replace('class="nav-link" id="link-contact"', 'class="nav-link active" id="link-contact"')
    contact_before = contact_before.replace('href="contact.html" class="mobile-nav-link"', 'href="contact.html" class="mobile-nav-link active"')

    contact_body = """  <main class="page-container">
    <header class="collection-hero">
      <div class="collection-hero-content">
        <span class="collection-badge">Concierge Service</span>
        <h1 class="collection-title">Contact Us</h1>
        <p class="collection-subtitle">We invite you to reach out for private styling appointments, showroom inquiries, or order support.</p>
      </div>
    </header>

    <section class="contact-section" id="contact" style="padding: 60px 40px 100px;">
      <div class="contact-container">
        <div class="contact-grid">
          <div class="contact-info">
            <span class="contact-badge">GET IN TOUCH</span>
            <h2 class="contact-title">Visit Our Atelier</h2>
            <p class="contact-desc">Have a question or want to schedule a private fitting? Reach out to us, and our advisors will respond within 24 hours.</p>
            
            <div class="contact-details">
              <div class="contact-detail-item">
                <div class="detail-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                </div>
                <div>
                  <h4 class="detail-label">Location</h4>
                  <p class="detail-value">Fifth Avenue 742, New York, NY</p>
                </div>
              </div>
              <div class="contact-detail-item">
                <div class="detail-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                </div>
                <div>
                  <h4 class="detail-label">Email</h4>
                  <p class="detail-value"><a href="mailto:concierge@shopelar.com">concierge@shopelar.com</a></p>
                </div>
              </div>
              <div class="contact-detail-item">
                <div class="detail-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                </div>
                <div>
                  <h4 class="detail-label">Phone</h4>
                  <p class="detail-value"><a href="tel:+18005557467">+1 (800) 555-SHOP</a></p>
                </div>
              </div>
            </div>
          </div>
          
          <div class="contact-form-wrapper">
            <form class="contact-form" id="contact-form-el">
              <div class="form-row">
                <div class="form-group">
                  <label for="form-name" class="form-label">Full Name</label>
                  <input type="text" id="form-name" placeholder="Enter your name" class="form-input" required>
                </div>
                <div class="form-group">
                  <label for="form-email" class="form-label">Email Address</label>
                  <input type="email" id="form-email" placeholder="Enter your email" class="form-input" required>
                </div>
              </div>
              <div class="form-group">
                <label for="form-subject" class="form-label">Subject</label>
                <input type="text" id="form-subject" placeholder="What is this regarding?" class="form-input" required>
              </div>
              <div class="form-group">
                <label for="form-message" class="form-label">Message</label>
                <textarea id="form-message" rows="5" placeholder="Write your message here..." class="form-input" required></textarea>
              </div>
              <button type="submit" class="form-submit-btn">
                <span>Send Message</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="submit-arrow"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </button>
              <div class="form-status-message" id="form-status"></div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>"""

    contact_content = contact_before + contact_body + shell_after
    contact_content = contact_content.replace("<title>Shopelar — Premium E-Commerce Navigation</title>", "<title>Contact Us — Shopelar</title>")
    contact_content = contact_content.replace('<meta name="description"\n    content="Experience Shopelar\'s premium, responsive, and elegant navigation bar, featuring modern design trends and smooth micro-interactions.">', '<meta name="description" content="Get in touch with Shopelar. Schedule a fitting, inquire about support, or visit our atelier showroom.">')

    with open(contact_path, "w", encoding="utf-8") as f:
        f.write(contact_content)

def sync_navbar_and_footer_in_static_files():
    # Read index.html
    with open(os.path.join(HTML_DIR, "index.html"), "r", encoding="utf-8") as f:
        index_content = f.read()

    # Extract header
    header_start = index_content.find('<header class="site-header"')
    header_end = index_content.find('</header>') + len('</header>')
    if header_start == -1 or header_end == -1:
        raise ValueError("Could not find header in index.html")
    header_html = index_content[header_start:header_end]

    # Extract mobile drawer
    drawer_start = index_content.find('<div id="mobile-drawer"')
    if drawer_start == -1:
        raise ValueError("Could not find mobile drawer in index.html")
    main_start = index_content.find('<main class="page-container">')
    if main_start == -1:
        main_start = index_content.find('<!-- Showcase / Scroll Spacing Container -->')
    if main_start == -1:
        raise ValueError("Could not find main container start in index.html")
    
    drawer_html = index_content[drawer_start:main_start].strip()
    if not drawer_html.endswith('</div>'):
        last_div = drawer_html.rfind('</div>')
        if last_div != -1:
            drawer_html = drawer_html[:last_div + len('</div>')]

    # Extract footer
    footer_start = index_content.find('<footer class="site-footer">')
    footer_end = index_content.find('</footer>') + len('</footer>')
    if footer_start == -1 or footer_end == -1:
        raise ValueError("Could not find footer in index.html")
    footer_html = index_content[footer_start:footer_end]

    static_files = [
        "new-arrivals.html",
        "best-sellers.html",
        "limited-edition.html",
        "clearance-sale.html"
    ]

    for sf in static_files:
        file_path = os.path.join(HTML_DIR, sf)
        if not os.path.exists(file_path):
            continue
        print(f"Syncing navbar and footer structure in {sf}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Replace header
        sf_header_start = content.find('<header class="site-header"')
        sf_header_end = content.find('</header>') + len('</header>')
        if sf_header_start != -1 and sf_header_end != -1:
            content = content[:sf_header_start] + header_html + content[sf_header_end:]

        # 2. Replace mobile drawer
        sf_drawer_start = content.find('<div id="mobile-drawer"')
        sf_main_start = content.find('<main class="page-container">')
        if sf_drawer_start != -1 and sf_main_start != -1:
            content = content[:sf_drawer_start] + drawer_html + "\n\n  " + content[sf_main_start:]

        # 3. Replace footer
        sf_footer_start = content.find('<footer class="site-footer">')
        sf_footer_end = content.find('</footer>') + len('</footer>')
        if sf_footer_start != -1 and sf_footer_end != -1:
            content = content[:sf_footer_start] + footer_html + content[sf_footer_end:]

        # Write back
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def generate_profile_pages():
    # Load index.html to extract the shell
    with open(os.path.join(HTML_DIR, "index.html"), "r", encoding="utf-8") as f:
        index_content = f.read()

    main_start_tag = '<main class="page-container">'
    main_end_tag = '</main>'
    
    start_idx = index_content.find(main_start_tag)
    end_idx = index_content.find(main_end_tag)
    
    if start_idx == -1 or end_idx == -1:
        raise ValueError("Could not find <main class='page-container'> structure in index.html")
        
    shell_before = index_content[:start_idx]
    shell_after = index_content[end_idx + len(main_end_tag):]

    # --- PROFILE PAGE ---
    profile_path = os.path.join(HTML_DIR, "profile.html")
    print("Generating profile.html...")
    p_before = shell_before.replace('class="nav-link active" id="link-home"', 'class="nav-link" id="link-home"')
    p_before = p_before.replace('class="mobile-nav-link active"', 'class="mobile-nav-link"')
    p_body = """  <main class="page-container">
    <header class="collection-hero">
      <div class="collection-hero-content">
        <span class="collection-badge">Personal Concierge</span>
        <h1 class="collection-title">My Profile</h1>
        <p class="collection-subtitle">Manage your personal details, sizing preferences, and security settings.</p>
      </div>
    </header>

    <div class="collection-main" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px;">
        <!-- Profile Form -->
        <div style="background-color: var(--color-bg-secondary); padding: 40px; border-radius: 4px;">
          <h2 style="font-family: var(--font-logo); font-size: 24px; margin-bottom: 24px; color: var(--color-text-primary); font-weight: 500;">Account Information</h2>
          <form class="contact-form" onsubmit="event.preventDefault(); alert('Profile updated successfully.');">
            <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
              <div class="form-group">
                <label class="form-label" style="display: block; margin-bottom: 8px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">First Name</label>
                <input type="text" value="Mahmoud" class="form-input" style="width: 100%; padding: 12px 16px; background-color: var(--color-white); border: 1px solid var(--color-border-light); font-size: 14px;" required>
              </div>
              <div class="form-group">
                <label class="form-label" style="display: block; margin-bottom: 8px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Last Name</label>
                <input type="text" value="Mohamed" class="form-input" style="width: 100%; padding: 12px 16px; background-color: var(--color-white); border: 1px solid var(--color-border-light); font-size: 14px;" required>
              </div>
            </div>
            <div class="form-group" style="margin-bottom: 20px;">
              <label class="form-label" style="display: block; margin-bottom: 8px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Email Address</label>
              <input type="email" value="mahmoud@example.com" class="form-input" style="width: 100%; padding: 12px 16px; background-color: var(--color-white); border: 1px solid var(--color-border-light); font-size: 14px;" required>
            </div>
            <div class="form-group" style="margin-bottom: 20px;">
              <label class="form-label" style="display: block; margin-bottom: 8px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Sizing Preference</label>
              <select class="form-input" style="width: 100%; padding: 12px 16px; background-color: var(--color-white); border: 1px solid var(--color-border-light); font-size: 14px;">
                <option value="tailored" selected>Tailored Fit (Recommended)</option>
                <option value="slim">Slim Fit</option>
                <option value="relaxed">Relaxed Fit</option>
              </select>
            </div>
            <button type="submit" class="form-submit-btn" style="padding: 14px 28px; background-color: var(--color-text-primary); color: var(--color-white); border: none; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer; display: flex; align-items: center; gap: 8px;">
              Save Changes
            </button>
          </form>
        </div>

        <!-- Sidebar Info -->
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <div style="background-color: var(--color-bg-secondary); padding: 30px; border-radius: 4px; text-align: center;">
            <div style="width: 80px; height: 80px; background-color: var(--color-border-light); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 40px; height: 40px; color: var(--color-text-secondary);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <h3 style="font-family: var(--font-logo); font-size: 18px; margin-bottom: 5px; color: var(--color-text-primary);">Mahmoud Mohamed</h3>
            <span style="font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--color-accent-gold); font-weight: 600;">Elite Member</span>
            <hr style="border: none; border-top: 1px solid var(--color-border-light); margin: 20px 0;">
            <div style="text-align: left; font-size: 13px; color: var(--color-text-secondary); display: flex; flex-direction: column; gap: 10px;">
              <div><strong>Status:</strong> Active</div>
              <div><strong>Client ID:</strong> #SHP-98412</div>
              <div><strong>Member Since:</strong> June 2026</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>"""
    p_content = p_before + p_body + shell_after
    p_content = p_content.replace("<title>Shopelar — Premium E-Commerce Navigation</title>", "<title>My Profile — Shopelar</title>")
    with open(profile_path, "w", encoding="utf-8") as f:
        f.write(p_content)

    # --- ORDERS PAGE ---
    orders_path = os.path.join(HTML_DIR, "orders.html")
    print("Generating orders.html...")
    o_before = shell_before.replace('class="nav-link active" id="link-home"', 'class="nav-link" id="link-home"')
    o_before = o_before.replace('class="mobile-nav-link active"', 'class="mobile-nav-link"')
    o_body = """  <main class="page-container">
    <header class="collection-hero">
      <div class="collection-hero-content">
        <span class="collection-badge">Order History</span>
        <h1 class="collection-title">My Orders</h1>
        <p class="collection-subtitle">Track your current concierge shipments and view past tailoring orders.</p>
      </div>
    </header>

    <div class="collection-main" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <div style="background-color: var(--color-bg-secondary); padding: 40px; border-radius: 4px; margin-bottom: 30px;">
        <h2 style="font-family: var(--font-logo); font-size: 20px; margin-bottom: 24px; color: var(--color-text-primary); font-weight: 500;">Active Shipments</h2>
        <div style="border: 1px solid var(--color-border-light); background-color: var(--color-white); padding: 24px; border-radius: 4px; display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: center;">
          <div>
            <div style="font-weight: 600; font-size: 15px; color: var(--color-text-primary); margin-bottom: 5px;">Order #SP-2026-8912</div>
            <div style="font-size: 13px; color: var(--color-text-secondary); margin-bottom: 10px;">Placed on June 15, 2026 — 1 Item</div>
            <div style="font-size: 14px; color: var(--color-text-primary);"><strong>Item:</strong> Loro Piana Tailored Linen Blazer ($890.00)</div>
          </div>
          <div style="text-align: right;">
            <span style="display: inline-block; padding: 6px 12px; background-color: rgba(212, 175, 55, 0.1); color: var(--color-accent-gold); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 20px; margin-bottom: 10px;">In Transit</span>
            <div style="font-size: 12px; color: var(--color-text-secondary);">Est. Delivery: June 22, 2026</div>
          </div>
        </div>
      </div>

      <div style="background-color: var(--color-bg-secondary); padding: 40px; border-radius: 4px;">
        <h2 style="font-family: var(--font-logo); font-size: 20px; margin-bottom: 24px; color: var(--color-text-primary); font-weight: 500;">Past Orders</h2>
        <div style="border: 1px solid var(--color-border-light); background-color: var(--color-white); padding: 24px; border-radius: 4px; display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: center;">
          <div>
            <div style="font-weight: 600; font-size: 15px; color: var(--color-text-primary); margin-bottom: 5px;">Order #SP-2026-7845</div>
            <div style="font-size: 13px; color: var(--color-text-secondary); margin-bottom: 10px;">Placed on May 10, 2026 — 1 Item</div>
            <div style="font-size: 14px; color: var(--color-text-primary);"><strong>Item:</strong> Gucci Artisanal Summer Loafers ($780.00)</div>
          </div>
          <div style="text-align: right;">
            <span style="display: inline-block; padding: 6px 12px; background-color: rgba(0, 128, 0, 0.08); color: green; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 20px; margin-bottom: 10px;">Delivered</span>
            <div style="font-size: 12px; color: var(--color-text-secondary);">Delivered on May 14, 2026</div>
          </div>
        </div>
      </div>
    </div>
  </main>"""
    o_content = o_before + o_body + shell_after
    o_content = o_content.replace("<title>Shopelar — Premium E-Commerce Navigation</title>", "<title>My Orders — Shopelar</title>")
    with open(orders_path, "w", encoding="utf-8") as f:
        f.write(o_content)

    # --- ADDRESSES PAGE ---
    addresses_path = os.path.join(HTML_DIR, "addresses.html")
    print("Generating addresses.html...")
    a_before = shell_before.replace('class="nav-link active" id="link-home"', 'class="nav-link" id="link-home"')
    a_before = a_before.replace('class="mobile-nav-link active"', 'class="mobile-nav-link"')
    a_body = """  <main class="page-container">
    <header class="collection-hero">
      <div class="collection-hero-content">
        <span class="collection-badge">Address Book</span>
        <h1 class="collection-title">Saved Addresses</h1>
        <p class="collection-subtitle">Manage your default billing and shipping destinations for express concierge styling checkouts.</p>
      </div>
    </header>

    <div class="collection-main" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        <!-- Primary Address -->
        <div style="background-color: var(--color-bg-secondary); padding: 30px; border-radius: 4px; border: 1px solid var(--color-accent-gold); position: relative;">
          <span style="position: absolute; top: 20px; right: 20px; font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent-gold);">Default</span>
          <h3 style="font-family: var(--font-logo); font-size: 18px; margin-bottom: 15px; color: var(--color-text-primary); font-weight: 500;">Shipping Address</h3>
          <p style="color: var(--color-text-secondary); font-size: 14px; line-height: 1.8; margin-bottom: 20px; font-weight: 300;">
            <strong>Mahmoud Mohamed</strong><br>
            Fifth Avenue 742<br>
            New York, NY 10019<br>
            United States<br>
            Phone: +1 (800) 555-7467
          </p>
          <div style="display: flex; gap: 15px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">
            <a href="#" style="color: var(--color-text-primary);">Edit</a>
            <span style="color: var(--color-border-light);">|</span>
            <a href="#" style="color: var(--color-text-secondary);">Remove</a>
          </div>
        </div>

        <!-- Secondary Address -->
        <div style="background-color: var(--color-bg-secondary); padding: 30px; border-radius: 4px; border: 1px solid var(--color-border-light);">
          <h3 style="font-family: var(--font-logo); font-size: 18px; margin-bottom: 15px; color: var(--color-text-primary); font-weight: 500;">Billing Address</h3>
          <p style="color: var(--color-text-secondary); font-size: 14px; line-height: 1.8; margin-bottom: 20px; font-weight: 300;">
            <strong>Mahmoud Mohamed</strong><br>
            Sunset Blvd 9021<br>
            Los Angeles, CA 90210<br>
            United States<br>
            Phone: +1 (800) 555-7467
          </p>
          <div style="display: flex; gap: 15px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">
            <a href="#" style="color: var(--color-text-primary);">Edit</a>
            <span style="color: var(--color-border-light);">|</span>
            <a href="#" style="color: var(--color-text-secondary);">Remove</a>
          </div>
        </div>
      </div>
    </div>
  </main>"""
    a_content = a_before + a_body + shell_after
    a_content = a_content.replace("<title>Shopelar — Premium E-Commerce Navigation</title>", "<title>Saved Addresses — Shopelar</title>")
    with open(addresses_path, "w", encoding="utf-8") as f:
        f.write(a_content)

def main():
    existing_files = [
        "index.html",
        "new-arrivals.html",
        "best-sellers.html",
        "limited-edition.html",
        "clearance-sale.html",
        
        # Generated category pages (we update them as well to maintain correct links everywhere)
        "the-linen-look.html",
        "warm-palette-suits.html",
        "monochrome-essentials.html",
        "minimalist-leather.html",
        "summer-knitwear.html",
        "tailored-coats.html",
        "silk-shirts-and-tops.html",
        "structured-trousers.html",
        "summer-dresses.html",
        "leather-handbags.html",
        "overcoats-and-jackets.html",
        "fine-knit-sweaters.html",
        "tailored-shirts.html",
        "casual-chinos.html",
        "chrono-watches.html",
        "the-neutral-tone.html",
        
        # About and Contact
        "about.html",
        "contact.html",
        
        # Profile subpages
        "profile.html",
        "orders.html",
        "addresses.html"
    ]
    
    # 1. Update index.html first to ensure its links are clean
    update_menu_links(os.path.join(HTML_DIR, "index.html"))
    
    # 2. Sync layout elements structurally in static files from index.html
    sync_navbar_and_footer_in_static_files()
    
    # 3. Update existing files to link correctly
    for ef in existing_files:
        file_path = os.path.join(HTML_DIR, ef)
        if os.path.exists(file_path):
            update_menu_links(file_path)
            
    # 4. Generate the category pages (including the-neutral-tone)
    generate_category_pages()
    
    # 5. Generate About & Contact pages
    generate_about_and_contact_pages()
    
    # 6. Generate Profile dropdown pages
    generate_profile_pages()
    
    print("Successfully generated and updated all category pages, about, contact, and profile pages!")

if __name__ == "__main__":
    main()
