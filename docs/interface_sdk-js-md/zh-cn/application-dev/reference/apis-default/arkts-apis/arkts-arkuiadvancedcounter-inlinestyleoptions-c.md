# InlineStyleOptions

InlineStyleOptions定义了数值内联型Counter的属性和事件。

继承于[CommonOptions](arkts-arkuiadvancedcounter-commonoptions-c.md)。

**继承/实现关系：** InlineStyleOptions extends [CommonOptions](arkts-arkuiadvancedcounter-commonoptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class InlineStyleOptions--><!--Device-unnamed-declare class InlineStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## max

```TypeScript
max?: int
```

设置Counter的最大值。 取值范围：(-∞, +∞)。默认值：999。

**类型：** int

**默认值：** 999

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InlineStyleOptions-max?: int--><!--Device-InlineStyleOptions-max?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: int
```

设置Counter的最小值。 取值范围：(-∞, +∞)。默认值：0。

**类型：** int

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InlineStyleOptions-min?: int--><!--Device-InlineStyleOptions-min?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: OnInlineCounterChange
```

当数值改变时，返回当前值。 value：当前显示的数值。 默认值：数值改变时，不返回值。

**类型：** [OnInlineCounterChange](arkts-oninlinecounterchange-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InlineStyleOptions-onChange?: OnInlineCounterChange--><!--Device-InlineStyleOptions-onChange?: OnInlineCounterChange-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textWidth

```TypeScript
textWidth?: double
```

设置数值文本的宽度。 取值范围：[0, +∞)。默认值：自适应文本宽度。

**类型：** double

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InlineStyleOptions-textWidth?: double--><!--Device-InlineStyleOptions-textWidth?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: int
```

设置Counter的初始值。 取值范围：[min, max]。默认值：0。

**类型：** int

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InlineStyleOptions-value?: int--><!--Device-InlineStyleOptions-value?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

