# DigitIndicator

A constructor used to create a **DigitIndicator** object. It inherits from [Indicator](arkts-arkui-indicator-c.md).

> **NOTE：**&gt;
> When pages are turned by group, the child nodes displayed in the digit-style navigation indicator do not count
> placeholder nodes.&gt;
> The maximum value of maxFontScale for the digit-style navigation indicator is
> **2**.&gt;
> The mirror display of the page number depends on the RTL status of the system.

**Inheritance/Implementation:** DigitIndicator extends Indicator<DigitIndicator>

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **DotIndicator** object.

> **NOTE：**&gt;
> - When pressed, the navigation indicator is zoomed in to 1.33 times. To account for this, there is a certain
> distance between the navigation indicator's visible boundary and its actual boundary in the non-pressed state.
> The distance increases with the value of **itemWidth**, **itemHeight**, **selectedItemWidth**, and
> **selectedItemHeight**.&gt;
> - If there are too many pages and dot-style indicators exceed the page, you are advised to use the
> **maxDisplayCount** parameter to set the number of dots to be displayed.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](../arkts-apis/arkts-arkui-arkui-uicontext-font-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) |

## fontColor

```TypeScript
fontColor(value: ResourceColor): DigitIndicator
```

Sets the font color of the digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) |

## selectedDigitFont

```TypeScript
selectedDigitFont(value: Font): DigitIndicator
```

Sets the font style of the selected digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](../arkts-apis/arkts-arkui-arkui-uicontext-font-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) |

## selectedFontColor

```TypeScript
selectedFontColor(value: ResourceColor): DigitIndicator
```

Sets the font color of the selected digit-style navigation indicator.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) |
