# AudioSessionStateChangeHint

枚举用于音频会话状态变更提示。

当用户监听到音频会话状态变化事件（即收到[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)事件）时，获取相关信息。

此类型表示根据焦点策略对音频会话执行的操作，包括暂停、调整音量等。

详情请参阅文档[音频会话管理](../../../media/audio/audio-session-management.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-audio-enum AudioSessionStateChangeHint--><!--Device-audio-enum AudioSessionStateChangeHint-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_RESUME

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_RESUME = 0
```

提示音频会话恢复，应用可主动触发开始渲染等操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_RESUME = 0--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_RESUME = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE = 1
```

提示音频会话暂停，暂时失去音频焦点。当焦点再次可用时，会收到 AUDIO_SESSION_STATE_CHANGE_HINT_RESUME 事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE = 1--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_STOP

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_STOP = 2
```

提示音频会话因焦点被抢占而停止，彻底失去音频焦点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_STOP = 2--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_STOP = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP = 3
```

提示音频会话因长时间无业务而被系统停止，导致失去音频焦点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP = 3--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP = 3-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_DUCK

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_DUCK = 4
```

提示音频会话躲避开始，降低音量播放。

如果已启用  
[enableMuteSuggestionWhenMixWithOthers](arkts-audio-audio-audiosessionmanager-i.md#enablemutesuggestionwhenmixwithothers)，此时可以选择执行静音操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_DUCK = 4--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_DUCK = 4-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK = 5
```

提示音频会话躲避结束，恢复音量播放。

如果已启用  
[enableMuteSuggestionWhenMixWithOthers](arkts-audio-audio-audiosessionmanager-i.md#enablemutesuggestionwhenmixwithothers)，此时可取消静音。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK = 5--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK = 5-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION = 6
```

静音播放建议。

当其他应用程序开始播放不可混音的音频时，应用程序可以自行决定是否静音。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION = 6--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION = 6-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION = 7
```

取消静音播放建议。

当其他应用程序不可混音的音频已结束，该应用程序可自行决定是否取消静音。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION = 7--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION = 7-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_MUTE

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_MUTE = 8
```

提示音频会话静音。

该提示仅在以下条件满足后才会收到：通过接口[setAudioSessionBehavior](arkts-audio-audio-audiosessionmanager-i.md#setaudiosessionbehavior)设置参数  
[AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md).MUTE_WHEN_INTERRUPTED，并已调用  
[setAudioSessionScene](arkts-audio-audio-audiosessionmanager-i.md#setaudiosessionscene)，且音频会话已激活。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_MUTE = 8--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_MUTE = 8-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE

```TypeScript
AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE = 9
```

提示音频会话解除静音，恢复播放。

该提示仅在以下条件满足后才会收到：通过接口[setAudioSessionBehavior](arkts-audio-audio-audiosessionmanager-i.md#setaudiosessionbehavior)设置参数  
[AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md).MUTE_WHEN_INTERRUPTED，并已调用  
[setAudioSessionScene](arkts-audio-audio-audiosessionmanager-i.md#setaudiosessionscene)，且音频会话已激活。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE = 9--><!--Device-AudioSessionStateChangeHint-AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE = 9-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

