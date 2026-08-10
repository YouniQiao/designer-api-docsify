# ParticlePropertyAnimation

设置粒子属性生命周期。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ParticlePropertyAnimation<T>--><!--Device-unnamed-export interface ParticlePropertyAnimation<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | ICurve
```

设置动画曲线。

默认值：Curve.Linear

**Type:** [Curve](arkts-arkui-curve-e.md) \| ICurve

**Default:** Curve.Linear

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyAnimation-curve?: Curve | ICurve--><!--Device-ParticlePropertyAnimation-curve?: Curve | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMillis

```TypeScript
endMillis: int
```

动画结束时间。

单位：毫秒。

取值范围：[0, +∞)。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyAnimation-endMillis: int--><!--Device-ParticlePropertyAnimation-endMillis: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from: T
```

属性起始值。非法输入取对应属性的默认值。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyAnimation-from: T--><!--Device-ParticlePropertyAnimation-from: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMillis

```TypeScript
startMillis: int
```

动画开始时间。

单位：毫秒。

取值范围：[0, +∞)。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyAnimation-startMillis: int--><!--Device-ParticlePropertyAnimation-startMillis: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: T
```

属性目标值。非法输入取对应属性的默认值。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyAnimation-to: T--><!--Device-ParticlePropertyAnimation-to: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

