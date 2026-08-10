# BackgroundTaskSubmode

长时任务子类型。通常与长时任务主类型[BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md)配合使用，对照关系请参考长时任务主类型与子类型对照表，两者共同作为API version 21新增的申请、更新长时任务接口入参，用于指定长时任务类型。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-backgroundTaskManager-export enum BackgroundTaskSubmode--><!--Device-backgroundTaskManager-export enum BackgroundTaskSubmode-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_CAR_KEY_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_CAR_KEY_NORMAL_NOTIFICATION = 1
```

车钥匙类型，通知类型为普通文本通知。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_CAR_KEY_NORMAL_NOTIFICATION = 1--><!--Device-BackgroundTaskSubmode-SUBMODE_CAR_KEY_NORMAL_NOTIFICATION = 1-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_NORMAL_NOTIFICATION = 2
```

普通文本通知。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskSubmode-SUBMODE_NORMAL_NOTIFICATION = 2--><!--Device-BackgroundTaskSubmode-SUBMODE_NORMAL_NOTIFICATION = 2-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_LIVE_VIEW_NOTIFICATION

```TypeScript
SUBMODE_LIVE_VIEW_NOTIFICATION = 3
```

实况窗通知。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_LIVE_VIEW_NOTIFICATION = 3--><!--Device-BackgroundTaskSubmode-SUBMODE_LIVE_VIEW_NOTIFICATION = 3-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4
```

音视频播放，通知类型为普通文本通知。根据实际场景选择是否接入[AVSession](../../../media/avsession/avsession-overview.md)。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskSubmode-SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4--><!--Device-BackgroundTaskSubmode-SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_AVSESSION_AUDIO_PLAYBACK

```TypeScript
SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5
```

已接入[AVSession](../../../media/avsession/avsession-overview.md)的音视频播放场景，不发送通知。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackgroundTaskSubmode-SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5--><!--Device-BackgroundTaskSubmode-SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION = 6
```

录音，通知类型为普通文本通知。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION = 6--><!--Device-BackgroundTaskSubmode-SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION = 6-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION = 7
```

录屏，通知类型为普通文本通知。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION = 7--><!--Device-BackgroundTaskSubmode-SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION = 7-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION = 8
```

通话，通知类型为普通文本通知。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION = 8--><!--Device-BackgroundTaskSubmode-SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION = 8-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION = 9
```

媒体处理，例如：应用在后台导出媒体文件，通知类型为普通文本通知。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION = 9--><!--Device-BackgroundTaskSubmode-SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION = 9-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION = 10
```

视频投播，例如：应用使用三方投播组件在后台进行投播，通知类型为普通文本通知。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskSubmode-SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION = 10--><!--Device-BackgroundTaskSubmode-SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION = 10-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## SUBMODE_WORK_OUT_NORMAL_NOTIFICATION

```TypeScript
SUBMODE_WORK_OUT_NORMAL_NOTIFICATION = 11
```

运动，例如：应用在后台有室内跑步场景，通知类型为普通文本通知。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskSubmode-SUBMODE_WORK_OUT_NORMAL_NOTIFICATION = 11--><!--Device-BackgroundTaskSubmode-SUBMODE_WORK_OUT_NORMAL_NOTIFICATION = 11-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

