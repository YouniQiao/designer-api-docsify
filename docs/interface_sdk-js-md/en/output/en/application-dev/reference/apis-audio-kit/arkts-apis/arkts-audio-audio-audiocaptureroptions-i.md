# AudioCapturerOptions

Describes audio capturer configurations.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioCapturerOptions--><!--Device-audio-interface AudioCapturerOptions-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## capturerInfo

```TypeScript
capturerInfo: AudioCapturerInfo
```

Audio capturer information.

**Type:** AudioCapturerInfo

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioCapturerOptions-capturerInfo: AudioCapturerInfo--><!--Device-AudioCapturerOptions-capturerInfo: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## playbackCaptureConfig

```TypeScript
playbackCaptureConfig?: AudioPlaybackCaptureConfig
```

Defines configuration for capturing played audio. This API is supported since API version 10 and deprecated since API version 12. You are advised to use \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instead.

**Type:** AudioPlaybackCaptureConfig

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

The playback capture mode for audio capturer. This can be a combination of the available \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** AudioPlaybackCaptureMode

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerOptions-playbackCaptureMode?: AudioPlaybackCaptureMode--><!--Device-AudioCapturerOptions-playbackCaptureMode?: AudioPlaybackCaptureMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## streamInfo

```TypeScript
streamInfo: AudioStreamInfo
```

Audio stream information.

**Type:** AudioStreamInfo

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioCapturerOptions-streamInfo: AudioStreamInfo--><!--Device-AudioCapturerOptions-streamInfo: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

