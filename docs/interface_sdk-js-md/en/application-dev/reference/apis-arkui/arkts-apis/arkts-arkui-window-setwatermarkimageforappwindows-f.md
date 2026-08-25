# setWatermarkImageForAppWindows

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## setWatermarkImageForAppWindows

```TypeScript
function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>
```

Sets a watermark image for windows in the current application process. This API uses a promise to return the result. This API must be called after [loadContent()](arkts-arkui-window-window-i.md#loadcontent) or [setUIContent()](arkts-arkui-window-window-i.md#setuicontent) takes effect.

**Since:** 21

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelMap | image.PixelMap \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
