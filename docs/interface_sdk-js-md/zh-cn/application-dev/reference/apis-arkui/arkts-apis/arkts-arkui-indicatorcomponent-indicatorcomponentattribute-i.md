# IndicatorComponentAttribute

除支持通用属性外，还支持以下属性。

**继承/实现关系：** IndicatorComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count(totalCount: int | undefined): this
```

设置导航点总数量。单独导航点组件和Swiper绑定的时候，以Swiper的页面数量为准。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| totalCount | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |

## initialIndex

```TypeScript
initialIndex(index: int | undefined): this
```

设置首次显示时当前导航点的索引值。设置小于0或大于等于导航点数量时，按照默认值0处理。单独导航点组件和Swiper绑定的时候，该属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |

## loop

```TypeScript
loop(isLoop: boolean | undefined): this
```

设置是否开启循环。单独导航点组件和Swiper绑定的时候，该属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isLoop | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |

## onChange

```TypeScript
onChange(event: Callback<int> | undefined): this
```

当前显示的选中导航点索引变化时触发该事件，可通过回调函数获取当前选中导航点的索引值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |

## setIndicatorComponentOptions

```TypeScript
default setIndicatorComponentOptions(controller?: IndicatorComponentController): this
```

设置indicatorComponent组件配置项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | [IndicatorComponentController](arkts-arkui-indicatorcomponent-indicatorcomponentcontroller-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |

## style

```TypeScript
style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this
```

设置可选导航点指示器样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| indicatorStyle | [DotIndicator](../arkts-components/arkts-arkui-dotindicator-c.md) \| [DigitIndicator](../arkts-components/arkts-arkui-digitindicator-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |

## vertical

```TypeScript
vertical(isVertical: boolean | undefined): this
```

设置是否为纵向滑动。单独导航点组件和Swiper绑定的时候，该属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isVertical | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [IndicatorComponentAttribute](arkts-arkui-indicatorcomponent-indicatorcomponentattribute-i.md) |
