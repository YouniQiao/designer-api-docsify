# AudioRecordingManager

Provides recording strategy management, including collaborative recording and recording control capabilities.

**Since:** 26.0.0

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

Unsubscribes from the system recording controller panel enabled state change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRecordingManager-offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void--><!--Device-AudioRecordingManager-offSystemRecordControllerEnabledChange(callback?: Callback<SystemRecordControllerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemRecordControllerChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## onSystemRecordControllerEnabledChange

```TypeScript
onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void
```

Subscribes to the system recording controller panel enabled state change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRecordingManager-onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void--><!--Device-AudioRecordingManager-onSystemRecordControllerEnabledChange(callback: Callback<SystemRecordControllerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemRecordControllerChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800102](../errorcode-audio.md#6800102-memory-allocation-failure) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
