# GestureObserverConfigs

The observer options for global gesture listener.

@interface GestureObserverConfigs

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export interface GestureObserverConfigs--><!--Device-unnamed-export interface GestureObserverConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## actionPhases

```TypeScript
actionPhases: Array<GestureActionPhase>
```

The gesture callback phases want to monitor. Only the specific action phases can be notified when the gesture is triggered. If empty array provided, the register will has no any effect.

**Type:** Array&lt;[GestureActionPhase](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-gestureactionphase-e.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureObserverConfigs-actionPhases: Array<GestureActionPhase>--><!--Device-GestureObserverConfigs-actionPhases: Array<GestureActionPhase>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

