# DigitIndicator

A constructor used to create a **DigitIndicator** object. It inherits from [Indicator](arkts-arkui-indicator-c.md). &gt; **NOTE：**&gt; &gt; When pages are turned by group, the child nodes displayed in the digit-style navigation indicator do not count &gt; placeholder nodes. &gt; &gt; The maximum value of maxFontScale for the digit-style navigation indicator is &gt; **2**. &gt; &gt; The mirror display of the page number depends on the RTL status of the system.

**Inheritance/Implementation:** DigitIndicator extends Indicator<DigitIndicator>

**Since:** 10

<!--Device-unnamed-declare class DigitIndicator--><!--Device-unnamed-declare class DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **DotIndicator** object. &gt; **NOTE：**&gt; &gt; - When pressed, the navigation indicator is zoomed in to 1.33 times. To account for this, there is a certain &gt; distance between the navigation indicator's visible boundary and its actual boundary in the non-pressed state. &gt; The distance increases with the value of **itemWidth**, **itemHeight**, **selectedItemWidth**, and &gt; **selectedItemHeight**. &gt; &gt; - If there are too many pages and dot-style indicators exceed the page, you are advised to use the &gt; **maxDisplayCount** parameter to set the number of dots to be displayed.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DigitIndicator-constructor()--><!--Device-DigitIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## digitFont

```TypeScript
digitFont(value: Font): DigitIndicator
```

Sets the font style of the digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DigitIndicator-digitFont(value: Font): DigitIndicator--><!--Device-DigitIndicator-digitFont(value: Font): DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Font style of the digit-style navigation indicator.<br>Only the **size** and **weight** parameters in **Font** are adjustable. Setting **family** and **style** has no effect.<br>Default value:<br>{ size:?14,?weight:?FontWeight.Normal?} |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) | Current digit-style navigation indicator. |

## fontColor

```TypeScript
fontColor(value: ResourceColor): DigitIndicator
```

Sets the font color of the digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DigitIndicator-fontColor(value: ResourceColor): DigitIndicator--><!--Device-DigitIndicator-fontColor(value: ResourceColor): DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ResourceColor | Yes | Font color of the digit-style navigation indicator.<br>Default value: **'#ff182431' |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) | Current digit-style navigation indicator. |

## selectedDigitFont

```TypeScript
selectedDigitFont(value: Font): DigitIndicator
```

Sets the font style of the selected digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DigitIndicator-selectedDigitFont(value: Font): DigitIndicator--><!--Device-DigitIndicator-selectedDigitFont(value: Font): DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Font style of the selected digit-style navigation indicator.<br>Default value:<br>{?size:?1 4,?weight:?FontWeight.Normal?} |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) | Current digit-style navigation indicator. |

## selectedFontColor

```TypeScript
selectedFontColor(value: ResourceColor): DigitIndicator
```

Sets the font color of the selected digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DigitIndicator-selectedFontColor(value: ResourceColor): DigitIndicator--><!--Device-DigitIndicator-selectedFontColor(value: ResourceColor): DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ResourceColor | Yes | Font color of the selected digit-style navigation indicator.<br>Default value: **'#ff182431' |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) | Current digit-style navigation indicator. |

