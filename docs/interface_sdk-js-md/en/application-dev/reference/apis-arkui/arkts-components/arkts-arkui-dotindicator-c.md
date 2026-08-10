# DotIndicator

构造圆点指示器的样式，继承自[Indicator](arkts-arkui-indicator-c.md)。

**Inheritance/Implementation:** DotIndicator extends [Indicator<DotIndicator>](Indicator<DotIndicator>)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class DotIndicator extends Indicator<DotIndicator>--><!--Device-unnamed-declare class DotIndicator extends Indicator<DotIndicator>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color(value: ResourceColor): DotIndicator
```

Swiper组件圆点导航指示器的颜色。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-color(value: ResourceColor): DotIndicator--><!--Device-DotIndicator-color(value: ResourceColor): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | 设置Swiper组件圆点导航指示器的颜色。&lt;br/&gt;默认值：'#1A182431'，浅灰色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## constructor

```TypeScript
constructor()
```

DotIndicator的构造函数。

> **说明：**

> - 按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、
> selectedItemHeight等参数变大而变大。
> 
> - 若页面数量较多、圆点导航点超出页面时，建议使用maxDisplayCount设置导航点显示个数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-constructor()--><!--Device-DotIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorIcon

```TypeScript
indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator
```

设置导航点图标。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-DotIndicator-indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator--><!--Device-DotIndicator-indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iconList | Array&lt;IndicatorIconInfo&gt; | Yes | 需要设置的导航点索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回DotIndicator。 |

## itemHeight

```TypeScript
itemHeight(value: Length): DotIndicator
```

Swiper组件圆点导航指示器的高。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-itemHeight(value: Length): DotIndicator--><!--Device-DotIndicator-itemHeight(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | 设置Swiper组件圆点导航指示器的高，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## itemWidth

```TypeScript
itemWidth(value: Length): DotIndicator
```

Swiper组件圆点导航指示器的宽。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-itemWidth(value: Length): DotIndicator--><!--Device-DotIndicator-itemWidth(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | 设置Swiper组件圆点导航指示器的宽，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## mask

```TypeScript
mask(value: boolean): DotIndicator
```

是否显示Swiper组件圆点导航指示器的蒙版样式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-mask(value: boolean): DotIndicator--><!--Device-DotIndicator-mask(value: boolean): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。为true时显示Swiper组件圆点导航指示器的蒙版样式，为false时不显示。&lt;br/&gt;默认值：false |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## maxDisplayCount

```TypeScript
maxDisplayCount(maxDisplayCount: number): DotIndicator
```

圆点导航点指示器样式下，导航点显示个数最大值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: number): DotIndicator--><!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: number): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxDisplayCount | number | Yes | 设置圆点导航点指示器样式下，导航点显示个数最大值，当实际导航点个数大于最大导航点个数时，会生效超长效果样式，样式如 [示例5](../../../reference/apis-arkui/arkui-ts/ts-container-swiper.md#示例5设置圆点导航点超长显示)所示。&lt;br/&gt;默认值：这个属性没有默认值，如果设置异 常值那等同于没有超长显示效果。&lt;br/&gt;取值范围：[6, 9]&lt;br/&gt;**说明：** &lt;br/&gt;1、超长显示场景，目前暂时不支持交互功能（包括：手指点击拖拽、鼠标操作等）。&lt;br/&gt;2、在超长显示场景下，中间页面对应的选 中导航点的位置，并不是完全固定的，取决于之前的翻页操作序列。&lt;br/&gt;3、当前仅支持displayCount为1的场景。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor): DotIndicator
```

选中Swiper组件圆点导航指示器的颜色。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-selectedColor(value: ResourceColor): DotIndicator--><!--Device-DotIndicator-selectedColor(value: ResourceColor): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | 设置选中Swiper组件圆点导航指示器的颜色。&lt;br/&gt;默认值：'#007DFF'，蓝色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## selectedItemHeight

```TypeScript
selectedItemHeight(value: Length): DotIndicator
```

选中Swiper组件圆点导航指示器的高。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-selectedItemHeight(value: Length): DotIndicator--><!--Device-DotIndicator-selectedItemHeight(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | 设置选中Swiper组件圆点导航指示器的高，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## selectedItemWidth

```TypeScript
selectedItemWidth(value: Length): DotIndicator
```

选中Swiper组件圆点导航指示器的宽。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-DotIndicator-selectedItemWidth(value: Length): DotIndicator--><!--Device-DotIndicator-selectedItemWidth(value: Length): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | 设置选中Swiper组件圆点导航指示器的宽，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

## space

```TypeScript
space(space: LengthMetrics): DotIndicator
```

设置Swiper圆点导航点间距。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-DotIndicator-space(space: LengthMetrics): DotIndicator--><!--Device-DotIndicator-space(space: LengthMetrics): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| space | [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md) | Yes | 设置圆点导航点间距，不支持设置百分比。&lt;br/&gt;默认值：PC/2in1设备上为10，其他设备为8。&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：[0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) | 返回当前圆点指示器，用于支持链式调用配置其他导航点属性。 |

