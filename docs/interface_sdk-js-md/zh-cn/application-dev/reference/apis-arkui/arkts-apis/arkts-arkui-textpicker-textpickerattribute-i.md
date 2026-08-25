# TextPickerAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** TextPickerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## canLoop

```TypeScript
default canLoop(value: boolean | undefined): this
```

设置是否可循环滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## defaultPickerItemHeight

```TypeScript
default defaultPickerItemHeight(value: double | string | undefined): this
```

设置选择项的高度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## defaultTextStyle

```TypeScript
default defaultTextStyle(style: TextPickerTextStyle | undefined): this
```

设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。 仅当disableTextStyleAnimation为true时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

设置表冠灵敏度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## disableTextStyleAnimation

```TypeScript
default disableTextStyleAnimation(disabled: boolean | undefined): this
```

设置滑动过程中是否有文本样式变化动效。设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为 defaultTextStyle属性设置样式。如未设置 defaultTextStyle，则显示为Text组件默认样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| disabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## disappearTextStyle

```TypeScript
default disappearTextStyle(value: PickerTextStyle | TextPickerTextStyle | undefined): this
```

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## divider

```TypeScript
default divider(value: DividerOptions | null | undefined): this
```

设置分割线样式，不设置该属性则按“默认值”展示分割线。  
[DividerOptions](arkts-arkui-textpicker-divideroptions-i.md)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DividerOptions](arkts-arkui-textpicker-divideroptions-i.md) \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): this
```

设置是否开启触控反馈。

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
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## gradientHeight

```TypeScript
default gradientHeight(value: Dimension | undefined): this
```

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnTextPickerChangeCallback | undefined): this
```

滑动TextPicker文本内容后，选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。当显示文本或图片加文本列表时， selectItem值为选中项中的文本值，当显示图片列表时，selectItem值为空。回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea] (../../../reference/apis-arkui/arkui-ts/ts-basic-components-textpicker.md#onenterselectedarea18)接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnTextPickerChangeCallback](arkts-arkui-ontextpickerchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## onEnterSelectedArea

```TypeScript
default onEnterSelectedArea(callback: TextPickerEnterSelectedAreaCallback | undefined): this
```

滑动TextPicker过程中，选项进入分割线区域内（当前列的滑动距离超过选中项高度的一半）时，触发该回调。

> **说明：**&gt;
> - 与onChange事件的差别在于，该事件的触发时机早于onChange事件。&gt;
> - 在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑
> 动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。&gt;
> - 该接口不支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TextPickerEnterSelectedAreaCallback](arkts-arkui-textpickerenterselectedareacallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## onScrollStop

```TypeScript
default onScrollStop(callback: TextPickerScrollStopCallback | undefined): this
```

文本选择器的选项列滑动停止时触发该事件。手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TextPickerScrollStopCallback](arkts-arkui-textpickerscrollstopcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## selectedBackgroundStyle

```TypeScript
default selectedBackgroundStyle(style: PickerBackgroundStyle | undefined): this
```

设置选中项的背景样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [PickerBackgroundStyle](arkts-arkui-textpicker-pickerbackgroundstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## selectedIndex

```TypeScript
default selectedIndex(value: int | int[] | undefined): this
```

设置默认选中项在数组中的索引值，优先级高于[TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md)中的选中值。单列数据选择器 使用int类型。多列、多列联动数据选择器使用int[]类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| int[] \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## selectedTextStyle

```TypeScript
default selectedTextStyle(value: PickerTextStyle | TextPickerTextStyle | undefined): this
```

设置选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。Wearable设备不支持设置该属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## textStyle

```TypeScript
default textStyle(value: PickerTextStyle | TextPickerTextStyle | undefined): this
```

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |
