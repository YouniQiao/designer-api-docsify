# AVScreenCaptureStateCode

屏幕录制的状态回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-enum AVScreenCaptureStateCode--><!--Device-unnamed-enum AVScreenCaptureStateCode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_STARTED

```TypeScript
SCREENCAPTURE_STATE_STARTED = 0
```

录屏已开始。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STARTED = 0--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STARTED = 0-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_CANCELED

```TypeScript
SCREENCAPTURE_STATE_CANCELED = 1
```

录屏被取消。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_CANCELED = 1--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_CANCELED = 1-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_STOPPED_BY_USER

```TypeScript
SCREENCAPTURE_STATE_STOPPED_BY_USER = 2
```

录屏被用户手动停止。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STOPPED_BY_USER = 2--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STOPPED_BY_USER = 2-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER

```TypeScript
SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER = 3
```

录屏被其他录屏打断。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER = 3--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER = 3-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_STOPPED_BY_CALL

```TypeScript
SCREENCAPTURE_STATE_STOPPED_BY_CALL = 4
```

录屏被来电打断。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STOPPED_BY_CALL = 4--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STOPPED_BY_CALL = 4-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_MIC_UNAVAILABLE

```TypeScript
SCREENCAPTURE_STATE_MIC_UNAVAILABLE = 5
```

录屏无法使用麦克风收音。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_MIC_UNAVAILABLE = 5--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_MIC_UNAVAILABLE = 5-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_MIC_MUTED_BY_USER

```TypeScript
SCREENCAPTURE_STATE_MIC_MUTED_BY_USER = 6
```

麦克风被用户关闭。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_MIC_MUTED_BY_USER = 6--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_MIC_MUTED_BY_USER = 6-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER

```TypeScript
SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER = 7
```

麦克风被用户打开。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER = 7--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER = 7-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE

```TypeScript
SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE = 8
```

录屏进入隐私页面。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE = 8--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE = 8-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE

```TypeScript
SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE = 9
```

录屏退出隐私页面。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE = 9--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE = 9-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES

```TypeScript
SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10
```

系统用户切换，录屏中断。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_PAUSED_BY_USER

```TypeScript
SCREENCAPTURE_STATE_PAUSED_BY_USER = 11
```

录屏已被用户暂停。

26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_PAUSED_BY_USER = 11--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_PAUSED_BY_USER = 11-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_RESUMED_BY_USER

```TypeScript
SCREENCAPTURE_STATE_RESUMED_BY_USER = 12
```

录屏已被用户恢复。

26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_RESUMED_BY_USER = 12--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_RESUMED_BY_USER = 12-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_PAUSED_BY_APP

```TypeScript
SCREENCAPTURE_STATE_PAUSED_BY_APP = 13
```

录屏已被应用程序暂停。

26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_PAUSED_BY_APP = 13--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_PAUSED_BY_APP = 13-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

## SCREENCAPTURE_STATE_RESUMED_BY_APP

```TypeScript
SCREENCAPTURE_STATE_RESUMED_BY_APP = 14
```

录屏已被应用程序恢复。

26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_RESUMED_BY_APP = 14--><!--Device-AVScreenCaptureStateCode-SCREENCAPTURE_STATE_RESUMED_BY_APP = 14-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

