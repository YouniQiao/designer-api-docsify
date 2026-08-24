# CheckBoxGroupConfiguration

CheckBoxGroupConfiguration used by content modifier.@extends CommonConfiguration&lt;CheckBoxGroupConfiguration&gt; @interface CheckBoxGroupConfiguration

**Inheritance/Implementation:** CheckBoxGroupConfiguration extends CommonConfiguration<CheckBoxGroupConfiguration>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface CheckBoxGroupConfiguration--><!--Device-unnamed-export declare interface CheckBoxGroupConfiguration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange(isSelect: boolean): void
```

Trigger checkboxgroup select change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

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

Current name of checkboxgroup.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckBoxGroupConfiguration-name: string--><!--Device-CheckBoxGroupConfiguration-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status: SelectStatus
```

Defines the select status of CheckboxGroup.

**Type:** [SelectStatus](arkts-checkboxgroup-selectstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckBoxGroupConfiguration-status: SelectStatus--><!--Device-CheckBoxGroupConfiguration-status: SelectStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

