# CheckboxAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**Inheritance/Implementation:** CheckboxAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CheckboxAttribute extends CommonMethod--><!--Device-unnamed-export declare interface CheckboxAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置多选框的属性修改器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | 多选框的属性修改 器。当modifier的值为undefined时，不使用属性修改器。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this
```

定制CheckBox内容区的方法。与  
[contentModifier](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#contentmodifier12)相比，modifier参数新增了对undefined类型的支持。设置该属性时，会导致其他属性设置失效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this--><!--Device-CheckboxAttribute-default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;CheckBoxConfiguration&gt; \| undefined | Yes | 在CheckBox组件上，定制内容区的方法。&lt;br/&gt;modifier：内容修改 器，开发者需要自定义class实现ContentModifier接口。&lt;br/&gt;当modifier的值为undefined时，不使用内容修改器。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mark

```TypeScript
default mark(value: MarkStyle | undefined): this
```

设置多选框内部图标的样式。与[mark](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#mark10)相比，value参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default mark(value: MarkStyle | undefined): this--><!--Device-CheckboxAttribute-default mark(value: MarkStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MarkStyle](arkts-arkui-markstyle-i.md) \| undefined | Yes | 多选框内部图标样式。 从API version 12开始，设置了indicatorBuilder时，按照indicatorBuilder中的内容 显示。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：{&lt;br/&gt;strokeColor : `\\$r('sys.color.ohos_id_color_foreground_contrary')`,&lt;br/ &gt;strokeWidth: `\\$r('sys.float.ohos_id_checkbox_stroke_width')`,&lt;br/&gt;size: '20vp'&lt;br/&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnCheckboxChangeCallback | undefined): this
```

当选中状态发生变化时，触发该回调。与[onChange](arkts-arkui-checkbox-checkboxattribute-i.md#onchange)相比，callback参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default onChange(callback: OnCheckboxChangeCallback | undefined): this--><!--Device-CheckboxAttribute-default onChange(callback: OnCheckboxChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCheckboxChangeCallback](../arkts-components/arkts-arkui-oncheckboxchangecallback-t.md) \| undefined | Yes | 返回选中的状态。&lt;br/&gt;当callback的值为undefined时，不使用回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## select

```TypeScript
default select(isSelected: boolean | undefined | Bindable<boolean>): this
```

设置多选框选中状态。

从API version 23开始，该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)、  
[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default select(isSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxAttribute-default select(isSelected: boolean | undefined | Bindable<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSelected | boolean \| undefined \| Bindable&lt;boolean&gt; | Yes | 多选框是否选中。取值为undefined时，按默认值处理。&lt;br/&gt;true：多选框被选中； false：多选框未选中。&lt;br/&gt;默认值：false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置多选框选中状态颜色。与[selectedColor](arkts-arkui-checkbox-checkboxattribute-i.md#selectedcolor)相比，value参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 多选框选中状态颜色。&lt;br/&gt;当value的值为undefined时取默认值\\$r(' sys.color.ohos_id_color_text_primary_activated')。&lt;br/&gt;异常值按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## shape

```TypeScript
default shape(value: CheckBoxShape | undefined): this
```

设置CheckBox组件形状，包括圆形和圆角方形。如果想要调整当前CheckBox的样式，需使用  
[contentModifier](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#contentmodifier12)属性自定义CheckBox样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default shape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxAttribute-default shape(value: CheckBoxShape | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CheckBoxShape](arkts-arkui-checkboxshape-e.md) \| undefined | Yes | CheckBox组件形状，包括圆形和圆角方形。&lt;br/&gt;当value的值为undefined时，默认值为 CheckBoxShape.CIRCLE。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

设置多选框非选中状态的边框颜色。与  
[unselectedColor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-checkbox copy.md#unselectedcolor10)相比，value参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-default unselectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 多选框非选中状态边框颜色。&lt;br/&gt;当value的值为undefined时取默认值\\$r(' sys.color.ohos_id_color_switch_outline_off') |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

