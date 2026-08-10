# IndicatorComponentAttribute

除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性。

**Inheritance/Implementation:** IndicatorComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IndicatorComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface IndicatorComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count(totalCount: int | undefined): this
```

设置导航点总数量。

单独导航点组件和Swiper绑定的时候，以Swiper的页面数量为准。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-count(totalCount: int | undefined): this--><!--Device-IndicatorComponentAttribute-count(totalCount: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalCount | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## initialIndex

```TypeScript
initialIndex(index: int | undefined): this
```

设置首次显示时当前导航点的索引值。设置小于0或大于等于导航点数量时，按照默认值0处理。

单独导航点组件和Swiper绑定的时候，该属性不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-initialIndex(index: int | undefined): this--><!--Device-IndicatorComponentAttribute-initialIndex(index: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## loop

```TypeScript
loop(isLoop: boolean | undefined): this
```

设置是否开启循环。

单独导航点组件和Swiper绑定的时候，该属性不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-loop(isLoop: boolean | undefined): this--><!--Device-IndicatorComponentAttribute-loop(isLoop: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLoop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
onChange(event: Callback<int> | undefined): this
```

当前显示的选中导航点索引变化时触发该事件，可通过回调函数获取当前选中导航点的索引值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-onChange(event: Callback<int> | undefined): this--><!--Device-IndicatorComponentAttribute-onChange(event: Callback<int> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setIndicatorComponentOptions

```TypeScript
default setIndicatorComponentOptions(controller?: IndicatorComponentController): this
```

设置indicatorComponent组件配置项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-default setIndicatorComponentOptions(controller?: IndicatorComponentController): this--><!--Device-IndicatorComponentAttribute-default setIndicatorComponentOptions(controller?: IndicatorComponentController): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [IndicatorComponentController](../arkts-components/arkts-arkui-indicatorcomponentcontroller-c.md) | No | IndicatorComponent构造函数选项 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回IndicatorComponentAttribute的实例。 |

## style

```TypeScript
style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this
```

设置可选导航点指示器样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this--><!--Device-IndicatorComponentAttribute-style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indicatorStyle | [DotIndicator](../arkts-components/arkts-arkui-dotindicator-c.md) \| DigitIndicator \| undefined | Yes | 可选导航点指示器样式。&lt;br/&gt; - DotIndicator：圆点指示器样式。&lt;br/&gt; - DigitIndicator：数字指示器样式。&lt;br/&gt;  默认类型：DotIndicator。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## vertical

```TypeScript
vertical(isVertical: boolean | undefined): this
```

设置是否为纵向滑动。

单独导航点组件和Swiper绑定的时候，该属性不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-vertical(isVertical: boolean | undefined): this--><!--Device-IndicatorComponentAttribute-vertical(isVertical: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isVertical | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

