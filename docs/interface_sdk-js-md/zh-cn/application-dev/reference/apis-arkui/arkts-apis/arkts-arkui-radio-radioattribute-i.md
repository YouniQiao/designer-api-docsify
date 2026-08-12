# RadioAttribute

除支持[通用属性](common)外，还支持以下属性：

**继承/实现关系：** RadioAttribute extends [CommonMethod](CommonMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface RadioAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RadioAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

定制Radio属性区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RadioAttribute-default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RadioAttribute-default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RadioAttribute](arkts-arkui-radio-radioattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | 在Radio组件上，定 制属性区的方法。&lt;br/&gt;RadioAttribute表示 [属性](../../../reference/apis-arkui/arkui-ts/ts-basic-components-radio.md#RadioAttribute)。&lt;br/&gt;CommonMethod表示 [通用属性](common)和[通用事件](common)。&lt;br/&gt;modifier：属性修改器，开发者需要自定义class实现AttributeModifier接口。&lt;br/&gt;当 modifier的值为undefined时，不使用属性修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## checked

```TypeScript
default checked(isChecked: boolean | undefined | Bindable<boolean>): this
```

设置单选框的选中状态。与[checked](checked)相比，isChecked参数新增了对undefined类型的支持。

该属性支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RadioAttribute-default checked(isChecked: boolean | undefined | Bindable<boolean>): this--><!--Device-RadioAttribute-default checked(isChecked: boolean | undefined | Bindable<boolean>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isChecked | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | 是 | 单选框的选中状态。&lt;br/&gt;默认值：false&lt;br/&gt;当isChecked的值为undefined 时取默认值false。&lt;br/&gt;值为true时，单选框被选中。值为false时，单选框不被选中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this
```

定制Radio内容区的方法。与  
[contentModifier](../../../reference/apis-arkui/arkui-ts/ts-basic-components-radio copy.md#contentmodifier12)&lt;sup&gt;12+&lt;/sup&gt;相比，modifier参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RadioAttribute-default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this--><!--Device-RadioAttribute-default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RadioConfiguration](arkts-arkui-radio-radioconfiguration-i.md)&gt; \| undefined | 是 | 在Radio组件上，定制内容区的方法。&lt;br/&gt;modifier：内容修改器，开发者需 要自定义class实现ContentModifier接口。&lt;br/&gt;当modifier的值为undefined时，不使用内容修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnRadioChangeCallback | undefined): this
```

单选框选中状态改变时触发的回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RadioAttribute-default onChange(callback: OnRadioChangeCallback | undefined): this--><!--Device-RadioAttribute-default onChange(callback: OnRadioChangeCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnRadioChangeCallback](arkts-arkui-onradiochangecallback-t.md) \| undefined | 是 | 单选框选中状态改变时触发该回调。&lt;br/&gt;当callback的值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## radioStyle

```TypeScript
default radioStyle(value?: RadioStyle | undefined): this
```

设置单选框选中状态和非选中状态的样式。 

从API version 10开始，该接口支持在ArkTS组件中使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RadioAttribute-default radioStyle(value?: RadioStyle | undefined): this--><!--Device-RadioAttribute-default radioStyle(value?: RadioStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RadioStyle](arkts-arkui-radio-radiostyle-i.md) \| undefined | 否 | 单选框选中状态和非选中状态的样式。 &lt;br/&gt; 未设置或设置undefined时，则按照RadioStyle中各参数的默认值配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

