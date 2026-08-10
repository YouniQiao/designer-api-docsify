# ProgressType

进度条类型。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare enum ProgressType--><!--Device-unnamed-declare enum ProgressType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Linear

```TypeScript
Linear = 0
```

线性样式。从API version 9开始，当高度大于宽度时，自适应垂直显示。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressType-Linear = 0--><!--Device-ProgressType-Linear = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Ring

```TypeScript
Ring = 1
```

环形无刻度样式，环形圆环逐渐显示直至完全填充。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressType-Ring = 1--><!--Device-ProgressType-Ring = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Eclipse

```TypeScript
Eclipse = 2
```

圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressType-Eclipse = 2--><!--Device-ProgressType-Eclipse = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ScaleRing

```TypeScript
ScaleRing = 3
```

环形有刻度样式，显示类似时钟刻度形式的进度展示效果。从API version 9开始，刻度外圈出现重叠时自动转换为环形无刻度进度条。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressType-ScaleRing = 3--><!--Device-ProgressType-ScaleRing = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Capsule

```TypeScript
Capsule = 4
```

胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同，中段的进度展示效果与Linear相同。从API version 9开始，当高度大于宽度时，自适应垂直显示。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressType-Capsule = 4--><!--Device-ProgressType-Capsule = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

