# saveHdrPicture (System API)

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## saveHdrPicture

```TypeScript
function saveHdrPicture(options?: HdrScreenshotOptions): Promise<Array<image.PixelMap>>
```

Obtains a screenshot. This API uses a promise to return the result. SDR stands for Standard Dynamic Range, and HDR stands for High Dynamic Range.  
- If the screen contains HDR resources (even if they are partially obscured), this API returns an array with both  
SDR and HDR PixelMaps, regardless of whether HDR is enabled.  
- If there are no HDR resources, it returns an array with a single SDR PixelMap. Unlike the  
[save](arkts-arkui-screenshot-save-f-sys.md) API, which returns a single SDR PixelMap, this API always returns an array. Additionally, this API does not support cropping, stretching, or rotating features available in the [save](arkts-arkui-screenshot-save-f-sys.md) API.

**Since:** 20

**Required permissions:** 
- API version 22+: ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 20 - 21: ohos.permission.CAPTURE_SCREEN

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [HdrScreenshotOptions](arkts-arkui-screenshot-hdrscreenshotoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;image.PixelMap & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [1400004](../errorcode-display.md#1400004-parameter-error) |
