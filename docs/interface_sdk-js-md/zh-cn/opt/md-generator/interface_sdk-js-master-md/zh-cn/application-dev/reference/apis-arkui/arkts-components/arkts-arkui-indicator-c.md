# Indicator

设置导航点与Swiper组件的距离。由于导航点有默认交互区域，交互区域高度为32vp，所以无法让显示部分完全贴底。若想实现完全贴底，可以使用  
[IndicatorComponent](../../../reference/apis-arkui/arkui-ts/ts-swiper-components-indicator.md#indicatorcomponent)组件，更灵活地调整位置。

**起始版本：** 10

<!--Device-unnamed-declare class Indicator<T>--><!--Device-unnamed-declare class Indicator<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom(value: Length): T
```

导航点底部相对于Swiper的位置。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-bottom(value: Length): T--><!--Device-Indicator-bottom(value: Length): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## bottom

```TypeScript
bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T
```

导航点底部相对于Swiper的位置，并可通过ignoreSize属性忽略导航点大小。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本19开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T--><!--Device-Indicator-bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [bottom](#bottom) | [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md) \| [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |
| ignoreSize | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## digit

```TypeScript
static digit(): DigitIndicator
```

返回一个DigitIndicator对象。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-static digit(): DigitIndicator--><!--Device-Indicator-static digit(): DigitIndicator-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) |

## dot

```TypeScript
static dot(): DotIndicator
```

返回一个DotIndicator对象。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-static dot(): DotIndicator--><!--Device-Indicator-static dot(): DotIndicator-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## end

```TypeScript
end(value: LengthMetrics): T
```

在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-end(value: LengthMetrics): T--><!--Device-Indicator-end(value: LengthMetrics): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## left

```TypeScript
left(value: Length): T
```

导航点左侧相对于Swiper的位置。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-left(value: Length): T--><!--Device-Indicator-left(value: Length): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## right

```TypeScript
right(value: Length): T
```

导航点右侧相对于Swiper的位置。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-right(value: Length): T--><!--Device-Indicator-right(value: Length): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## start

```TypeScript
start(value: LengthMetrics): T
```

在[RTL](../arkts-apis/arkts-arkui-layoutdirection-e.md/arkts-arkui-layoutdirection-e.md)模式下为导航点距离Swiper组件右边的距离，在[LTR](../arkts-apis/arkts-arkui-layoutdirection-e.md/arkts-arkui-layoutdirection-e.md)模式下为导航点距离Swiper组件左边的距离。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-start(value: LengthMetrics): T--><!--Device-Indicator-start(value: LengthMetrics): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## top

```TypeScript
top(value: Length): T
```

导航点顶部相对于Swiper的位置。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-Indicator-top(value: Length): T--><!--Device-Indicator-top(value: Length): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |
