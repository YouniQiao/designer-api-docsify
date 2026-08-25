# capture

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## capture

```TypeScript
function capture(options?: CaptureOption): Promise<image.PixelMap>
```

Takes a screenshot of the entire screen. This API uses a promise to return the result.This API allows you to take screenshots of different screens by setting various **displayId** values, but only full -screen captures are supported. The [pick](arkts-arkui-screenshot-pick-f.md) API allows you to take screenshots of a specified region.

**Since:** 14

**Required permissions:** 
- API version 22+: ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 14 - 21: ohos.permission.CUSTOM_SCREEN_CAPTURE

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CaptureOption](arkts-arkui-screenshot-captureoption-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
