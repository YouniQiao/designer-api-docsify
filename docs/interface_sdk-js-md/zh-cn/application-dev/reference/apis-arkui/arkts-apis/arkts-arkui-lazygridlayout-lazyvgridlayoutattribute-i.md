# LazyVGridLayoutAttribute

除支持通用属性外，还支持以下属性：

## columnsGap

default columnsGap(value: LengthMetrics | undefined): this设置列与列的间距。设置为小于0的值时，按默认值显示。  
**原子化服务API（仅ArkTS-Dyn）：** 从API version 19开始，该接口支持在原子化服务中使用。  
**系统能力：** SystemCapability.ArkUI.ArkUI.Full  
**参数：**  
| 参数名 | 类型 | 必填 | 说明 | | ------ | ---------------------------- | ---- | ---------------------------- | | value | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

## rowsGap

default rowsGap(value: LengthMetrics | undefined): this设置行与行的间距。设置为小于0的值时，按默认值显示。  
**原子化服务API（仅ArkTS-Dyn）：** 从API version 19开始，该接口支持在原子化服务中使用。  
**系统能力：** SystemCapability.ArkUI.ArkUI.Full  
**参数：**  
| 参数名 | 类型 | 必填 | 说明 | | ------ | ---------------------------- | ---- | ---------------------------- | | value | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**继承/实现关系：** LazyVGridLayoutAttribute extends [LazyGridLayoutAttribute](arkts-arkui-lazygridlayout-lazygridlayoutattribute-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LazyVGridLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置LazyVGridLayout组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## columnsTemplate

```TypeScript
default columnsTemplate(value: string | undefined): this
```

设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。例如，'1fr&nbsp;1fr&nbsp;2fr'&nbsp;是将父组件分3列，将父组件允许的宽分为4等份，第一列占1份，第二列占1份，第三列占2份。columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用columnsGap为最小列间距，自动计算列数和实际列间距。其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包含一个有效列宽。auto-fit模式和auto-stretch模式只支持track-size为一个有效列宽值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有 效列宽，如columnsTemplate('repeat(auto-fill, 20)')、columnsTemplate('repeat(auto-fill, 20 80px)')。设置为'0fr'时，该列的列宽为0，不显示子组件。设置为其他非法值时，子组件显示为固定1列。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setLazyVGridLayoutOptions

```TypeScript
default setLazyVGridLayoutOptions(): this
```

设置LazyVGrid选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md) |
