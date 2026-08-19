# RowOptions

Sets the spacing between child components of the **Row** component. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While starting version information is preserved for historical anonymous objects, there may be cases where the &gt; outer element's @since version number is higher than inner element's. This does not affect interface usability.

**Since:** 18

<!--Device-unnamed-declare interface RowOptions--><!--Device-unnamed-declare interface RowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## space

```TypeScript
space?: string | number
```

Spacing between child components. Since API version 9, this parameter does not take effect when it is set to a negative number or when **justifyContent** is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround** or **FlexAlign.SpaceEvenly**. Unit: vp. If an invalid value is set, the default value is used instead. &gt; **NOTE：**&gt; &gt; The value of **space** can be a number greater than or equal to 0 or a string that can be converted to a number. &gt; Default value: **0**.

**Type:** string \| number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RowOptions-space?: string | number--><!--Device-RowOptions-space?: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

