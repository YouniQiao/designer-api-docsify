# getVisibleWindowInfo

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getVisibleWindowInfo

```TypeScript
function getVisibleWindowInfo(): Promise<Array<WindowInfo>>
```

Obtains information about visible main windows on the current screen. Visible main windows are main windows that are not returned to the background. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** 
- API version 18+: ohos.permission.VISIBLE_WINDOW_INFO

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;WindowInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
