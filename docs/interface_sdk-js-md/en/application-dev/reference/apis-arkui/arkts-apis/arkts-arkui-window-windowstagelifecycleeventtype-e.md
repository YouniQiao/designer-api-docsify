# WindowStageLifecycleEventType

WindowStage生命周期的状态类型枚举。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-enum WindowStageLifecycleEventType--><!--Device-window-enum WindowStageLifecycleEventType-End-->

**System capability:** SystemCapability.Window.SessionManager

## SHOWN

```TypeScript
SHOWN = 1
```

切到前台，例如点击应用图标启动，无论是首次启动还是从后台启动均会触发。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStageLifecycleEventType-SHOWN = 1--><!--Device-WindowStageLifecycleEventType-SHOWN = 1-End-->

**System capability:** SystemCapability.Window.SessionManager

## RESUMED

```TypeScript
RESUMED = 2
```

前台可交互状态，例如打开应用后，应用处于前台，且可以与用户交互的状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStageLifecycleEventType-RESUMED = 2--><!--Device-WindowStageLifecycleEventType-RESUMED = 2-End-->

**System capability:** SystemCapability.Window.SessionManager

## PAUSED

```TypeScript
PAUSED = 3
```

前台不可交互状态，例如应用在前台时，进入多任务界面，应用依然处于前台但不可以与用户交互的状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStageLifecycleEventType-PAUSED = 3--><!--Device-WindowStageLifecycleEventType-PAUSED = 3-End-->

**System capability:** SystemCapability.Window.SessionManager

## HIDDEN

```TypeScript
HIDDEN = 4
```

切到后台，例如应用上滑退出、应用窗口关闭。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStageLifecycleEventType-HIDDEN = 4--><!--Device-WindowStageLifecycleEventType-HIDDEN = 4-End-->

**System capability:** SystemCapability.Window.SessionManager

