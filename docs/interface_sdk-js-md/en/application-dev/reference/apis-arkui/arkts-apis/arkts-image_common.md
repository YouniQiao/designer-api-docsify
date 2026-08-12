# image_common

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ImageAnalyzerController](arkts-arkui-imageanalyzercontroller-c.md) | Implements an AI image analysis controller, which provides control for image analysis features when bound to supported components. |

### Interfaces

| Name | Description |
| --- | --- |
| [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | Provides the AI image analysis options.  > **NOTE：** >  > The **types** parameter of this API has a higher priority than that of > [ImageAnalyzerConfig](arkts-arkui-imageanalyzerconfig-i.md#ImageAnalyzerConfig). This means that, if both parameters are set, the value set by > this API takes precedence. >  > This API depends on device capabilities and must be used together with the > [enableAnalyzer](ImageAttribute#enableAnalyzer) API of the corresponding component (for example, the > [Image](./image) component). |
| [ImageAnalyzerConfig](arkts-arkui-imageanalyzerconfig-i.md) | Provides AI image analyzer configuration. |

### Enums

| Name | Description |
| --- | --- |
| [ImageAnalyzerType](arkts-arkui-imageanalyzertype-e.md) | Defines the AI image analysis type. If it is not set, subject recognition and text recognition are enabled by default. |

