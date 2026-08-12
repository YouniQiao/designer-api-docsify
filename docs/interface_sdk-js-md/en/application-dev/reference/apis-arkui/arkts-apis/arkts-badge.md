# badge

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BadgeParam](arkts-arkui-badge-badgeparam-i.md) | Provides basic parameters for creating a badge. |
| [BadgeParamWithNumber](arkts-arkui-badge-badgeparamwithnumber-i.md) | Inherits from BadgeParam and has all attributes of BadgeParam. |
| [BadgeParamWithString](arkts-arkui-badge-badgeparamwithstring-i.md) | Inherits from BadgeParam and has all attributes of BadgeParam. |
| [BadgeStyle](arkts-arkui-badge-badgestyle-i.md) | Describes the badge style. It includes the font color, font size, badge color, badge size, etc.  > **NOTE：** >  > - When **borderWidth** is set to a value greater than 0 and **borderColor** is different from **badgeColor**, the > badge is drawn before the border. Edge pixels are anti-aliased, which produces semi-transparent pixels. This causes > the border in **badgeColor** to become visible at the four corners. To implement related scenarios, it is > recommended that you use the [Text](text) component with its > [outline](CommonMethod#outline(value: OutlineOptions)) attribute instead of the **Badge** component. |

### Enums

| Name | Description |
| --- | --- |
| [BadgePosition](arkts-arkui-badge-badgeposition-e.md) | Defines the badge position property. |

