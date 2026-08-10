# AudioRecordingManager

提供录像策略管理，包括协同录音和录制控制能力。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-audio-interface AudioRecordingManager--><!--Device-audio-interface AudioRecordingManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## offSystemRecordControllerEnabledChange

```TypeScript
offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void
```

取消订阅系统录像控制器面板启用状态更改事件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRecordingManager-offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void--><!--Device-AudioRecordingManager-offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemRecordControllerChangeInfo&gt; | 否 | 订阅中使用的回调 取消订阅功能。如果不使用此参数，则当前订阅的所有回调 之前的流程将被取消订阅 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800301 | Audio service error occurs like service died. |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

audioRecordingManager.offSystemRecordControllerEnabledChange();
```

## onSystemRecordControllerEnabledChange

```TypeScript
onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void
```

订阅系统录像控制器面板使能状态变化事件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRecordingManager-onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void--><!--Device-AudioRecordingManager-onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemRecordControllerChangeInfo&gt; | 是 | 用于监听的回调 系统记录控制器面板启用状态更改事件 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 6800102 | Memory allocation failed. |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800301 | Audio service error occurs like service died. |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

audioRecordingManager.onSystemRecordControllerEnabledChange((changeInfo: audio.SystemRecordControllerChangeInfo) => {
  console.info(`System record controller enabled state changed: ${changeInfo.enabled}, uid: ${changeInfo.uid}, sourceType: ${changeInfo.sourceType}`);
});
```

