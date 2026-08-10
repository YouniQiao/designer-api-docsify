# ParticlePropertyAnimation

设置粒子属性生命周期。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-interface ParticlePropertyAnimation<T>--><!--Device-unnamed-interface ParticlePropertyAnimation<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | ICurve
```

设置动画曲线。

默认值：Curve.Linear

**Type:** [Curve](../arkts-apis/arkts-arkui-curve-e.md) \| ICurve

**Default:** Curve.Linear

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyAnimation-curve?: Curve | ICurve--><!--Device-ParticlePropertyAnimation-curve?: Curve | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMillis

```TypeScript
endMillis: number
```

动画结束时间。

单位：毫秒。

取值范围：[0, +∞)。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyAnimation-endMillis: number--><!--Device-ParticlePropertyAnimation-endMillis: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from: T
```

属性起始值。非法输入取对应属性的默认值。

**Type:** T

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyAnimation-from: T--><!--Device-ParticlePropertyAnimation-from: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMillis

```TypeScript
startMillis: number
```

动画开始时间。

单位：毫秒。

取值范围：[0, +∞)。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyAnimation-startMillis: number--><!--Device-ParticlePropertyAnimation-startMillis: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: T
```

属性目标值。非法输入取对应属性的默认值。

**Type:** T

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyAnimation-to: T--><!--Device-ParticlePropertyAnimation-to: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

