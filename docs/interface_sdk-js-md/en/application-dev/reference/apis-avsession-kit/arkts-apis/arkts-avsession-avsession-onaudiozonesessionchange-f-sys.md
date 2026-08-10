# onAudioZoneSessionChange (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## onAudioZoneSessionChange

```TypeScript
function onAudioZoneSessionChange(userId: int, callback: Callback<AVSessionDescriptor>): void
```

注册音区会话变化回调

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function onAudioZoneSessionChange(userId: int, callback: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function onAudioZoneSessionChange(userId: int, callback: Callback<AVSessionDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 当前userId最终归属的音区 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVSessionDescriptor&gt; | Yes | 返回的会话列表 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 202 | Not System App. |

