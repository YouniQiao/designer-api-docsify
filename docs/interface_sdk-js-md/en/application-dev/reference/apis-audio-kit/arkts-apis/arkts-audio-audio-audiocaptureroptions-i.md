# AudioCapturerOptions

音频采集器选项信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioCapturerOptions--><!--Device-audio-interface AudioCapturerOptions-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## capturerInfo

```TypeScript
capturerInfo: AudioCapturerInfo
```

音频采集器信息。

**Type:** [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioCapturerOptions-capturerInfo: AudioCapturerInfo--><!--Device-AudioCapturerOptions-capturerInfo: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## playbackCaptureConfig

```TypeScript
playbackCaptureConfig?: AudioPlaybackCaptureConfig
```

音频内录的配置信息。

<br/

**Type:** [AudioPlaybackCaptureConfig](arkts-audio-audio-audioplaybackcaptureconfig-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 12

**Substitutes:** OH_AVScreenCapture

<!--Device-AudioCapturerOptions-playbackCaptureConfig?: AudioPlaybackCaptureConfig--><!--Device-AudioCapturerOptions-playbackCaptureConfig?: AudioPlaybackCaptureConfig-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## playbackCaptureMode

```TypeScript
playbackCaptureMode?: AudioPlaybackCaptureMode
```

内录模式。可设置为AudioPlaybackCaptureMode中的枚举值或其按位或组合，当前仅支持MODE_DEFAULT（0x0）、MODE_MEDIA（0x1）、MODE_EXCLUDING_SELF（0x8000），以及MODE_MEDIA和MODE_EXCLUDING_SELF的按位或组合（0x8001）。

**Type:** [AudioPlaybackCaptureMode](arkts-audio-audio-audioplaybackcapturemode-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerOptions-playbackCaptureMode?: AudioPlaybackCaptureMode--><!--Device-AudioCapturerOptions-playbackCaptureMode?: AudioPlaybackCaptureMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## streamInfo

```TypeScript
streamInfo: AudioStreamInfo
```

音频流信息。

**Type:** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioCapturerOptions-streamInfo: AudioStreamInfo--><!--Device-AudioCapturerOptions-streamInfo: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

