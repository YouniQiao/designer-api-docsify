# ListDividerOptions

Defines the divider style of the list or list item group.

> **NOTE：**&gt;
> To standardize anonymous object definitions, the element definitions here have been revised in API version 18.
> While historical version information is preserved for anonymous objects, there may be cases where the outer element
> 's

**Since:** 18

<!--Device-unnamed-declare interface ListDividerOptions--><!--Device-unnamed-declare interface ListDividerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## color

```TypeScript
color?: ResourceColor
```

Color of the divider. Anonymous Object Rectification.<p>&lt;strong&gt;Default value&lt;/strong&gt;: 0x08000000 </p>

**Type:** ResourceColor

**Default:** 0x08000000 [since 18]

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-color?: ResourceColor--><!--Device-ListDividerOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Length
```

Distance between the divider and the end edge of the list. Anonymous Object Rectification.<p>&lt;strong&gt;Default value&lt;/strong&gt;: **0**<br>Unit: vp <br>&lt;strong&gt;NOTE&lt;/strong&gt; <br>If this parameter is set to a negative number or a percentage, the default value will be used. <br>If &lt;strong&gt;endMargin&lt;/strong&gt; and &lt;strong&gt;startMargin&lt;/strong&gt; add up to a value that exceeds the column width, they will be set to &lt;strong&gt;0&lt;/strong&gt;. </p>

**Type:** Length

**Default:** 0vp [since 18]

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-endMargin?: Length--><!--Device-ListDividerOptions-endMargin?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Length
```

Distance between the divider and the start edge of the list. Anonymous Object Rectification.<p>&lt;strong&gt;Default value&lt;/strong&gt;: **0**<br>Unit: vp <br>&lt;strong&gt;NOTE&lt;/strong&gt; <br>If this parameter is set to a negative number or a percentage, the default value will be used. <br>If &lt;strong&gt;endMargin&lt;/strong&gt; and &lt;strong&gt;startMargin&lt;/strong&gt; add up to a value that exceeds the column width, they will be set to &lt;strong&gt;0&lt;/strong&gt;. </p>

**Type:** Length

**Default:** 0vp [since 18]

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-startMargin?: Length--><!--Device-ListDividerOptions-startMargin?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth: Length
```

Width of the divider. <br>Unit: vp Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>If this parameter is set to a negative number, a percentage, or a value greater than or equal to the length of the list content area, the value &lt;strong&gt;0&lt;/strong&gt; will be used. </p>

**Type:** Length

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-strokeWidth: Length--><!--Device-ListDividerOptions-strokeWidth: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

