# AudioRecordingManager

Provides recording strategy management, including collaborative recording and recording control capabilities.

**Since:** 26.0.0

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

Enables or disables the system recording controller panel.The application can call this API to pull up the recording controller panel before starting the recording stream,allowing the user to finish selecting the recording device or audio effect parameters.The recording service can then be started to avoid inconsistent audio effects caused by switching during the recording process.The application must be in the foreground to enable the panel; the enable operation does not take effect if the application is in the background. Disabling the panel is not restricted by the application's foreground or background status.The API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRecordingManager-enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise<void>--><!--Device-AudioRecordingManager-enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| show | boolean | Yes |
| config | [SystemRecordControllerConfig](arkts-audio-audio-systemrecordcontrollerconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
