# NavDestinationMode

NavDestination类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum NavDestinationMode--><!--Device-unnamed-export declare enum NavDestinationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## STANDARD

```TypeScript
STANDARD = 0
```

标准模式的NavDestination。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationMode-STANDARD = 0--><!--Device-NavDestinationMode-STANDARD = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DIALOG

```TypeScript
DIALOG = 1
```

默认透明，进出路由栈不影响下层NavDestination的可见性（onShown、onHidden等生命周期），只会触发onActive、onInactive这两个生命周期。

API version 13之前，默认无系统转场动画。从API version 13开始，支持系统转场动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationMode-DIALOG = 1--><!--Device-NavDestinationMode-DIALOG = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

