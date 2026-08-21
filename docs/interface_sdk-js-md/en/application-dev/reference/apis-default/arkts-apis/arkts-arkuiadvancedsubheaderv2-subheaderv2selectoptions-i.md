# SubHeaderV2SelectOptions

Defines the options for initializing a **SubHeaderV2Select** object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface SubHeaderV2SelectOptions--><!--Device-unnamed-export interface SubHeaderV2SelectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

Whether the drop-down button is the default focus.

**true**: The drop-down button is the default focus.

**false**: The drop-down button is not the default focus.

Default value: **false**

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2SelectOptions-defaultFocus?: boolean--><!--Device-SubHeaderV2SelectOptions-defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id?: string
```

Set the id for the SubHeaderV2SelectOptions.

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2SelectOptions-id?: string--><!--Device-SubHeaderV2SelectOptions-id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onSelect

```TypeScript
onSelect?: SubHeaderV2SelectOnSelect
```

Callback invoked when an item in the drop-down list box is selected.

Default value: **undefined**

**Type:** [SubHeaderV2SelectOnSelect](arkts-subheaderv2selectonselect-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2SelectOptions-onSelect?: SubHeaderV2SelectOnSelect--><!--Device-SubHeaderV2SelectOptions-onSelect?: SubHeaderV2SelectOnSelect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options: SelectOption[]
```

Options for the drop-down list box.

**Type:** SelectOption[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2SelectOptions-options: SelectOption[]--><!--Device-SubHeaderV2SelectOptions-options: SelectOption[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedContent

```TypeScript
selectedContent?: ResourceStr
```

Text content of the drop-down button. Default value: **''**. The Resource type is supported since API version 20.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2SelectOptions-selectedContent?: ResourceStr--><!--Device-SubHeaderV2SelectOptions-selectedContent?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
selectedIndex?: int
```

Index of the initially selected item in the drop-down list box.

The index of the first item is 0.

If this property is not set, the default value **-1** is used, indicating that no item is selected.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2SelectOptions-selectedIndex?: int--><!--Device-SubHeaderV2SelectOptions-selectedIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

