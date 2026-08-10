# DotIndicator

Define DotIndicator, the indicator type is dot.

**Inheritance/Implementation:** DotIndicator extends [Indicator](../arkts-components/arkts-arkui-indicator-c.md/arkts-arkui-indicator-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class DotIndicator extends Indicator--><!--Device-unnamed-export declare class DotIndicator extends Indicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color(value: ResourceColor | undefined): this
```

Swiper组件圆点导航指示器的颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-color(value: ResourceColor | undefined): this--><!--Device-DotIndicator-color(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置Swiper组件圆点导航指示器的颜色。&lt;br/&gt;默认值：'#1A182431'，浅灰色。&lt;br/&gt;取值为undefined时，按默认值处 理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## constructor

```TypeScript
constructor()
```

DotIndicator的构造函数。

> **说明：**
> 
> - 按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、
> selectedItemHeight等参数变大而变大。
> 
> - 若页面数量较多、圆点导航点超出页面时，建议使用maxDisplayCount设置导航点显示个数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-constructor()--><!--Device-DotIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemHeight

```TypeScript
itemHeight(value: Length | undefined): this
```

Swiper组件圆点导航指示器的高。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-itemHeight(value: Length | undefined): this--><!--Device-DotIndicator-itemHeight(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置Swiper组件圆点导航指示器的高，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞)&lt;br/&gt;取值为 undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## itemWidth

```TypeScript
itemWidth(value: Length | undefined): this
```

Swiper组件圆点导航指示器的宽。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-itemWidth(value: Length | undefined): this--><!--Device-DotIndicator-itemWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置Swiper组件圆点导航指示器的宽，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞)&lt;br/&gt;取值为 undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mask

```TypeScript
mask(value: boolean | undefined): this
```

是否显示Swiper组件圆点导航指示器的蒙版样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-mask(value: boolean | undefined): this--><!--Device-DotIndicator-mask(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。&lt;br/&gt;true表示显示Swiper组件圆点导航指示器的蒙版样式；false表示不显示。&lt;br/ &gt;默认值：false&lt;br/&gt;取值为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## maxDisplayCount

```TypeScript
maxDisplayCount(maxDisplayCount: int | undefined): this
```

圆点导航点指示器样式下，导航点显示个数最大值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: int | undefined): this--><!--Device-DotIndicator-maxDisplayCount(maxDisplayCount: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxDisplayCount | int \| undefined | Yes | 设置圆点导航点指示器样式下，导航点显示个数最大值，当实际导航点个数大于最大导航点个数时，会生效超长效果样式，样式如 [示例5](../../../reference/apis-arkui/arkui-ts/ts-container-swiper copy.md#示例5设置圆点导航点超长显示)所示。&lt;br/&gt;取值范围：[6, 9]&lt;br /&gt;**说明：** &lt;br/&gt;1、超长显示场景，目前暂时不支持交互功能（包括：手指点击拖拽、鼠标操作等）。&lt;br/&gt;2、在超长显示场景下，中间页面对应的选中导航点的位置，并不是完全固定的，取决于之前的翻页操作序列。&lt;br/ &gt;3、当前仅支持displayCount为1的场景。&lt;br/&gt;取值为undefined时，等同于没有超长显示效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the DotIndicator |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

选中Swiper组件圆点导航指示器的颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-selectedColor(value: ResourceColor | undefined): this--><!--Device-DotIndicator-selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置选中Swiper组件圆点导航指示器的颜色。&lt;br/&gt;默认值：'#007DFF'，蓝色。&lt;br/&gt;取值为undefined时，按默认值处理 。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedItemHeight

```TypeScript
selectedItemHeight(value: Length | undefined): this
```

选中Swiper组件圆点导航指示器的高。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-selectedItemHeight(value: Length | undefined): this--><!--Device-DotIndicator-selectedItemHeight(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置选中Swiper组件圆点导航指示器的高，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞)&lt;br/&gt;取值为 undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedItemWidth

```TypeScript
selectedItemWidth(value: Length | undefined): this
```

选中Swiper组件圆点导航指示器的宽。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-selectedItemWidth(value: Length | undefined): this--><!--Device-DotIndicator-selectedItemWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置选中Swiper组件圆点导航指示器的宽，不支持设置百分比。&lt;br/&gt;默认值：6&lt;br/&gt;单位：vp&lt;br/&gt;取值范围：(0, +∞)&lt;br/&gt;取值为 undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## space

```TypeScript
space(space: LengthMetrics | undefined): this
```

设置Swiper圆点导航点间距。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DotIndicator-space(space: LengthMetrics | undefined): this--><!--Device-DotIndicator-space(space: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| space | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | 设置圆点导航点间距，不支持设置百分比。&lt;br/&gt;默认值：PC/2in1设备上为10，其他设备为8。&lt;br/&gt;单位：vp&lt;br/&gt;取值范围： [0, +∞)&lt;br/&gt;取值为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

