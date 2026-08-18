# SubHeaderV2Select

Defines the content and events for selection.

**Since:** 18

<!--Device-unnamed-export declare class SubHeaderV2Select--><!--Device-unnamed-export declare class SubHeaderV2Select-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: SubHeaderV2SelectOptions)
```

A constructor used to create a **SubHeaderV2SelectOptions** object.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Select-constructor(options: SubHeaderV2SelectOptions)--><!--Device-SubHeaderV2Select-constructor(options: SubHeaderV2SelectOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [options](#options) | [SubHeaderV2SelectOptions](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2selectoptions-i.md) | Yes |

## defaultFocus

```TypeScript
@Trace
  defaultFocus?: boolean
```

Whether the drop-down button is the default focus. **true**: The drop-down button is the default focus. **false**: The drop-down button is not the default focus. Default value: **false** Decorator: @Trace

**Type:** boolean

**Default:** false

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Select-@Trace  defaultFocus?: boolean--><!--Device-SubHeaderV2Select-@Trace  defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
@Trace
  id?: string
```

Set the id for the SubHeaderV2Select.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-SubHeaderV2Select-@Trace  id?: string--><!--Device-SubHeaderV2Select-@Trace  id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onSelect

```TypeScript
@Trace
  onSelect?: SubHeaderV2SelectOnSelect
```

Sets the onSelect of the SubHeaderV2SelectOptions.

**Type:** [SubHeaderV2SelectOnSelect](arkts-arkui-subheaderv2selectonselect-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Select-@Trace  onSelect?: SubHeaderV2SelectOnSelect--><!--Device-SubHeaderV2Select-@Trace  onSelect?: SubHeaderV2SelectOnSelect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Trace
  options: SelectOption[]
```

Sets the options of the SubHeaderV2SelectOptions.

**Type:** SelectOption[]

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Select-@Trace  options: SelectOption[]--><!--Device-SubHeaderV2Select-@Trace  options: SelectOption[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedContent

```TypeScript
@Trace
  selectedContent?: ResourceStr
```

Sets the selected content of the SubHeaderV2SelectOptions.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Select-@Trace  selectedContent?: ResourceStr--><!--Device-SubHeaderV2Select-@Trace  selectedContent?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
@Trace
  selectedIndex?: number
```

Sets the selected index of the SubHeaderV2SelectOptions.

**Type:** number

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Select-@Trace  selectedIndex?: number--><!--Device-SubHeaderV2Select-@Trace  selectedIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
