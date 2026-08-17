# imageCommon

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ImageAnalyzerController](arkts-na-imagecommon-imageanalyzercontroller-c.md) | Image AI analysis controller. You can bind this object to a supported component and call supported methods through the controller. |

### Interfaces

| Name | Description |
| --- | --- |
| [ImageAIOptions](arkts-na-imagecommon-imageaioptions-i.md) | Image AI analysis options. > **Description:** > > The types parameter in this feature has higher priority than the types parameter in > [ImageAnalyzerConfig](arkts-na-imagecommon-imageanalyzerconfig-i.md#imageanalyzerconfig). When both are set, > the value set in this feature takes precedence. > > This feature depends on device capability and needs to be used with > the enableAnalyzer interface > of the corresponding component (for example, Image component). |
| [ImageAnalyzerConfig](arkts-na-imagecommon-imageanalyzerconfig-i.md) | Image AI analysis configuration item. |

### Enums

| Name | Description |
| --- | --- |
| [ImageAnalyzerType](arkts-na-imagecommon-imageanalyzertype-e.md) | Image AI analysis type. When not set, subject recognition and text recognition are enabled by default. |

