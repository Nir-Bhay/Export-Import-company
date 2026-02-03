# Naaz Scrap - Industrial Excellence

A professional corporate website for **Naaz Scrap** (formerly GM International/Enterprise), a leading metal scrap trading company offering global import and export services. This single-page application (SPA) serves as a digital portfolio tailored to showcase the company's industrial capabilities, product range, and international reach.

## 📋 Project Overview

This project is a static, responsive single-page website designed to provide a seamless user experience for clients and partners in the metal trading industry. It features a modern design, interactive elements, and a clean architecture that allows for easy content updates and maintenance.

**Purpose**: To establish a strong digital presence for Naaz Scrap, facilitating global trade connections and showcasing operational excellence.

## ✨ Key Features

-   **Single Page Application (SPA) Architecture**:  
    Utilizes lightweight vanilla JavaScript for smooth navigation between sections (Home, About, Products, Services, Contact) without page reloads.
-   **Responsive & Modern Design**:  
    Built with **Tailwind CSS** to ensure a fully responsive experience across mobile, tablet, and desktop devices.
-   **Interactive Gallery**:  
    Features a custom modal lightbox with keyboard navigation for viewing facility and operational images.
-   **Dynamic Content Sections**:  
    Includes an FAQ accordion, tabbed interfaces for services, and hash-based routing/deep-linking support.
-   **Professional Branding**:  
    Consistent use of typography (Inter & Poppins) and color schemes (Navy, Gold, Green) to reflect industrial professionalism.

## 🛠️ Tech Stack

-   **Core**: HTML5, CSS3, JavaScript (ES6+)
-   **Styling**: [Tailwind CSS](https://tailwindcss.com/) (via CDN), Custom CSS Variables
-   **Icons**: [Font Awesome](https://fontawesome.com/)
-   **Fonts**: Google Fonts (Inter, Poppins)

## 📂 Folder Structure

```
/
├── assets/
│   ├── images/           # Core project images (gallery, banners, etc.)
│   └── update images/    # Assets for recent branding updates
├── main/
│   └── logo.png          # Primary brand logo
├── index.html            # Main entry file containing structure and logic
└── README.md             # Project documentation
```

## 🚀 Installation & Setup

Since this is a static website, no complex backend or build process is required.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Nir-Bhay/Export-Import-company.git
    cd Export-Import-company
    ```

2.  **Run Locally**:
    *   **Option A (VS Code)**: Install the "Live Server" extension, right-click `index.html`, and select "Open with Live Server".
    *   **Option B (Python)**:
        ```bash
        # Python 3
        python3 -m http.server
        # Then open http://localhost:8000 in your browser
        ```
    *   **Option C (Direct)**: Simply double-click `index.html` to open it in your default web browser (note: some modern browser security policies might restrict local file access for certain features).

## 📖 Usage

-   **Navigation**: Use the top navigation bar to jump between different business sections.
-   **Gallery**: Click on any image in the "Our Operations & Facilities" section to open the full-screen viewer. Use arrow keys or on-screen buttons to navigate.
-   **Contact**: Scroll to the dedicated Contact section or use the footer for quick access to email, phone, and location details.

## 🔄 Recent Updates

-   **Rebranding**: Successfully transitioned the digital identity from **GM International** to **Naaz Scrap**, updating all relevant logos, text references, and color accents to align with the new brand strategy.
-   **Visual Enhancements**: Improved the mobile menu interaction and refined the "Export Services" maps and flow animations.

## 🏗️ Architecture

The application follows a simple **Client-Side Rendering** model:

-   **Frontend**: All content resides within `index.html`. JavaScript controls the visibility of different "views" (`#home-view`, `#about-view`, etc.) based on user interaction.
-   **Logic**: A custom `navigateTo()` function handles view switching and URL hash updates to support browser back/forward navigation.
-   **Styling**: Tailwind utility classes handle layout and responsiveness, while a global `<style>` block manages custom animations and component-specific overrides.

## ⚙️ Configuration

-   **Environment**: No `.env` files are required as this is a client-side static site.
-   **External Dependencies**: The project relies on CDNs for Tailwind CSS and Font Awesome. Ensure you have an active internet connection for these styles to load correctly during development.

## 🤝 Contribution

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## 📞 Contact & Credits

**Developer**: Nirbhay Hiwse  
[LinkedIn Placeholder] | [Portfolio Placeholder]

---
© 2026 Naaz Scrap. All Rights Reserved.  
*Made with ❤️ in India 🇮🇳*
