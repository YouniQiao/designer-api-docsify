# DotIndicator

A constructor used to create a **DotIndicator** object. It inherits from [Indicator](arkts-arkui-indicator-c.md#Indicator).

**Inheritance/Implementation:** DotIndicator extends Indicator<DotIndicator>

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare class DotIndicator--><!--Device-unnamed-declare class DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color(value: ResourceColor): DotIndicator
```

Sets the color of the dot-style navigation indicator.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-color(value: ResourceColor): DotIndicator--><!--Device-DotIndicator-color(value: ResourceColor): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **DotIndicator** object. > **NOTE：**> > - When pressed, the navigation indicator is zoomed in to 1.33 times. To account for this, there is a certain > distance between the navigation indicator's visible boundary and its actual boundary in the non-pressed state. > The distance increases with the value of **itemWidth**, **itemHeight**, **selectedItemWidth**, and > **selectedItemHeight**. > > - If there are too many pages and dot-style indicators exceed the page, you are advised to use the > **maxDisplayCount** parameter to set the number of dots to be displayed.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-constructor()--><!--Device-DotIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorIcon

```TypeScript
indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator
```

Set indicator icon.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-DotIndicator-indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator--><!--Device-DotIndicator-indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iconList | Array&lt;[IndicatorIconInfo](arkts-arkui-indicatoriconinfo-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## itemHeight

```TypeScript
itemHeight(value: Length): DotIndicator
```

Sets the height of a dot-style navigation indicator of the **Swiper** component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-itemHeight(value: Length): DotIndicator--><!--Device-DotIndicator-itemHeight(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## itemWidth

```TypeScript
itemWidth(value: Length): DotIndicator
```

Sets the width of a dot-style navigation indicator of the **Swiper** component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-itemWidth(value: Length): DotIndicator--><!--Device-DotIndicator-itemWidth(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## mask

```TypeScript
mask(value: boolean): DotIndicator
```

Sets whether to enable the mask for the dot-style navigation indicator.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-mask(value: boolean): DotIndicator--><!--Device-DotIndicator-mask(value: boolean): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## maxDisplayCount

```TypeScript
maxDisplayCount(maxDisplayCount: number): DotIndicator
```

Sets the maximum number of navigation dots in the dot-style navigation indicator.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: number): DotIndicator--><!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: number): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [maxDisplayCount](#maxDisplayCount) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor): DotIndicator
```

Sets the color of the selected dot-style navigation indicator.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-selectedColor(value: ResourceColor): DotIndicator--><!--Device-DotIndicator-selectedColor(value: ResourceColor): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## selectedItemHeight

```TypeScript
selectedItemHeight(value: Length): DotIndicator
```

Sets the height of the selected dot-style navigation indicator.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-selectedItemHeight(value: Length): DotIndicator--><!--Device-DotIndicator-selectedItemHeight(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## selectedItemWidth

```TypeScript
selectedItemWidth(value: Length): DotIndicator
```

Sets the width of the selected dot-style navigation indicator.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-selectedItemWidth(value: Length): DotIndicator--><!--Device-DotIndicator-selectedItemWidth(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## space

```TypeScript
space(space: LengthMetrics): DotIndicator
```

Sets the spacing between dot-style navigation indicators of the **Swiper** component.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-DotIndicator-space(space: LengthMetrics): DotIndicator--><!--Device-DotIndicator-space(space: LengthMetrics): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [space](#space) | [LengthMetrics](../../apis-na/arkts-apis/arkts-na-lengthmetrics-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |
