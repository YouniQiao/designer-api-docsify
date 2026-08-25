# RadioAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** RadioAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

定制Radio属性区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RadioAttribute](arkts-arkui-radio-radioattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RadioAttribute](arkts-arkui-radio-radioattribute-i.md) |

## checked

```TypeScript
default checked(isChecked: boolean | undefined | Bindable<boolean>): this
```

设置单选框的选中状态。与checked相比，isChecked参数新增了对undefined类型的支持。该属性支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isChecked | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RadioAttribute](arkts-arkui-radio-radioattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this
```

定制Radio内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RadioConfiguration](arkts-arkui-radio-radioconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RadioAttribute](arkts-arkui-radio-radioattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnRadioChangeCallback | undefined): this
```

单选框选中状态改变时触发的回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnRadioChangeCallback](arkts-arkui-onradiochangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RadioAttribute](arkts-arkui-radio-radioattribute-i.md) |

## radioStyle

```TypeScript
default radioStyle(value?: RadioStyle | undefined): this
```

设置单选框选中状态和非选中状态的样式。从API version 10开始，该接口支持在ArkTS组件中使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RadioStyle](arkts-arkui-radio-radiostyle-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [RadioAttribute](arkts-arkui-radio-radioattribute-i.md) |
