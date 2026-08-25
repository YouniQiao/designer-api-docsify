# CheckboxAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** CheckboxAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置多选框的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this
```

定制CheckBox内容区的方法。与 [contentModifier](#contentmodifier) 相比，modifier参数新增了对undefined类型的支持。设置该属性时，会导致其他属性设置失效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxConfiguration](arkts-arkui-checkbox-checkboxconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## mark

```TypeScript
default mark(value: MarkStyle | undefined): this
```

设置多选框内部图标的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MarkStyle](arkts-arkui-markstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnCheckboxChangeCallback | undefined): this
```

当选中状态发生变化时，触发该回调。与[onChange](#onchange)相比，callback参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnCheckboxChangeCallback](arkts-arkui-oncheckboxchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## select

```TypeScript
default select(isSelected: boolean | undefined | Bindable<boolean>): this
```

设置多选框选中状态。从API version 23开始，该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)、 [!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isSelected | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置多选框选中状态颜色。与[selectedColor](#selectedcolor)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## shape

```TypeScript
default shape(value: CheckBoxShape | undefined): this
```

设置CheckBox组件形状，包括圆形和圆角方形。如果想要调整当前CheckBox的样式，需使用 [contentModifier](#contentmodifier) 属性自定义CheckBox样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CheckBoxShape](arkts-arkui-checkboxshape-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

设置多选框非选中状态的边框颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md) |
