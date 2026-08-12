# AudioPlaybackCaptureMode

Defines mode for playback capture, each mode means different target streams to capture.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-enum AudioPlaybackCaptureMode--><!--Device-audio-enum AudioPlaybackCaptureMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## MODE_ONLY_VOIP

```TypeScript
MODE_ONLY_VOIP = 0x4000
```

Only voip mode. Capture only voice/video communication streams.If [playbackCaptureUid](arkts-audio-audio-audiocaptureroptions-i-sys.md#playbackCaptureUid) is set, only the voice/video communication stream of the specified application is captured.The [playbackCaptureUid](arkts-audio-audio-audiocaptureroptions-i-sys.md#playbackCaptureUid) takes effect only when this mode is set.This mode requires the `ohos.permission.CAPTURE_VOICE_DOWNLINK_AUDIO`permission; otherwise [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createAudioCapturer) fails.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioPlaybackCaptureMode-MODE_ONLY_VOIP = 0x4000--><!--Device-AudioPlaybackCaptureMode-MODE_ONLY_VOIP = 0x4000-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

**System API:** This is a system API.

