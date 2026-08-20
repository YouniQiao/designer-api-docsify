# SubHeaderV2Select

Defines the content and events for selection.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class SubHeaderV2Select--><!--Device-unnamed-export declare class SubHeaderV2Select-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(options: SubHeaderV2SelectOptions)
```

A constructor used to create a **SubHeaderV2SelectOptions** object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-public constructor(options: SubHeaderV2SelectOptions)--><!--Device-SubHeaderV2Select-public constructor(options: SubHeaderV2SelectOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SubHeaderV2SelectOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheaderv2-subheaderv2selectoptions-i.md) | Yes | Options of the drop-down list box. |

## defaultFocus

```TypeScript
@Trace
  public defaultFocus?: boolean
```

Whether the drop-down button is the default focus.

**true**: The drop-down button is the default focus.

**false**: The drop-down button is not the default focus.

Default value: **false**

Decorator: @Trace

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-@Trace  public defaultFocus?: boolean--><!--Device-SubHeaderV2Select-@Trace  public defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
@Trace
  public id?: string
```

Sets the id for SubHeaderV2SelectOptions.

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-@Trace  public id?: string--><!--Device-SubHeaderV2Select-@Trace  public id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onSelect

```TypeScript
@Trace
  public onSelect?: SubHeaderV2SelectOnSelect
```

Callback invoked when an item in the drop-down list box is selected.

Default value: **undefined**

Decorator: @Trace

**Type:** [SubHeaderV2SelectOnSelect](../../apis-arkui/arkts-apis/arkts-arkui-subheaderv2selectonselect-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-@Trace  public onSelect?: SubHeaderV2SelectOnSelect--><!--Device-SubHeaderV2Select-@Trace  public onSelect?: SubHeaderV2SelectOnSelect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Trace
  public options: SelectOption[]
```

Options for the drop-down list box.

Decorator: @Trace

**Type:** SelectOption[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-@Trace  public options: SelectOption[]--><!--Device-SubHeaderV2Select-@Trace  public options: SelectOption[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedContent

```TypeScript
@Trace
  public selectedContent?: ResourceStr
```

Text content of the drop-down button. Default value: **''**. The Resource type is supported since API version 20.

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-@Trace  public selectedContent?: ResourceStr--><!--Device-SubHeaderV2Select-@Trace  public selectedContent?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
@Trace
  public selectedIndex?: int
```

Index of the initially selected item in the drop-down list box.

The index of the first item is 0.

If this property is not set, the default value **-1** is used, indicating that no item is selected.

Decorator: @Trace

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Select-@Trace  public selectedIndex?: int--><!--Device-SubHeaderV2Select-@Trace  public selectedIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

