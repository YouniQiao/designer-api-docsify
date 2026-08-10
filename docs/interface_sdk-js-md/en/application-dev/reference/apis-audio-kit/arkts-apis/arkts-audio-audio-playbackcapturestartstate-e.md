# PlaybackCaptureStartState

表示调用[requestPlaybackCaptureStart](arkts-audio-audio-audiocapturer-i.md#requestplaybackcapturestart)后异步返回的内录启动状态的枚举。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-enum PlaybackCaptureStartState--><!--Device-audio-enum PlaybackCaptureStartState-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## STATE_SUCCESS

```TypeScript
STATE_SUCCESS = 0
```

启动内录成功。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlaybackCaptureStartState-STATE_SUCCESS = 0--><!--Device-PlaybackCaptureStartState-STATE_SUCCESS = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## STATE_FAILED

```TypeScript
STATE_FAILED = 1
```

启动内录失败。原因是音频打断请求被拒绝或发生系统内部错误。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlaybackCaptureStartState-STATE_FAILED = 1--><!--Device-PlaybackCaptureStartState-STATE_FAILED = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## STATE_NOT_AUTHORIZED

```TypeScript
STATE_NOT_AUTHORIZED = 2
```

用户未授权，启动内录失败。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlaybackCaptureStartState-STATE_NOT_AUTHORIZED = 2--><!--Device-PlaybackCaptureStartState-STATE_NOT_AUTHORIZED = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

