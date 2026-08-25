# getSnapshot (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getSnapshot

```TypeScript
function getSnapshot(windowId: number): Promise<image.PixelMap>
```

Obtains a snapshot of the same size as the specified window. This API uses a promise to return the result. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](arkts-arkui-window-window-i.md#setwindowprivacymode)), taking a screenshot will result in a blank screen.

**Since:** 12

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
