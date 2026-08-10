# GestureMask

定义是否屏蔽子组件手势。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum GestureMask--><!--Device-unnamed-declare enum GestureMask-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Normal

```TypeScript
Normal
```

不屏蔽子组件的手势，按照默认手势识别顺序进行识别。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GestureMask-Normal--><!--Device-GestureMask-Normal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IgnoreInternal

```TypeScript
IgnoreInternal
```

屏蔽子组件的手势，包括子组件上系统内置的手势，如子组件为List组件时，内置的滑动手势同样会被屏蔽。 若父子组件区域存在部分重叠，则只会屏蔽父子组件重叠的部分。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GestureMask-IgnoreInternal--><!--Device-GestureMask-IgnoreInternal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

