# onSystemPrivateCommand (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from 'kits/@kit.IMEKit';
```

## onSystemPrivateCommand

```TypeScript
function onSystemPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void
```

订阅输入法应用发送私有数据命令的事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function onSystemPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void--><!--Device-inputMethodSystemPanelManager-function onSystemPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | Yes | 当输入法应用发送私有数据命令时触发的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

