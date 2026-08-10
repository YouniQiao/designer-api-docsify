# sendPrivateCommand (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from 'kits/@kit.IMEKit';
```

## sendPrivateCommand

```TypeScript
function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

发送私有命令。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>--><!--Device-inputMethodSystemPanelManager-function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| commandData | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, CommandDataType&gt; | Yes | 将要发送的命令数据。最大大小32KB。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800026 | input method system panel error. Possible causes: 1. the system panel not connected. 2. ipc failed due to the large amount of data transferred or other reasons. 3. the caller is not system panel. |
| 202 | not system application. |

