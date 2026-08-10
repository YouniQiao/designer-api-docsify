# AudioRecordingManager

提供录像策略管理，包括协同录音和录制控制能力。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-interface AudioRecordingManager--><!--Device-audio-interface AudioRecordingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## offSystemRecordControllerEnabledChange

```TypeScript
offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void
```

取消订阅系统录像控制器面板启用状态更改事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRecordingManager-offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void--><!--Device-AudioRecordingManager-offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemRecordControllerChangeInfo&gt; | No | 订阅中使用的回调 取消订阅功能。如果不使用此参数，则当前订阅的所有回调 之前的流程将被取消订阅 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800301 | Audio service error occurs like service died. |

## onSystemRecordControllerEnabledChange

```TypeScript
onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void
```

订阅系统录像控制器面板使能状态变化事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRecordingManager-onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void--><!--Device-AudioRecordingManager-onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemRecordControllerChangeInfo&gt; | Yes | 用于监听的回调 系统记录控制器面板启用状态更改事件 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800102 | Memory allocation failed. |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800301 | Audio service error occurs like service died. |

