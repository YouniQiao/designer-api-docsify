# DataPanelAttribute

除支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)外，还支持以下属性。

支持[通用事件](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md)。

**继承/实现关系：** DataPanelAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface DataPanelAttribute--><!--Device-unnamed-export declare interface DataPanelAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<DataPanelAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-attributeModifier(modifier: AttributeModifier<DataPanelAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-DataPanelAttribute-attributeModifier(modifier: AttributeModifier<DataPanelAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[DataPanelAttribute](arkts-datapanel-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## closeEffect

```TypeScript
closeEffect(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-closeEffect(value: boolean | undefined): this--><!--Device-DataPanelAttribute-closeEffect(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<DataPanelConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-contentModifier(modifier: ContentModifier<DataPanelConfiguration> | undefined): this--><!--Device-DataPanelAttribute-contentModifier(modifier: ContentModifier<DataPanelConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[DataPanelConfiguration](arkts-datapanel-datapanelconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setDataPanelOptions

```TypeScript
setDataPanelOptions(options: DataPanelOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-setDataPanelOptions(options: DataPanelOptions): this--><!--Device-DataPanelAttribute-setDataPanelOptions(options: DataPanelOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DataPanelOptions](arkts-datapanel-datapaneloptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## strokeWidth

```TypeScript
strokeWidth(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-strokeWidth(value: Length | undefined): this--><!--Device-DataPanelAttribute-strokeWidth(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## trackBackgroundColor

```TypeScript
trackBackgroundColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-trackBackgroundColor(value: ResourceColor | undefined): this--><!--Device-DataPanelAttribute-trackBackgroundColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## trackShadow

```TypeScript
trackShadow(value: DataPanelShadowOptions | undefined | null): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-trackShadow(value: DataPanelShadowOptions | undefined | null): this--><!--Device-DataPanelAttribute-trackShadow(value: DataPanelShadowOptions | undefined | null): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DataPanelShadowOptions](arkts-datapanel-datapanelshadowoptions-i.md) \| undefined \| null | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## valueColors

```TypeScript
valueColors(value: Array<ResourceColor | LinearGradient> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-DataPanelAttribute-valueColors(value: Array<ResourceColor | LinearGradient> | undefined): this--><!--Device-DataPanelAttribute-valueColors(value: Array<ResourceColor | LinearGradient> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array&lt;[ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-datapanel-lineargradient-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置DataPanel选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataPanelAttribute-default--><!--Device-DataPanelAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

