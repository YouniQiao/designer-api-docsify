# BackgroundTaskMode

Main type of a continuous task. It is usually used together with the subtype [BackgroundTaskSubmode]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. For details, see the mapping table. The two types are newly added in API version 21 for [requesting]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and [updating]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ continuous tasks. When the main type of the continuous task is **MODE\_SPECIAL\_SCENARIO\_PROCESSING**, or that of a non-PC/2-in-1 device is **MODE\_TASK\_KEEPING**, you need to request the ACL permission \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ before calling APIs related to continuous tasks. In other scenarios, this permission is not required.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-backgroundTaskManager-export enum BackgroundTaskMode--><!--Device-backgroundTaskManager-export enum BackgroundTaskMode-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_DATA_TRANSFER

```TypeScript
MODE_DATA_TRANSFER = 1
```

Data transfer. Use scenario: upload and download in non-hosting mode, for example, uploading or downloading data in the background of a browser. **NOTE** 1. During data transfer, the application needs to update the progress. If the progress is not updated for more than 10 minutes, the continuous task of the **DATA\_TRANSFER** type will be canceled. 2. The notification type of the progress update must be live view. For details, see the example in [startBackgroundRunning()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_DATA_TRANSFER = 1--><!--Device-BackgroundTaskMode-MODE_DATA_TRANSFER = 1-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_AUDIO_PLAYBACK

```TypeScript
MODE_AUDIO_PLAYBACK = 2
```

Audio and video playback. Use scenario: audio/video playback in the background and audio/video casting. Note: If a continuous task of the **MODE\_AUDIO\_PLAYBACK** type is requested or updated without connecting to AVSession, a notification will appear in the notification panel once the task is successfully requested or updated. Once AVSession is connected, notifications will be sent by AVSession instead of the background task module.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskMode-MODE_AUDIO_PLAYBACK = 2--><!--Device-BackgroundTaskMode-MODE_AUDIO_PLAYBACK = 2-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_AUDIO_RECORDING

```TypeScript
MODE_AUDIO_RECORDING = 3
```

Audio recording. Use scenario: recording and screen capture in the background.\_\_\_MD\_COMMENT\_DESC\_USD\_0\_\_\_ Note: No notification is displayed if a system application requests or updates a continuous task.\_\_\_MD\_COMMENT\_DESC\_USD\_1\_\_\_

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_AUDIO_RECORDING = 3--><!--Device-BackgroundTaskMode-MODE_AUDIO_RECORDING = 3-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_LOCATION

```TypeScript
MODE_LOCATION = 4
```

Positioning and navigation.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskMode-MODE_LOCATION = 4--><!--Device-BackgroundTaskMode-MODE_LOCATION = 4-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_BLUETOOTH_INTERACTION

```TypeScript
MODE_BLUETOOTH_INTERACTION = 5
```

Bluetooth-related services. Use scenario: An application moves to the background while transferring files via Bluetooth.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_BLUETOOTH_INTERACTION = 5--><!--Device-BackgroundTaskMode-MODE_BLUETOOTH_INTERACTION = 5-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_MULTI_DEVICE_CONNECTION

```TypeScript
MODE_MULTI_DEVICE_CONNECTION = 6
```

Multi-device connection. Use scenario: distributed service connection and casting.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskMode-MODE_MULTI_DEVICE_CONNECTION = 6--><!--Device-BackgroundTaskMode-MODE_MULTI_DEVICE_CONNECTION = 6-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_VOIP

```TypeScript
MODE_VOIP = 8
```

Audio and video calls. Use scenario: Chat applications (with audio and video services) transition into the background during audio and video calls. \_\_\_MD\_COMMENT\_DESC\_USD\_0\_\_\_ Note: No notification is displayed if a system application requests or updates a continuous task.\_\_\_MD\_COMMENT\_DESC\_USD\_1\_\_\_

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_VOIP = 8--><!--Device-BackgroundTaskMode-MODE_VOIP = 8-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_TASK_KEEPING

```TypeScript
MODE_TASK_KEEPING = 9
```

Computing tasks. Use scenario: antivirus software. **NOTE**: This capability is available only to PCs/2-in-1 devices, or non-PCs/2-in-1 devices that have obtained the ACL permission \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_TASK_KEEPING = 9--><!--Device-BackgroundTaskMode-MODE_TASK_KEEPING = 9-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_AV_PLAYBACK_AND_RECORD

```TypeScript
MODE_AV_PLAYBACK_AND_RECORD = 12
```

Multimedia services. Use scenarios: audio/video playback, recording, and audio/video calls. The scenario must match that of the subtype. You can select this task type or the corresponding main type for preceding scenarios. For example, you can request a continuous task of the **MODE\_AUDIO\_PLAYBACK** or **MODE\_AV\_PLAYBACK\_AND\_RECORD** type for audio/ video playback.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskMode-MODE_AV_PLAYBACK_AND_RECORD = 12--><!--Device-BackgroundTaskMode-MODE_AV_PLAYBACK_AND_RECORD = 12-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_SPECIAL_SCENARIO_PROCESSING

```TypeScript
MODE_SPECIAL_SCENARIO_PROCESSING = 13
```

Special scenarios (available only for smartphones, tablets, PCs/2-in-1 devices). Use scenarios: An application exports media files in the background or uses a third-party component to cast content in the background. The scenario must match that of the subtype. **NOTE** 1. If an application needs to run in the background for a long time, it can request user authorization through the [requestAuthFromUser]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API and check the authorization result via [checkSpecialScenarioAuth]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. 2. Since API version 24, this capability is available only to applications that have obtainedthe ACL permission \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. For API version 23 and earlier, this capability is available only to applications that have obtained the ACL permission \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_. Applications that have obtained this permission are not affected for API version 24 and later. 3. This task type must be used independently and notifications cannot be combined. Specifically, when you request or update a continuous task, it must be of the **MODE\_SPECIAL\_SCENARIO\_PROCESSING** type. Otherwise, an error is returned.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_SPECIAL_SCENARIO_PROCESSING = 13--><!--Device-BackgroundTaskMode-MODE_SPECIAL_SCENARIO_PROCESSING = 13-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_NEARLINK

```TypeScript
MODE_NEARLINK = 14
```

NearLink device. Use scenario: An application transitions into the background during the process of file transfer using NearLink.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskMode-MODE_NEARLINK = 14--><!--Device-BackgroundTaskMode-MODE_NEARLINK = 14-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

