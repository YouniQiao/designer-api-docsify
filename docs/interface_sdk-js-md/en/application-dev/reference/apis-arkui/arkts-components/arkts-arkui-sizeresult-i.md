# SizeResult

> **NOTE：**&gt; &gt; - The custom layout does not support the LazyForEach syntax. &gt; - When a custom layout is created in builder mode, only **this.builder()** is allowed in the **build()** method &gt; of a custom component, as shown in the recommended usage in the example below. &gt; - The size parameters of the parent component (custom component), except **aspectRatio**, are at a lower &gt; priority than those specified by onMeasureSize. &gt; - The position parameters of the child component, except **offset**, **position**, and **markAnchor**, are at &gt; a lower priority than those specified by onPlaceChildren, &gt; and do not take effect. &gt; - When using the custom layout method, you must call **onMeasureSize** and **onPlaceChildren** at the same &gt; time for the layout to display properly.

**Since:** 10

<!--Device-unnamed-declare interface SizeResult--><!--Device-unnamed-declare interface SizeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## height

```TypeScript
height: number
```

Height obtained from the measurement result. Unit: vp, Value range: (-∞,+∞).

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SizeResult-height: number--><!--Device-SizeResult-height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width obtained from the measurement result. Unit: vp, Value range: (-∞,+∞).

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SizeResult-width: number--><!--Device-SizeResult-width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

