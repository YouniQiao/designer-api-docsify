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

Only voip mode. Capture only voice/video communication streams. If \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is set, only the voice/video communication stream of the specified application is captured. The \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ takes effect only when this mode is set. This mode requires the \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ permission; otherwise \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ fails.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioPlaybackCaptureMode-MODE_ONLY_VOIP = 0x4000--><!--Device-AudioPlaybackCaptureMode-MODE_ONLY_VOIP = 0x4000-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

**System API:** This is a system API.

