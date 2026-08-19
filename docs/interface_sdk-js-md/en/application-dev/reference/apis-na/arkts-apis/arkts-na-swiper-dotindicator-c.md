# DotIndicator

Define DotIndicator, the indicator type is dot.

**Inheritance/Implementation:** DotIndicator extends [Indicator](arkts-na-swiper-indicator-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class DotIndicator--><!--Device-unnamed-export declare class DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color(value: ResourceColor | undefined): this
```

Set the indicator color.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-color(value: ResourceColor | undefined): this--><!--Device-DotIndicator-color(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the indicator item color, default value is { #18243119 }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-constructor()--><!--Device-DotIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorIcon

```TypeScript
indicatorIcon(iconList: Array<IndicatorIconInfo> | undefined) : this
```

Set indicator icon.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-indicatorIcon(iconList: Array<IndicatorIconInfo> | undefined) : this--><!--Device-DotIndicator-indicatorIcon(iconList: Array<IndicatorIconInfo> | undefined) : this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iconList | Array&lt;[IndicatorIconInfo](arkts-na-swiper-indicatoriconinfo-i.md)&gt; \| undefined | Yes | indicator items need to be set icon. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) | return the DotIndicator. |

## itemHeight

```TypeScript
itemHeight(value: Length | undefined): this
```

Set the indicator item height.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-itemHeight(value: Length | undefined): this--><!--Device-DotIndicator-itemHeight(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator item height, default value is 6.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## itemWidth

```TypeScript
itemWidth(value: Length | undefined): this
```

Set the indicator item width.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-itemWidth(value: Length | undefined): this--><!--Device-DotIndicator-itemWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator item width, default value is 6.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## mask

```TypeScript
mask(value: boolean | undefined): this
```

Setting indicator style mask.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-mask(value: boolean | undefined): this--><!--Device-DotIndicator-mask(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | the indicator item mask, default value is false, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## maxDisplayCount

```TypeScript
maxDisplayCount(maxDisplayCount: int | undefined): this
```

Set the Indicator maxDisplayCount when selected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: int | undefined): this--><!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxDisplayCount | int \| undefined | Yes | the indicator item maxDisplayCount when selected, default value is 6, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) | return the DotIndicator |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

Set the navigation point color.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-selectedColor(value: ResourceColor | undefined): this--><!--Device-DotIndicator-selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the indicator item when selected, default value is { #007DFFFF }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## selectedItemHeight

```TypeScript
selectedItemHeight(value: Length | undefined): this
```

Set the indicator item height when selected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-selectedItemHeight(value: Length | undefined): this--><!--Device-DotIndicator-selectedItemHeight(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator item height when selected, default value is 6.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## selectedItemWidth

```TypeScript
selectedItemWidth(value: Length | undefined): this
```

Set the indicator item width when selected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-selectedItemWidth(value: Length | undefined): this--><!--Device-DotIndicator-selectedItemWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator item width when selected, default value is 6.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## space

```TypeScript
space(space: LengthMetrics | undefined): this
```

Set the space between dots.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-space(space: LengthMetrics | undefined): this--><!--Device-DotIndicator-space(space: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| space | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | the space between dots, default value is 8.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

