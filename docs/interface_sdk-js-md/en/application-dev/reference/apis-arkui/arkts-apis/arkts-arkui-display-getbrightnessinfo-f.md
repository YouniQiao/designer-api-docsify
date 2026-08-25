# getBrightnessInfo

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getBrightnessInfo

```TypeScript
function getBrightnessInfo(displayId: number): BrightnessInfo
```

Obtains the screen brightness information of a display. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the returned [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [1400004](../errorcode-display.md#1400004-parameter-error) |
