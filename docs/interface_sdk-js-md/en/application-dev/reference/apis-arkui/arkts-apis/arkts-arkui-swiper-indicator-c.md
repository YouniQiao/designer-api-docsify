# Indicator

Defines the indicator class.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Indicator--><!--Device-unnamed-export declare class Indicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom(value: Length | undefined): this
```

导航点底部相对于Swiper的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-bottom(value: Length | undefined): this--><!--Device-Indicator-bottom(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置导航点底部相对于Swiper的位置。&lt;br/&gt;未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上 ，位于底部，效果与设置bottom=0一致。&lt;br/&gt;设置为0时：按照0位置布局计算。&lt;br/&gt;优先级：低于top属性。&lt;br/&gt;取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bottom

```TypeScript
bottom(bottom: LengthMetrics | Length | undefined, ignoreSize: boolean): this
```

导航点底部相对于Swiper的位置，并可通过ignoreSize属性忽略导航点大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-bottom(bottom: LengthMetrics | Length | undefined, ignoreSize: boolean): this--><!--Device-Indicator-bottom(bottom: LengthMetrics | Length | undefined, ignoreSize: boolean): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bottom | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| Length \| undefined | Yes | 设置导航点底部相对于Swiper的位置。&lt;br/&gt;未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和 Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。&lt;br/&gt;设置为0时：按照0位置布局计算。&lt;br/&gt;优先级：低于top属性。&lt;br/&gt;取值范围：[0,Swiper高度-导航点区域高度]，超出该 范围时，取最近的边界值。 |
| ignoreSize | boolean | Yes | 设置是否忽略导航点本身大小，默认false。&lt;br/&gt;true表示可以将导航点更靠近Swiper底部；false表示忽略导航点本身大小。&lt;br/&gt;使用方法可以参考 [示例9演示导航点space与bottom](../../../reference/apis-arkui/arkui-ts/ts-container-swiper copy.md#示例9演示导航点space与bottom) 。&lt;br/&gt; 说明：[数字导航点](../arkts-components/arkts-arkui-digitindicator-c.md/arkts-arkui-digitindicator-c.md)ignoreSize属性，不生效的场景如下：&lt;br/&gt; ? 当 [vertical](SwiperAttribute.vertical) 设置为false，且bottom > 0。&lt;br/&gt; ? 当 [vertical](SwiperAttribute.vertical) 设置为true时：&lt;br/&gt;1、bottom > 0 时。&lt;br/&gt; 2、bottom设为undefined。 &lt;br/&gt; 3、 isSidebarMiddle设置为false时。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## digit

```TypeScript
static digit(): DigitIndicator
```

返回一个DigitIndicator对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-static digit(): DigitIndicator--><!--Device-Indicator-static digit(): DigitIndicator-End-->

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) | 数字指示器对象，用于设置Swiper组件的数字导航样式。 |

## dot

```TypeScript
static dot(): DotIndicator
```

返回一个DotIndicator对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-static dot(): DotIndicator--><!--Device-Indicator-static dot(): DotIndicator-End-->

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](../arkts-components/arkts-arkui-dotindicator-c.md) | 圆点指示器对象，用于设置Swiper组件的圆点导航样式。 |

## end

```TypeScript
end(value: LengthMetrics | undefined): this
```

在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-end(value: LengthMetrics | undefined): this--><!--Device-Indicator-end(value: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | 设置在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。&lt;br/&gt;默认值：0&lt;br/ &gt;单位：vp&lt;br/&gt;取值范围：[0, Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。&lt;br/&gt;取值为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## left

```TypeScript
left(value: Length | undefined): this
```

导航点左侧相对于Swiper的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-left(value: Length | undefined): this--><!--Device-Indicator-left(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置导航点左侧相对于Swiper的位置。&lt;br/&gt;未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行 居中对齐。&lt;br/&gt;设置为0时：按照0位置布局计算。&lt;br/&gt;优先级：高于right属性。&lt;br/&gt;取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## right

```TypeScript
right(value: Length | undefined): this
```

导航点右侧相对于Swiper的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-right(value: Length | undefined): this--><!--Device-Indicator-right(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置导航点右侧相对于Swiper的位置。&lt;br/&gt;未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行 居中对齐。&lt;br/&gt;设置为0时：按照0位置布局计算。&lt;br/&gt;优先级：低于left属性。&lt;br/&gt;取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围 时，取最近的边界值。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## start

```TypeScript
start(value: LengthMetrics | undefined): this
```

在[RTL](arkts-arkui-layoutdirection-e.md)模式下为导航点距离Swiper组件右边的距离，在  
[LTR](arkts-arkui-layoutdirection-e.md)模式下为导航点距离Swiper组件左边的距离。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-start(value: LengthMetrics | undefined): this--><!--Device-Indicator-start(value: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | 设置在RTL模式下为导航点距离Swiper组件右边的距离，在LTR模式下为导航点距离Swiper组件左边的距离。&lt;br/&gt;默认值：0&lt;br/ &gt;单位：vp&lt;br/&gt;取值范围：[0, Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。&lt;br/&gt;取值为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## top

```TypeScript
top(value: Length | undefined): this
```

导航点顶部相对于Swiper的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-top(value: Length | undefined): this--><!--Device-Indicator-top(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 设置导航点顶部相对于Swiper的位置。&lt;br/&gt;未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上 ，位于底部，效果与设置bottom=0一致。&lt;br/&gt;设置为0时：按照0位置布局计算。&lt;br/&gt;优先级：高于bottom属性。&lt;br/&gt;取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

