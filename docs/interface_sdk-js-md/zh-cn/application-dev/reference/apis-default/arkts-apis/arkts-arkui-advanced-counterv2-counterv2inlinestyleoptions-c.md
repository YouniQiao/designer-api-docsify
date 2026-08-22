# CounterV2InlineStyleOptions

CounterV2InlineStyleOptions定义了数值内联型CounterV2的属性和事件。

继承于[CounterV2CommonOptions](arkts-arkui-advanced-counterv2-counterv2commonoptions-c.md)。

**继承/实现关系：** CounterV2InlineStyleOptions extends [CounterV2CommonOptions](arkts-arkui-advanced-counterv2-counterv2commonoptions-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-declare class CounterV2InlineStyleOptions--><!--Device-unnamed-declare class CounterV2InlineStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## max

```TypeScript
max?: int
```

设置CounterV2的最大值。 取值范围：(-∞, +∞)。默认值：999 值为undefined时，按默认值处理。

**类型：** int

**默认值：** 999

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2InlineStyleOptions-max?: int--><!--Device-CounterV2InlineStyleOptions-max?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: int
```

设置CounterV2的最小值。 取值范围：(-∞, +∞)。默认值：0 值为undefined时，按默认值处理。

**类型：** int

**默认值：** 0

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2InlineStyleOptions-min?: int--><!--Device-CounterV2InlineStyleOptions-min?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: OnInlineCounterV2Change
```

CounterV2的数值发生改变时触发该回调。

默认值：undefined，表示不触发该回调。

**类型：** [OnInlineCounterV2Change](arkts-oninlinecounterv2change-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2InlineStyleOptions-onChange?: OnInlineCounterV2Change--><!--Device-CounterV2InlineStyleOptions-onChange?: OnInlineCounterV2Change-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textWidth

```TypeScript
textWidth?: double
```

设置数值文本的宽度。 取值范围：[0, +∞)。默认值：undefined 单位：vp 不设置该属性或者设置为undefined时，文本宽度由内容自适应撑开。

**类型：** double

**默认值：** undefined

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2InlineStyleOptions-textWidth?: double--><!--Device-CounterV2InlineStyleOptions-textWidth?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: int
```

设置CounterV2的初始值。 取值范围：[min, max]。默认值：0 其中min和max分别对应下述CounterV2的最小值和最大值。

**类型：** int

**默认值：** 0

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2InlineStyleOptions-value?: int--><!--Device-CounterV2InlineStyleOptions-value?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

