# SelectOptions

Declare type SelectOption

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class SelectOptions--><!--Device-unnamed-export declare class SelectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## defaultFocus

```TypeScript
public defaultFocus?: boolean
```

Whether the drop-down button is the default focus.  
**true**: The drop-down button is the default focus.  
**false**: The drop-down button is not the default focus.Default value: **false**

**Type:** boolean

**Default:** { false }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectOptions-public defaultFocus?: boolean--><!--Device-SelectOptions-public defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
public id?: string
```

Set the id for select.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectOptions-public id?: string--><!--Device-SelectOptions-public id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onSelect

```TypeScript
public onSelect?: (index: int, value?: string) => void
```

Callback invoked when an item in the drop-down list box is selected.  
- **index**: index of the selected option. - **value**: value of the selected option.

**Type:** (index: int, value?: string) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectOptions-public onSelect?: (index: int, value?: string) => void--><!--Device-SelectOptions-public onSelect?: (index: int, value?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
public options: Array<SelectOption>
```

Options of an item in the drop-down list box.

**Type:** Array&lt;SelectOption&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectOptions-public options: Array<SelectOption>--><!--Device-SelectOptions-public options: Array<SelectOption>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
public selected?: int
```

Index of the initially selected item in the drop-down list box.The value must be greater than or equal to -1.The index of the first item is 0.If this attribute is not set, the default value **-1** is used, indicating that the option is not selected.Values less than -1 are treated as no selection.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectOptions-public selected?: int--><!--Device-SelectOptions-public selected?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value?: ResourceStr
```

Text content of the drop-down list button itself.The default value is an empty string.Note: If the text length exceeds the column width, it will be truncated. The Resource type is supported since API version 20.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectOptions-public value?: ResourceStr--><!--Device-SelectOptions-public value?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

