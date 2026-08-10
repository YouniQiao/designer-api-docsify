# SourceType

表示录制音频流类型的枚举。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-enum SourceType--><!--Device-audio-enum SourceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_INVALID

```TypeScript
SOURCE_TYPE_INVALID = -1
```

无效的音频源。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_INVALID = -1--><!--Device-SourceType-SOURCE_TYPE_INVALID = -1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_MIC

```TypeScript
SOURCE_TYPE_MIC = 0
```

Mic音频源。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_MIC = 0--><!--Device-SourceType-SOURCE_TYPE_MIC = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_VOICE_RECOGNITION

```TypeScript
SOURCE_TYPE_VOICE_RECOGNITION = 1
```

语音识别源。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_VOICE_RECOGNITION = 1--><!--Device-SourceType-SOURCE_TYPE_VOICE_RECOGNITION = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_PLAYBACK_CAPTURE

```TypeScript
SOURCE_TYPE_PLAYBACK_CAPTURE = 2
```

播放音频流（内录）录制音频源。

<br/

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 12

**Substitutes:** OH_AVScreenCapture

<!--Device-SourceType-SOURCE_TYPE_PLAYBACK_CAPTURE = 2--><!--Device-SourceType-SOURCE_TYPE_PLAYBACK_CAPTURE = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## SOURCE_TYPE_VOICE_COMMUNICATION

```TypeScript
SOURCE_TYPE_VOICE_COMMUNICATION = 7
```

语音通话场景的音频源（单独启动录制不会开启3A算法，需同时使用[STREAM_USAGE_VOICE_COMMUNICATION](arkts-audio-audio-streamusage-e.md)或  
[STREAM_USAGE_VIDEO_COMMUNICATION](arkts-audio-audio-streamusage-e.md)类型的AudioRender起播才会触发开启3A算法）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_VOICE_COMMUNICATION = 7--><!--Device-SourceType-SOURCE_TYPE_VOICE_COMMUNICATION = 7-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_VOICE_MESSAGE

```TypeScript
SOURCE_TYPE_VOICE_MESSAGE = 10
```

短语音消息的音频源。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_VOICE_MESSAGE = 10--><!--Device-SourceType-SOURCE_TYPE_VOICE_MESSAGE = 10-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_CAMCORDER

```TypeScript
SOURCE_TYPE_CAMCORDER = 13
```

录像的音频源。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_CAMCORDER = 13--><!--Device-SourceType-SOURCE_TYPE_CAMCORDER = 13-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_UNPROCESSED

```TypeScript
SOURCE_TYPE_UNPROCESSED = 14
```

麦克风纯净录音的音频源（系统不做任何算法处理）。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_UNPROCESSED = 14--><!--Device-SourceType-SOURCE_TYPE_UNPROCESSED = 14-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_LIVE

```TypeScript
SOURCE_TYPE_LIVE = 17
```

直播场景的音频源，在支持的设备上会提供系统回声消除能力。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_LIVE = 17--><!--Device-SourceType-SOURCE_TYPE_LIVE = 17-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

