# sendSystemCommonCommand (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## sendSystemCommonCommand

```TypeScript
function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>
```

发送通用事件命令

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>--><!--Device-avSession-function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | 通用的控制命令 |
| args | [ExtraInfo](arkts-avsession-avsession-extrainfo-t.md) | Yes | 事件参数 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | callback info for sync command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 201 | permission denied |
| 202 | Not System App. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

