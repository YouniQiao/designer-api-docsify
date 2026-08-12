# CheckboxAttribute

除支持[通用属性](common)外，还支持以下属性：

**继承/实现关系：** CheckboxAttribute extends [CommonMethod](CommonMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface CheckboxAttribute extends CommonMethod--><!--Device-unnamed-export declare interface CheckboxAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置多选框的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | 多选框的属性修改 器。当modifier的值为undefined时，不使用属性修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this
```

定制CheckBox内容区的方法。与  
[contentModifier](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#contentmodifier12)相比，modifier参数新增了对undefined类型的支持。设置该属性时，会导致其他属性设置失效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this--><!--Device-CheckboxAttribute-default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxConfiguration](arkts-arkui-checkbox-checkboxconfiguration-i.md)&gt; \| undefined | 是 | 在CheckBox组件上，定制内容区的方法。&lt;br/&gt;modifier：内容修改 器，开发者需要自定义class实现ContentModifier接口。&lt;br/&gt;当modifier的值为undefined时，不使用内容修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## mark

```TypeScript
default mark(value: MarkStyle | undefined): this
```

设置多选框内部图标的样式。与[mark](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#mark10)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default mark(value: MarkStyle | undefined): this--><!--Device-CheckboxAttribute-default mark(value: MarkStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MarkStyle](arkts-arkui-markstyle-i.md) \| undefined | 是 | 多选框内部图标样式。 从API version 12开始，设置了indicatorBuilder时，按照indicatorBuilder中的内容 显示。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：{&lt;br/&gt;strokeColor : `\\$r('sys.color.ohos_id_color_foreground_contrary')`,&lt;br/ &gt;strokeWidth: `\\$r('sys.float.ohos_id_checkbox_stroke_width')`,&lt;br/&gt;size: '20vp'&lt;br/&gt;} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnCheckboxChangeCallback | undefined): this
```

当选中状态发生变化时，触发该回调。与[onChange](#onChange)相比，callback参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default onChange(callback: OnCheckboxChangeCallback | undefined): this--><!--Device-CheckboxAttribute-default onChange(callback: OnCheckboxChangeCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCheckboxChangeCallback](arkts-arkui-oncheckboxchangecallback-t.md) \| undefined | 是 | 返回选中的状态。&lt;br/&gt;当callback的值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## select

```TypeScript
default select(isSelected: boolean | undefined | Bindable<boolean>): this
```

设置多选框选中状态。

从API version 23开始，该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)、  
[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default select(isSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxAttribute-default select(isSelected: boolean | undefined | Bindable<boolean>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelected | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | 是 | 多选框是否选中。取值为undefined时，按默认值处理。&lt;br/&gt;true：多选框被选中； false：多选框未选中。&lt;br/&gt;默认值：false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置多选框选中状态颜色。与[selectedColor](#selectedColor)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 多选框选中状态颜色。&lt;br/&gt;当value的值为undefined时取默认值\\$r(' sys.color.ohos_id_color_text_primary_activated')。&lt;br/&gt;异常值按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## shape

```TypeScript
default shape(value: CheckBoxShape | undefined): this
```

设置CheckBox组件形状，包括圆形和圆角方形。如果想要调整当前CheckBox的样式，需使用  
[contentModifier](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#contentmodifier12)属性自定义CheckBox样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default shape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxAttribute-default shape(value: CheckBoxShape | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CheckBoxShape](arkts-arkui-checkboxshape-e.md) \| undefined | 是 | CheckBox组件形状，包括圆形和圆角方形。&lt;br/&gt;当value的值为undefined时，默认值为 CheckBoxShape.CIRCLE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

设置多选框非选中状态的边框颜色。与  
[unselectedColor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#unselectedcolor10)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxAttribute-default unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-default unselectedColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 多选框非选中状态边框颜色。&lt;br/&gt;当value的值为undefined时取默认值\\$r(' sys.color.ohos_id_color_switch_outline_off') |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

