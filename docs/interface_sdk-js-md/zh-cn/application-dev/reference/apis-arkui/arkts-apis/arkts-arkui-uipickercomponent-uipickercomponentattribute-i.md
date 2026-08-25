# UIPickerComponentAttribute

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface UIPickerComponentAttribute

**继承/实现关系：** UIPickerComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## canLoop

```TypeScript
default canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute
```

设置选项列是否可循环滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isLoop | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## displayedItemCount

```TypeScript
default displayedItemCount(count: int | undefined): this
```

设置UIPickerComponent容器可见选项的数量。未通过该接口设置时，可见选项的数量为7行。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute
```

设置是否开启触控反馈。开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## itemHeight

```TypeScript
default itemHeight(height: LengthMetrics | undefined): this
```

设置UIPickerComponent容器每个选项的高度。未通过该接口设置时，每个选项的高度为40vp。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| height | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

滑动选择器选项时，若选中项发生变化，触发该事件。

> **说明：**&gt;
> 如果某个选项有一半以上的区域进入选中项区域内，则该选项成为选中项。&gt;
> 选中项区域可通过设置[selectionIndicator](#selectionindicator)进行标识。如果设置选中项指示器为背景，则背景区域即为
> 选中项区域。如果设置选中项指示器为分割线，则上下分割线的中心线内的区域为选中项区域。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## onScrollStop

```TypeScript
default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

选择器滑动停止时，触发该事件。选择器滑动停止指某次行为触发的滑动动画完全结束。如果某次滑动动画还未结束时又触发了新的滑动动画， 则不属于滑动停止。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |

## selectionIndicator

```TypeScript
default selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute
```

设置选中项指示器的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [PickerIndicatorStyle](arkts-arkui-uipickercomponent-pickerindicatorstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |
