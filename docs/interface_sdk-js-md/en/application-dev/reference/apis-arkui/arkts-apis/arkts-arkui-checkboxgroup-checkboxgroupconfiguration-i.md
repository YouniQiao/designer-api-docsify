# CheckBoxGroupConfiguration

CheckboxGroup的内容修饰器配置对象，用于配置CheckboxGroup的内容和样式。

**Inheritance/Implementation:** CheckBoxGroupConfiguration extends [CommonConfiguration<CheckBoxGroupConfiguration>](CommonConfiguration<CheckBoxGroupConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CheckBoxGroupConfiguration extends CommonConfiguration<CheckBoxGroupConfiguration>--><!--Device-unnamed-export declare interface CheckBoxGroupConfiguration extends CommonConfiguration<CheckBoxGroupConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange(isSelect: boolean): void
```

触发多选框群组选中状态变化。true表示从部分选中或未选中变为全部选中，false表示从全部选中或部分选中变为全部未选中。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckBoxGroupConfiguration-triggerChange(isSelect: boolean): void--><!--Device-CheckBoxGroupConfiguration-triggerChange(isSelect: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSelect | boolean | Yes | Whether the checkbox group is selected. |

## name

```TypeScript
name: string
```

当前CheckboxGroup的群组名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckBoxGroupConfiguration-name: string--><!--Device-CheckBoxGroupConfiguration-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status: SelectStatus
```

CheckboxGroup的选中状态。

**Type:** [SelectStatus](../arkts-components/arkts-arkui-selectstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckBoxGroupConfiguration-status: SelectStatus--><!--Device-CheckBoxGroupConfiguration-status: SelectStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

