# GestureGroupGestureHandlerOptions

手势组处理器配置参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface GestureGroupGestureHandlerOptions--><!--Device-unnamed-export interface GestureGroupGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gestures

```TypeScript
gestures: GestureHandler[]
```

设置手势组中需要包含的手势集合。

**说明：**

当需要为一个组件同时添加单击和双击手势时，可在[GestureGroup](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中添加两个[TapGesture](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)，需要双击手势在前，单击手势在后，否则不生效。

**Type:** [GestureHandler](arkts-arkui-gesturehandler-c.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroupGestureHandlerOptions-gestures: GestureHandler[]--><!--Device-GestureGroupGestureHandlerOptions-gestures: GestureHandler[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode: GestureMode
```

设置组合手势识别模式。

默认值：GestureMode.Sequence

**Type:** [GestureMode](arkts-arkui-gesture-gesturemode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode--><!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

