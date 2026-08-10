# SurfaceRotationOptions

定义屏幕旋转时是否锁定当前XComponent所持有的surface的方向。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface SurfaceRotationOptions--><!--Device-unnamed-declare interface SurfaceRotationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lock

```TypeScript
lock?: boolean
```

屏幕旋转时是否锁定surface的方向。如果不设置此参数，默认值为false，表示不锁定方向。

**true**：屏幕旋转时锁定surface的方向。

**false**：屏幕旋转时不锁定surface的方向。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRotationOptions-lock?: boolean--><!--Device-SurfaceRotationOptions-lock?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

