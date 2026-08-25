# Radio属性/事件

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：

**继承/实现关系：** RadioAttribute extends CommonMethod<RadioAttribute>

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## checked

```TypeScript
checked(value: boolean)
```

设置单选框的选中状态。从API version 10开始，该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。从API version 18开始，该属性支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## checked

```TypeScript
checked(isChecked: Optional<boolean>)
```

设置单选框的选中状态。与[checked](#checked)相比，isChecked参数新增了对undefined类型的支持。该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)、 [!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isChecked | Optional & lt;boolean & gt; | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<RadioConfiguration>)
```

定制Radio内容区的方法。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | ContentModifier&lt;[RadioConfiguration](arkts-arkui-radioconfiguration-i.md)&gt; | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: Optional<ContentModifier<RadioConfiguration>>)
```

定制Radio内容区的方法。与 [contentModifier](#contentmodifier)&lt;sup&gt;12+&lt;/sup&gt;相比，modifier参数新增了对undefined类型的支持。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | Optional&lt;ContentModifier&lt;[RadioConfiguration](arkts-arkui-radioconfiguration-i.md)&gt;&gt; | 是 |

## onChange

```TypeScript
onChange(callback: (isChecked: boolean) => void)
```

单选框选中状态改变时触发的回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (isChecked: boolean) = & gt; void | 是 |

## onChange

```TypeScript
onChange(callback: Optional<OnRadioChangeCallback>)
```

单选框选中状态改变时触发的回调。与onChange相比，callback参数新增了对 undefined类型的支持。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional&lt;[OnRadioChangeCallback](arkts-arkui-onradiochangecallback-t.md)&gt; | 是 |

## radioStyle

```TypeScript
radioStyle(value?: RadioStyle)
```

设置单选框选中状态和非选中状态的样式。从API version 10开始，该接口支持在ArkTS组件中使用。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RadioStyle](arkts-arkui-radiostyle-i.md) | 否 |
