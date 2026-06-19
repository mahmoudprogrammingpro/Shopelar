/* ==========================================================================
   Shopelar Premium E-Commerce Interactivity Script
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  // 1. Desktop Expanding Search Bar Interaction
  const searchContainer = document.getElementById('nav-search-container');
  const searchToggle = document.getElementById('nav-search-toggle');
  const searchInput = document.getElementById('nav-search-input');

  if (searchToggle && searchContainer && searchInput) {
    searchToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      searchContainer.classList.toggle('active');

      if (searchContainer.classList.contains('active')) {
        searchInput.focus();
      }
    });

    // Close search bar when clicking anywhere outside
    document.addEventListener('click', (e) => {
      if (!searchContainer.contains(e.target)) {
        searchContainer.classList.remove('active');
      }
    });

    // Close search bar on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        searchContainer.classList.remove('active');
        searchInput.blur();
      }
    });
  }

  // 2. Mobile Drawer Accordion Menu Toggles
  const collapsibleButtons = document.querySelectorAll('.mobile-collapsible-btn');

  collapsibleButtons.forEach(button => {
    button.addEventListener('click', () => {
      const parentLi = button.parentElement;

      // Close other mobile collapsibles (Accordion behavior)
      document.querySelectorAll('.mobile-collapsible').forEach(item => {
        if (item !== parentLi) {
          item.classList.remove('active');
        }
      });

      // Toggle current collapsible
      parentLi.classList.toggle('active');
    });
  });

  // 3. Cart Simulation & Badge Micro-interactions
  const simCartBtn = document.getElementById('sim-add-cart');
  const cartCountBadge = document.getElementById('cart-count');
  const productAddCartButtons = document.querySelectorAll('.product-add-cart-btn');
  let cartCount = 0;

  const incrementCart = () => {
    cartCount += 1;
    cartCountBadge.textContent = cartCount;

    // Apply pop pulse micro-animation
    cartCountBadge.classList.add('pulse');

    // Remove class after animation cycles
    setTimeout(() => {
      cartCountBadge.classList.remove('pulse');
    }, 300);
  };

  if (simCartBtn && cartCountBadge) {
    simCartBtn.addEventListener('click', incrementCart);
  }

  if (cartCountBadge) {
    productAddCartButtons.forEach(btn => {
      btn.addEventListener('click', incrementCart);
    });
  }

  // 4. Scroll-Driven Animation Fallback for Non-Supporting Browsers (e.g. Firefox)
  const isScrollDrivenSupported = CSS.supports('(animation-timeline: scroll()) and (animation-range: 0% 100%)');

  if (!isScrollDrivenSupported) {
    const header = document.getElementById('main-header');

    if (header) {
      const initialHeight = 88;
      const finalHeight = 64;
      const scrollThreshold = 120; // Scroll distance matching animation-range

      const handleScrollFallback = () => {
        const scrollY = window.scrollY;
        const ratio = Math.min(1, scrollY / scrollThreshold);

        // Interpolate size
        const currentHeight = initialHeight - (initialHeight - finalHeight) * ratio;
        header.style.height = `${currentHeight}px`;

        if (ratio > 0.05) {
          header.style.backgroundColor = `rgba(255, 255, 255, ${0.95 + 0.03 * ratio})`;
          header.style.boxShadow = `0 4px 30px rgba(0, 0, 0, ${0.04 * ratio})`;
          header.style.borderBottomColor = `rgba(228, 228, 231, ${1 - ratio * 0.8})`;
        } else {
          header.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
          header.style.boxShadow = 'none';
          header.style.borderBottomColor = '#e4e4e7';
        }
      };

      // Run immediately in case user loads page scrolled down
      handleScrollFallback();

      // Bind to scroll listener
      window.addEventListener('scroll', handleScrollFallback, { passive: true });
    }
  }

  // 5. Contact Form Interaction
  const contactForm = document.getElementById('contact-form-el');
  const contactStatus = document.getElementById('form-status');

  if (contactForm && contactStatus) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const submitBtn = contactForm.querySelector('.form-submit-btn');
      const submitText = submitBtn.querySelector('span');
      const originalText = submitText.textContent;
      
      // Loading state
      submitBtn.style.pointerEvents = 'none';
      submitText.textContent = 'Sending...';
      
      // Simulate API call
      setTimeout(() => {
        // Clear inputs
        contactForm.reset();
        
        // Show success state
        submitBtn.style.pointerEvents = 'auto';
        submitText.textContent = originalText;
        
        contactStatus.textContent = 'Thank you! Your message has been sent successfully. Our consultants will reach out to you within 24 hours.';
        contactStatus.className = 'form-status-message visible success';
        
        // Hide status after 6 seconds
        setTimeout(() => {
          contactStatus.classList.remove('visible');
        }, 6000);
      }, 1500);
    });
  }

  // 6. Newsletter Subscription Interaction
  const newsletterForm = document.getElementById('newsletter-form-el');
  const newsletterStatus = document.getElementById('newsletter-status-el');

  if (newsletterForm && newsletterStatus) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const emailInput = newsletterForm.querySelector('.newsletter-input');
      const submitBtn = newsletterForm.querySelector('.newsletter-btn');
      
      // Loading state
      submitBtn.style.pointerEvents = 'none';
      submitBtn.style.opacity = '0.5';
      
      // Simulate API call
      setTimeout(() => {
        emailInput.value = '';
        submitBtn.style.pointerEvents = 'auto';
        submitBtn.style.opacity = '1';
        
        newsletterStatus.textContent = 'Welcome to the Club! Check your inbox for your confirmation details.';
        newsletterStatus.style.color = 'var(--color-accent-gold)';
        newsletterStatus.style.opacity = '1';
        
        // Hide status after 5 seconds
        setTimeout(() => {
          newsletterStatus.style.opacity = '0';
        }, 5000);
      }, 1200);
    });
  }
});
