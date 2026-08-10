# CheckBoxConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](../arkts-apis/arkts-arkui-common-commonconfiguration-i.md/arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** CheckBoxConfiguration extends [CommonConfiguration<CheckBoxConfiguration>](CommonConfiguration<CheckBoxConfiguration>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface CheckBoxConfiguration extends CommonConfiguration<CheckBoxConfiguration>--><!--Device-unnamed-declare interface CheckBoxConfiguration extends CommonConfiguration<CheckBoxConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

当前多选框名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CheckBoxConfiguration-name: string--><!--Device-CheckBoxConfiguration-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected: boolean
```

指示多选框是否被选中，值为true时，多选框被选中。值为false时，多选框未选中。&lt;/br&gt;如果select属性没有设置默认值是false。&lt;/br&gt;如果设置select属性，此值与设置select属性的值相同。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CheckBoxConfiguration-selected: boolean--><!--Device-CheckBoxConfiguration-selected: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<boolean>
```

触发多选框选中状态变化的回调函数。调用时传入true，多选框被设置为选中状态；传入false，多选框被设置为未选中状态。

**Type:** [Callback](arkts-arkui-callback-i.md)&lt;boolean&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CheckBoxConfiguration-triggerChange: Callback<boolean>--><!--Device-CheckBoxConfiguration-triggerChange: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

