# getAllMainWindowInfo

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getAllMainWindowInfo

```TypeScript
function getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>
```

Obtains the information about all main windows. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.CUSTOM_SCREEN_CAPTURE

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MainWindowInfo](arkts-arkui-window-mainwindowinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
