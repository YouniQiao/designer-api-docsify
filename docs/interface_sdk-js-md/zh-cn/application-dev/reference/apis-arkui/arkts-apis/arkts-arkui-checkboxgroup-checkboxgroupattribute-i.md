# CheckboxGroupAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** CheckboxGroupAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置CheckboxGroup的属性修饰器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## checkboxShape

```TypeScript
default checkboxShape(value: CheckBoxShape | undefined): this
```

设置CheckboxGroup组件形状，包括圆形和圆角方形。与 [checkboxShape](#checkboxshape) &lt;sup&gt;12+&lt;/sup&gt;相比，shape参数新增了对undefined类型的支持。

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
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this
```

设置CheckboxGroup的内容修饰器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxGroupConfiguration](arkts-arkui-checkboxgroup-checkboxgroupconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## mark

```TypeScript
default mark(value: MarkStyle | undefined): this
```

设置多选框内部图标样式。

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
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this
```

CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnCheckboxGroupChangeCallback](arkts-arkui-oncheckboxgroupchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## selectAll

```TypeScript
default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this
```

设置是否全选。若同组的Checkbox显式设置了select属性，则Checkbox的优先级高。在与带有缓存功能的组件（如List）配合使用时，未创建的Checkbox选中状态需由开发者控制。该属性支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isAllSelected | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置被选中或部分选中状态的颜色。与[selectedColor](#selectedcolor)相比，resColor参数新增了对undefined类型的支持。

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
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

设置非选中状态边框颜色。与 [unselectedColor](#unselectedcolor) &lt;sup&gt;10+&lt;/sup&gt;相比，resColor参数新增了对undefined类型的支持。

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
| [CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md) |
