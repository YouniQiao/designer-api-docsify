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

## enableSystemRecordController

```TypeScript
enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise<void>
```

启用或禁用系统录像控制器面板。应用程序在启动录制码流之前，可以调用此接口拉起录制控制器面板。允许用户完成录音设备或音效参数的选择。然后可以启动录音服务，避免在记录过程。应用程序必须在前台才能启用面板；启用操作不生效如果应用程序在后台。禁用面板不受应用程序的限制前台或后台状态。该接口使用promise返回结果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRecordingManager-enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise<void>--><!--Device-AudioRecordingManager-enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| show | boolean | Yes | 一个布尔值，指示是显示（true）还是隐藏(false) 系统记录控制器面板 |
| config | [SystemRecordControllerConfig](arkts-audio-audio-systemrecordcontrollerconfig-i.md) | Yes | 系统录像控制器面板配置 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 不会返回任何值的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio service error occurs like service died. |

