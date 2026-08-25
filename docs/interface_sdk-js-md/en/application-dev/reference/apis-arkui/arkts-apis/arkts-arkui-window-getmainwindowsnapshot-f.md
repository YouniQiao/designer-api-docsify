# getMainWindowSnapshot

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getMainWindowSnapshot

```TypeScript
function getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration):
    Promise<Array<image.PixelMap | undefined>>
```

Obtains the screenshots of one or more main windows specified by **windowId**. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.CUSTOM_SCREEN_CAPTURE

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | Array & lt;number & gt; | Yes |
| config | [WindowSnapshotConfiguration](arkts-arkui-window-windowsnapshotconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;image.PixelMap \ | undefined & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
