# StreamUsage

表示播放音频流类型的枚举。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-audio-enum StreamUsage--><!--Device-audio-enum StreamUsage-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_UNKNOWN

```TypeScript
STREAM_USAGE_UNKNOWN = 0
```

未知类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_UNKNOWN = 0--><!--Device-StreamUsage-STREAM_USAGE_UNKNOWN = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_MEDIA

```TypeScript
STREAM_USAGE_MEDIA = 1
```

媒体。

从API version 7开始支持，从API version 10开始废弃，建议使用该枚举中的STREAM_USAGE_MUSIC、STREAM_USAGE_MOVIE、STREAM_USAGE_GAME或STREAM_USAGE_AUDIOBOOK替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** ohos.multimedia.audio.StreamUsage.STREAM_USAGE_MUSIC

<!--Device-StreamUsage-STREAM_USAGE_MEDIA = 1--><!--Device-StreamUsage-STREAM_USAGE_MEDIA = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_MUSIC

```TypeScript
STREAM_USAGE_MUSIC = 1
```

音乐。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_MUSIC = 1--><!--Device-StreamUsage-STREAM_USAGE_MUSIC = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_VOICE_COMMUNICATION

```TypeScript
STREAM_USAGE_VOICE_COMMUNICATION = 2
```

VoIP语音通话（该流类型起播时，会触发开启3A算法）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_VOICE_COMMUNICATION = 2--><!--Device-StreamUsage-STREAM_USAGE_VOICE_COMMUNICATION = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_VOICE_ASSISTANT

```TypeScript
STREAM_USAGE_VOICE_ASSISTANT = 3
```

语音播报。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_VOICE_ASSISTANT = 3--><!--Device-StreamUsage-STREAM_USAGE_VOICE_ASSISTANT = 3-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_ALARM

```TypeScript
STREAM_USAGE_ALARM = 4
```

闹钟。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_ALARM = 4--><!--Device-StreamUsage-STREAM_USAGE_ALARM = 4-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_VOICE_MESSAGE

```TypeScript
STREAM_USAGE_VOICE_MESSAGE = 5
```

语音消息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_VOICE_MESSAGE = 5--><!--Device-StreamUsage-STREAM_USAGE_VOICE_MESSAGE = 5-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_NOTIFICATION_RINGTONE

```TypeScript
STREAM_USAGE_NOTIFICATION_RINGTONE = 6
```

通知铃声。

从API version 7开始支持，从API version 10开始废弃，建议使用该枚举中的STREAM_USAGE_RINGTONE替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** ohos.multimedia.audio.StreamUsage#STREAM_USAGE_RINGTONE

<!--Device-StreamUsage-STREAM_USAGE_NOTIFICATION_RINGTONE = 6--><!--Device-StreamUsage-STREAM_USAGE_NOTIFICATION_RINGTONE = 6-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_RINGTONE

```TypeScript
STREAM_USAGE_RINGTONE = 6
```

铃声。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_RINGTONE = 6--><!--Device-StreamUsage-STREAM_USAGE_RINGTONE = 6-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_NOTIFICATION

```TypeScript
STREAM_USAGE_NOTIFICATION = 7
```

通知音。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_NOTIFICATION = 7--><!--Device-StreamUsage-STREAM_USAGE_NOTIFICATION = 7-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_ACCESSIBILITY

```TypeScript
STREAM_USAGE_ACCESSIBILITY = 8
```

无障碍。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_ACCESSIBILITY = 8--><!--Device-StreamUsage-STREAM_USAGE_ACCESSIBILITY = 8-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_MOVIE

```TypeScript
STREAM_USAGE_MOVIE = 10
```

电影或视频。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_MOVIE = 10--><!--Device-StreamUsage-STREAM_USAGE_MOVIE = 10-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_GAME

```TypeScript
STREAM_USAGE_GAME = 11
```

游戏。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_GAME = 11--><!--Device-StreamUsage-STREAM_USAGE_GAME = 11-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_AUDIOBOOK

```TypeScript
STREAM_USAGE_AUDIOBOOK = 12
```

有声读物（包括听书、相声、评书）、听新闻、播客等。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_AUDIOBOOK = 12--><!--Device-StreamUsage-STREAM_USAGE_AUDIOBOOK = 12-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_NAVIGATION

```TypeScript
STREAM_USAGE_NAVIGATION = 13
```

导航。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_NAVIGATION = 13--><!--Device-StreamUsage-STREAM_USAGE_NAVIGATION = 13-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## STREAM_USAGE_VIDEO_COMMUNICATION

```TypeScript
STREAM_USAGE_VIDEO_COMMUNICATION = 17
```

VoIP视频通话（该流类型起播时，会触发开启3A算法）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StreamUsage-STREAM_USAGE_VIDEO_COMMUNICATION = 17--><!--Device-StreamUsage-STREAM_USAGE_VIDEO_COMMUNICATION = 17-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

