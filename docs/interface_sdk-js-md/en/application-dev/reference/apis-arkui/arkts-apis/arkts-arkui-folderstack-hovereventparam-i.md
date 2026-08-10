# HoverEventParam

当前设备与悬停状态相关的参数，包括设备的折叠状态、悬停状态、应用方向以及窗口模式枚举。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface HoverEventParam--><!--Device-unnamed-export declare interface HoverEventParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appRotation

```TypeScript
appRotation: AppRotation
```

当前应用方向。

**Type:** [AppRotation](arkts-arkui-approtation-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HoverEventParam-appRotation: AppRotation--><!--Device-HoverEventParam-appRotation: AppRotation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foldStatus

```TypeScript
foldStatus: FoldStatus
```

当前设备的折叠状态。

**Type:** [FoldStatus](arkts-arkui-foldstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HoverEventParam-foldStatus: FoldStatus--><!--Device-HoverEventParam-foldStatus: FoldStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isHoverMode

```TypeScript
isHoverMode: boolean
```

当前是否为悬停态。设置为true时表示当前为悬停态，设置为false时表示当前为非悬停态。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HoverEventParam-isHoverMode: boolean--><!--Device-HoverEventParam-isHoverMode: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowStatusType

```TypeScript
windowStatusType: WindowStatusType
```

窗口模式枚举。

**Type:** [WindowStatusType](../arkts-components/arkts-arkui-windowstatustype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HoverEventParam-windowStatusType: WindowStatusType--><!--Device-HoverEventParam-windowStatusType: WindowStatusType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

