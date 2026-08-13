# ListDividerOptions

Defines the divider style of the list or list item group. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-declare interface ListDividerOptions--><!--Device-unnamed-declare interface ListDividerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Color of the divider. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;Default value&lt;/strong&gt;: 0x08000000 &lt;/p&gt;

**Type:** ResourceColor

**Default:** 0x08000000 [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-color?: ResourceColor--><!--Device-ListDividerOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Length
```

Distance between the divider and the end edge of the list. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;Default value&lt;/strong&gt;: **0**&lt;br&gt;Unit: vp &lt;br&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;If this parameter is set to a negative number or a percentage, the default value will be used. &lt;br&gt;If &lt;strong&gt;endMargin&lt;/strong&gt; and &lt;strong&gt;startMargin&lt;/strong&gt; add up to a value that exceeds the column width, they will be set to &lt;strong&gt;0&lt;/strong&gt;. &lt;/p&gt;

**Type:** Length

**Default:** 0vp [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-endMargin?: Length--><!--Device-ListDividerOptions-endMargin?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Length
```

Distance between the divider and the start edge of the list. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;Default value&lt;/strong&gt;: **0**&lt;br&gt;Unit: vp &lt;br&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;If this parameter is set to a negative number or a percentage, the default value will be used. &lt;br&gt;If &lt;strong&gt;endMargin&lt;/strong&gt; and &lt;strong&gt;startMargin&lt;/strong&gt; add up to a value that exceeds the column width, they will be set to &lt;strong&gt;0&lt;/strong&gt;. &lt;/p&gt;

**Type:** Length

**Default:** 0vp [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-startMargin?: Length--><!--Device-ListDividerOptions-startMargin?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth: Length
```

Width of the divider. &lt;br&gt;Unit: vp Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;If this parameter is set to a negative number, a percentage, or a value greater than or equal to the length of the list content area, the value &lt;strong&gt;0&lt;/strong&gt; will be used. &lt;/p&gt;

**Type:** Length

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-strokeWidth: Length--><!--Device-ListDividerOptions-strokeWidth: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

