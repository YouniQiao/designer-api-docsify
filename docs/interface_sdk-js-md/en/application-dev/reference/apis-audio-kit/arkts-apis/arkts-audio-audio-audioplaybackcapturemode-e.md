# AudioPlaybackCaptureMode

表示内录（录制设备内部应用的声音）模式的枚举。不同模式决定可录制的目标播放流类型。支持通过按位或组合枚举值，当前仅支持MODE_DEFAULT（0x0）、MODE_MEDIA（0x1）、MODE_EXCLUDING_SELF（0x8000），以及MODE_MEDIA和MODE_EXCLUDING_SELF的按位或组合（0x8001）。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-enum AudioPlaybackCaptureMode--><!--Device-audio-enum AudioPlaybackCaptureMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## MODE_DEFAULT

```TypeScript
MODE_DEFAULT = 0x0
```

默认模式。录制大部分音频流，但不包括提示音流和隐私流。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioPlaybackCaptureMode-MODE_DEFAULT = 0x0--><!--Device-AudioPlaybackCaptureMode-MODE_DEFAULT = 0x0-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## MODE_MEDIA

```TypeScript
MODE_MEDIA = 0x1
```

媒体模式。录制媒体、语音消息和未知类型的音频流。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioPlaybackCaptureMode-MODE_MEDIA = 0x1--><!--Device-AudioPlaybackCaptureMode-MODE_MEDIA = 0x1-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## MODE_EXCLUDING_SELF

```TypeScript
MODE_EXCLUDING_SELF = 0x8000
```

排除自身模式。录制除应用自身播放的音频以外的音频流。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioPlaybackCaptureMode-MODE_EXCLUDING_SELF = 0x8000--><!--Device-AudioPlaybackCaptureMode-MODE_EXCLUDING_SELF = 0x8000-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

