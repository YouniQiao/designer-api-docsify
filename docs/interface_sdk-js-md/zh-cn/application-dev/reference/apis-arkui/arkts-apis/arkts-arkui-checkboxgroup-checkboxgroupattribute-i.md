# CheckboxGroupAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**继承/实现关系：** CheckboxGroupAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface CheckboxGroupAttribute extends CommonMethod--><!--Device-unnamed-export declare interface CheckboxGroupAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置CheckboxGroup的属性修饰器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxGroupAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxGroupAttribute](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 | CheckboxGroup的属性修饰器。&lt;br/&gt;CheckboxGroupAttribute：当前组件的[属性](../arkts-components/arkts-arkui-checkboxgroup-attribute.md/arkts-arkui-checkboxgroup-attribute.md)&lt;br/&gt;CommonMethod： [通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## checkboxShape

```TypeScript
default checkboxShape(value: CheckBoxShape | undefined): this
```

设置CheckboxGroup组件形状，包括圆形和圆角方形。与  
[checkboxShape](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkboxgroup copy.md#checkboxshape12)&lt;sup&gt;12+&lt;/sup&gt;相比，shape参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default checkboxShape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxGroupAttribute-default checkboxShape(value: CheckBoxShape | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CheckBoxShape](arkts-arkui-checkboxshape-e.md) \| undefined | 是 | 设置CheckboxGroup组件形状，包括圆形和圆角方形。&lt;br/&gt;当shape的值为undefined时，默认值为 CheckBoxShape.CIRCLE。&lt;br /&gt;**说明：**&lt;br/&gt;CheckboxGroup组件将按照设置的形状显示。&lt;br/&gt;CheckboxGroup内所有未单独设置shape类型的Checkbox，其 形状将与CheckboxGroup保持一致。&lt;br/&gt;CheckboxGroup内已单独设置shape类型的Checkbox，其形状将优先于CheckboxGroup的设置，按照自身设置显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this
```

设置CheckboxGroup的内容修饰器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this--><!--Device-CheckboxGroupAttribute-default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;CheckBoxGroupConfiguration&gt; \| undefined | 是 | CheckboxGroup的内容修饰器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## mark

```TypeScript
default mark(value: MarkStyle | undefined): this
```

设置多选框内部图标样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default mark(value: MarkStyle | undefined): this--><!--Device-CheckboxGroupAttribute-default mark(value: MarkStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MarkStyle](arkts-arkui-markstyle-i.md) \| undefined | 是 | 多选框内部图标样式。&lt;br/&gt;当style的值为undefined时，维持上次取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this
```

CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this--><!--Device-CheckboxGroupAttribute-default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCheckboxGroupChangeCallback](arkts-arkui-oncheckboxgroupchangecallback-t.md) \| undefined | 是 | 多选框群组的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectAll

```TypeScript
default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this
```

设置是否全选。若同组的[Checkbox](arkts-arkui-checkbox-checkbox-f.md#checkbox)显式设置了select属性，则Checkbox的优先级高。

在与带有缓存功能的组件（如[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)）配合使用时，未创建的Checkbox选中状态需由开发者控制。

该属性支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxGroupAttribute-default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAllSelected | boolean \| undefined \| Bindable&lt;boolean&gt; | 是 | 是否全选。&lt;br/&gt;默认值：false&lt;br/&gt;值为true时，多选框群组将全部被选中；值为 false时，多选框群组将全部取消选中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置被选中或部分选中状态的颜色。与[selectedColor](arkts-arkui-checkboxgroup-checkboxgroupattribute-i.md#selectedcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 被选中或部分选中状态的颜色。&lt;br/&gt;当resColor的值为undefined时，默认值：\\$r(' sys.color.ohos_id_color_text_primary_activated')&lt;br/&gt;异常值按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

设置非选中状态边框颜色。与  
[unselectedColor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkboxgroup copy.md#unselectedcolor10)&lt;sup&gt;10+&lt;/sup&gt;相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-default unselectedColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 非选中状态边框颜色。&lt;br/&gt;当value的值为undefined时，默认值：\\$r(' sys.color.ohos_id_color_switch_outline_off')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

