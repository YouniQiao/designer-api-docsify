# connectSystemChannel (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from 'kits/@kit.IMEKit';
```

## connectSystemChannel

```TypeScript
function connectSystemChannel(): Promise<void>
```

连接面板和输入法之间的系统通道。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function connectSystemChannel(): Promise<void>--><!--Device-inputMethodSystemPanelManager-function connectSystemChannel(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | permissions check fails. |
| 12800026 | input method system panel error. Possible causes: 1. the system panel not connected. 2. ipc failed due to the large amount of data transferred or other reasons. 3. the caller is not system panel. |
| 202 | not system application. |
| 12800008 | input method manager service error. Possible causes: a system error, such as null pointer, IPC exception. |

