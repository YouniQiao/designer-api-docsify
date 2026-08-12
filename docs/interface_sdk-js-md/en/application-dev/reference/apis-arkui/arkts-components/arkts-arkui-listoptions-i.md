# ListOptions

Defines the options of the **List** component.

> **NOTE：**
> 
> To standardize anonymous object definitions, the element definitions here have been revised in API version 18.
> While historical version information is preserved for anonymous objects, there may be cases where the outer element
> 's @since version number is higher than inner elements'. This does not affect interface usability.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface ListOptions--><!--Device-unnamed-interface ListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialIndex

```TypeScript
initialIndex?: number
```

Index of the item to be displayed at the start when the list is initially loaded.Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;If the set value is a negative number or is greater than the index of the last item in the list,the value is invalid. In this case, the default value will be used.&lt;/p&gt;

**Type:** number

**Default:** 0 [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListOptions-initialIndex?: number--><!--Device-ListOptions-initialIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

Scroller, which can be bound to scrollable components.Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;The scroller cannot be bound to other scrollable components.&lt;/p&gt;

**Type:** Scroller

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListOptions-scroller?: Scroller--><!--Device-ListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: number | string
```

Spacing between list items along the main axis.&lt;br&gt;Default value: **0**&lt;br&gt;If the parameter type is number, the unit is vp.Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.&lt;br&gt;If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.&lt;br&gt; Child components of &lt;em&gt;List&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt; are not displayed, but the spacing above and below them still takes effect.&lt;/p&gt;

**Type:** number \| string

**Default:** 0 [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListOptions-space?: number | string--><!--Device-ListOptions-space?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

Spacing between list items along the main axis.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.&lt;br&gt;If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.&lt;br&gt; Child components of &lt;em&gt;ListItemGroup&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt;are not displayed, but the spacing above and below them still takes effect.&lt;br&gt; If both spaceWidth and space are set, spaceWidth will take precedence.&lt;/p&gt;

**Type:** Dimension

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ListOptions-spaceWidth?: Dimension--><!--Device-ListOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

