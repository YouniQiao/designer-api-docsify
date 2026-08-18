# getBrightnessInfo

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## getBrightnessInfo

```TypeScript
function getBrightnessInfo(displayId: long): BrightnessInfo
```

Obtains the screen brightness information of a display. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the returned [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md#brightnessinfo) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-display-function getBrightnessInfo(displayId: long): BrightnessInfo--><!--Device-display-function getBrightnessInfo(displayId: long): BrightnessInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | long | Yes | Display ID. The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) | Screen brightness information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function getBrightnessInfo can not work correctly due to limited device capabilities. |
| [1400004](../errorcode-display.md#1400004-parameter-error) | Parameter error. Possible cause: 1. Invalid parameter range. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

