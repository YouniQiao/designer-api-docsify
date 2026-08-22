# LazyVGridLayoutAttribute

除支持通用属性外，还支持以下属性：

## columnsGap

default columnsGap(value: LengthMetrics | undefined): this

设置列与列的间距。设置为小于0的值时，按默认值显示。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 19开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 | | ------ | ---------------------------- | ---- | ---------------------------- | | value | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 | 列与列的间距。<br/>默认值：0vp<br/>取值为undefined时，按默认值处理。 |

## rowsGap

default rowsGap(value: LengthMetrics | undefined): this

设置行与行的间距。设置为小于0的值时，按默认值显示。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 19开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 | | ------ | ---------------------------- | ---- | ---------------------------- | | value | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 | 行与行的间距。<br/>默认值：0vp<br/>取值为undefined时，按默认值处理。 |

**继承/实现关系：** LazyVGridLayoutAttribute extends [LazyGridLayoutAttribute](arkts-lazygridlayout-lazygridlayoutattribute-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface LazyVGridLayoutAttribute--><!--Device-unnamed-export declare interface LazyVGridLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<LazyVGridLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-LazyVGridLayoutAttribute-attributeModifier(modifier: AttributeModifier<LazyVGridLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LazyVGridLayoutAttribute-attributeModifier(modifier: AttributeModifier<LazyVGridLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LazyVGridLayoutAttribute](arkts-lazyvgridlayout-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnsTemplate

```TypeScript
columnsTemplate(value: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-LazyVGridLayoutAttribute-columnsTemplate(value: string | undefined): this--><!--Device-LazyVGridLayoutAttribute-columnsTemplate(value: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setLazyVGridLayoutOptions

```TypeScript
setLazyVGridLayoutOptions(): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-LazyVGridLayoutAttribute-setLazyVGridLayoutOptions(): this--><!--Device-LazyVGridLayoutAttribute-setLazyVGridLayoutOptions(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置LazyVGridLayout组件的属性方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyVGridLayoutAttribute-default--><!--Device-LazyVGridLayoutAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

