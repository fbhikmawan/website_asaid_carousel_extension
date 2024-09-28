# ASAid Carousel Extension

## Overview

ASAid Carousel Extension is an Odoo 17 module that enhances the functionality of website Carousels. It adds various additional custom options or features for the Carousel block, allowing for more flexible control over carousel display and behavior.

## Features

- Adds customizable height options to the Carousel block settings.
- Provides additional style and transition options for Carousel items.
- Seamlessly integrates with Odoo's website builder for easy customization.

## Installation

1. Clone this repository into your Odoo addons directory:
   ```
   git clone https://github.com/fbhikmawan/website_asaid_carousel_extension.git
   ```
2. Update your Odoo addons path to include this module.
3. Restart your Odoo server.
4. Go to Apps and search for "ASAid Carousel Extension".
5. Click "Install" to activate the module.

## Usage

After installation:

1. Go to Website > Edit Website.
2. Add or edit a Carousel block.
3. In the Carousel options, you'll find new height and style options.
4. Customize the Carousel to fit your design needs.

## Configuration

No additional configuration is needed. The module extends existing carousel functionality without requiring separate setup.

## Dependencies

This module depends on:
- `web_editor`
- `website`

Ensure these modules are available in your Odoo installation.

## Technical Details

- The module extends the `ir.ui.view` model to add new options for the Carousel block.
- It modifies the carousel template to include additional customization options.
- Custom JavaScript (if any) handles the display logic for the new options.

## Contributing

Contributions to improve ASAid Carousel Extension are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to your branch.
5. Create a new Pull Request.

## Support

For support, please contact ASAid Group Investment at support@asaidgroup.com or visit our website at https://www.asaidgroup.com.

## License

This module is licensed under the LGPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Authors

- ASAid Group Investment
- Fatchul Bari Hikmawan

---

For more information about Odoo development, visit the [official Odoo documentation](https://www.odoo.com/documentation/17.0/).
