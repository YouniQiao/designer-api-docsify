# offAudioZoneSessionChange (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## offAudioZoneSessionChange

```TypeScript
function offAudioZoneSessionChange(userId: int, callback?: Callback<AVSessionDescriptor>): void
```

取消注册音区对应的会话变化监听

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function offAudioZoneSessionChange(userId: int, callback?: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function offAudioZoneSessionChange(userId: int, callback?: Callback<AVSessionDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用户id，归属某个音区 &lt;br&gt;用户userId 所归属的音区 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVSessionDescriptor&gt; | No | 返回对应音区的会话列表 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 202 | Not System App. |

