# badge

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BadgeParam](arkts-na-badge-badgeparam-i.md) | Provides basic parameters for creating a badge. |
| [BadgeParamWithNumber](arkts-na-badge-badgeparamwithnumber-i.md) | Inherits from BadgeParam and has all attributes of BadgeParam. |
| [BadgeParamWithString](arkts-na-badge-badgeparamwithstring-i.md) | Inherits from BadgeParam and has all attributes of BadgeParam. |
| [BadgeStyle](arkts-na-badge-badgestyle-i.md) | Describes the badge style. It includes the font color, font size, badge color, badge size, etc. > **NOTE：**> > - When **borderWidth** is set to a value greater than 0 and **borderColor** is different from **badgeColor**, the > badge is drawn before the border. Edge pixels are anti-aliased, which produces semi-transparent pixels. This causes > the border in **badgeColor** to become visible at the four corners. To implement related scenarios, it is > recommended that you use the Text component with its > outline attribute instead of the **Badge** component. |

### Enums

| Name | Description |
| --- | --- |
| [BadgePosition](arkts-na-badge-badgeposition-e.md) | Defines the badge position property. |

