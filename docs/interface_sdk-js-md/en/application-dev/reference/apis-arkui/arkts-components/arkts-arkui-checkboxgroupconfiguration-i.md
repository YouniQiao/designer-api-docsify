# CheckBoxGroupConfiguration

开发者必须自定义此类以实现ContentModifier接口，使用方法见[contentModifier](CheckboxGroupAttribute#contentModifier)。

**Inheritance/Implementation:** CheckBoxGroupConfiguration extends [CommonConfiguration<CheckBoxGroupConfiguration>](CommonConfiguration<CheckBoxGroupConfiguration>)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-unnamed-declare interface CheckBoxGroupConfiguration extends CommonConfiguration<CheckBoxGroupConfiguration>--><!--Device-unnamed-declare interface CheckBoxGroupConfiguration extends CommonConfiguration<CheckBoxGroupConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

当前多选框群组名称，用于标识和关联Checkbox与CheckboxGroup，与Checkbox的group属性值相同时属于同一群组。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CheckBoxGroupConfiguration-name: string--><!--Device-CheckBoxGroupConfiguration-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status: SelectStatus
```

表示多选框群组的选中状态。

**Type:** [SelectStatus](arkts-arkui-selectstatus-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CheckBoxGroupConfiguration-status: SelectStatus--><!--Device-CheckBoxGroupConfiguration-status: SelectStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<boolean>
```

触发多选框群组选中状态变化。true表示从部分选中或未选中变为全部选中，false表示从全部选中或部分选中变为全部未选中。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CheckBoxGroupConfiguration-triggerChange: Callback<boolean>--><!--Device-CheckBoxGroupConfiguration-triggerChange: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

