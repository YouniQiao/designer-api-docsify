# CheckboxGroup属性/事件

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：

**继承/实现关系：** CheckboxGroupAttribute extends CommonMethod<CheckboxGroupAttribute>

**起始版本：** 8

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## checkboxShape

```TypeScript
checkboxShape(value: CheckBoxShape)
```

设置CheckboxGroup组件形状，包括圆形和圆角方形。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CheckBoxShape](../arkts-apis/arkts-arkui-checkboxshape-e.md) | 是 |

## checkboxShape

```TypeScript
checkboxShape(shape: Optional<CheckBoxShape>)
```

设置CheckboxGroup组件形状，包括圆形和圆角方形。与[checkboxShape](#checkboxshape)&lt;sup&gt;12+&lt;/sup&gt;相比，shape参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shape | [Optional](arkts-arkui-optional-t.md)&lt;[CheckBoxShape](../arkts-apis/arkts-arkui-checkboxshape-e.md)&gt; | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: Optional<ContentModifier<CheckBoxGroupConfiguration>>)
```

定制CheckboxGroup内容区的方法。设置该属性时，其他属性设置会失效。

> **说明：**&gt;
> 该接口不支持在attributeModifier中调用。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxGroupConfiguration](arkts-arkui-checkboxgroupconfiguration-i.md)&gt;&gt; | 是 |

## mark

```TypeScript
mark(value: MarkStyle)
```

设置多选框内部图标样式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MarkStyle](../arkts-apis/arkts-arkui-markstyle-i.md) | 是 |

## mark

```TypeScript
mark(style: Optional<MarkStyle>)
```

设置多选框内部图标样式。与[mark](#mark)&lt;sup&gt;10+&lt;/sup&gt;相比，style参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[MarkStyle](../arkts-apis/arkts-arkui-markstyle-i.md)&gt; | 是 |

## onChange

```TypeScript
onChange(callback: OnCheckboxGroupChangeCallback)
```

CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。在与带有缓存功能的组件（如List）配合使用时，需注意未创建的Checkbox的选中状态对回调结果的影响。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnCheckboxGroupChangeCallback](arkts-arkui-oncheckboxgroupchangecallback-t.md) | 是 |

## onChange

```TypeScript
onChange(callback: Optional<OnCheckboxGroupChangeCallback>)
```

CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。与 [onChange](#onchange)相比，callback参数新增了对 undefined类型的支持。在与带有缓存功能的组件（如List）配合使用时，需注意未创建的Checkbox的选中状态对回调结果的影响。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnCheckboxGroupChangeCallback](arkts-arkui-oncheckboxgroupchangecallback-t.md)&gt; | 是 |

## selectAll

```TypeScript
selectAll(value: boolean)
```

设置是否全选。若同组的Checkbox显式设置了select属性，则Checkbox的优先级高。在与带有缓存功能的组件（如List）配合使用时，未创建的Checkbox选中状态需由开发者控制。从API version 10开始，该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。从API version 18开始，该属性支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## selectAll

```TypeScript
selectAll(isAllSelected: Optional<boolean>)
```

设置是否全选。若同组的Checkbox显式设置了select属性，则Checkbox的优先级高。与 [selectAll](#selectall)相比，isAllSelected参数新增了对undefined类型的支持。在与带有缓存功能的组件（如List）配合使用时，未创建的Checkbox选中状态需由开发者控制。该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)、 [!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isAllSelected | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

设置被选中或部分选中状态的颜色。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## selectedColor

```TypeScript
selectedColor(resColor: Optional<ResourceColor>)
```

设置被选中或部分选中状态的颜色。与[selectedColor](#selectedcolor)相比，resColor参数新增了对 undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | 是 |

## unselectedColor

```TypeScript
unselectedColor(value: ResourceColor)
```

设置非选中状态边框颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## unselectedColor

```TypeScript
unselectedColor(resColor: Optional<ResourceColor>)
```

设置非选中状态边框颜色。与[unselectedColor](#unselectedcolor)&lt;sup&gt;10+&lt;/sup&gt;相比， resColor参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | 是 |
