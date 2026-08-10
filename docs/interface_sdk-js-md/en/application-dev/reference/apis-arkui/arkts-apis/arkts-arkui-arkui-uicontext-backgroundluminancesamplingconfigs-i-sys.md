# BackgroundLuminanceSamplingConfigs (System API)

背景取色参数配置。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export interface BackgroundLuminanceSamplingConfigs--><!--Device-unnamed-export interface BackgroundLuminanceSamplingConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## brightThreshold

```TypeScript
brightThreshold?: number
```

浅色亮度阈值：[0, 255]内的整数，设置的深色亮度阈值应小于浅色亮度阈值。

默认值：220

**Type:** number

**Default:** 220

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-brightThreshold?: number--><!--Device-BackgroundLuminanceSamplingConfigs-brightThreshold?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## darkThreshold

```TypeScript
darkThreshold?: number
```

深色亮度阈值：[0, 255]内的整数，设置的深色亮度阈值应小于浅色亮度阈值。

默认值：150

**Type:** number

**Default:** 150

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-darkThreshold?: number--><!--Device-BackgroundLuminanceSamplingConfigs-darkThreshold?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## region

```TypeScript
region?: Edges<LengthMetrics>
```

相对组件的取色区域偏移，以组件自身的左上点为基准进行偏移计算。

默认使用组件自身区域

**Type:** [Edges](arkts-arkui-edges-i.md)&lt;[LengthMetrics](arkts-arkui-lengthmetrics-t.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-region?: Edges<LengthMetrics>--><!--Device-BackgroundLuminanceSamplingConfigs-region?: Edges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## samplingInterval

```TypeScript
samplingInterval?: number
```

取色间隔，单位为毫秒，最小值180ms。

默认值：500

**Type:** number

**Default:** 500

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-samplingInterval?: number--><!--Device-BackgroundLuminanceSamplingConfigs-samplingInterval?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

