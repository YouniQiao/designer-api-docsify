# RadioConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** RadioConfiguration extends [CommonConfiguration<RadioConfiguration>](CommonConfiguration<RadioConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RadioConfiguration extends CommonConfiguration<RadioConfiguration>--><!--Device-unnamed-export declare interface RadioConfiguration extends CommonConfiguration<RadioConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## checked

```TypeScript
checked: boolean
```

设置单选框的选中状态。

默认值：false

值为true时，单选框被选中。值为false时，单选框不被选中。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioConfiguration-checked: boolean--><!--Device-RadioConfiguration-checked: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<boolean>
```

触发单选框选中状态变化。

值为true时，表示从未选中变为选中。值为false时，表示从选中变为未选中。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioConfiguration-triggerChange: Callback<boolean>--><!--Device-RadioConfiguration-triggerChange: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: string
```

当前单选框的值。 

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioConfiguration-value: string--><!--Device-RadioConfiguration-value: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

