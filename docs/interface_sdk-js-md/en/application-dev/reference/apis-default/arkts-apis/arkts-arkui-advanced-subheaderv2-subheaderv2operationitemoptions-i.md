# SubHeaderV2OperationItemOptions

Defines the options for initializing a **SubHeaderV2OperationItem** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface SubHeaderV2OperationItemOptions--><!--Device-unnamed-export interface SubHeaderV2OperationItemOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## accessibilityDescription

```TypeScript
accessibilityDescription?: ResourceStr
```

Accessibility description.Default value: **"Double-tap to activate"**

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-accessibilityDescription?: ResourceStr--><!--Device-SubHeaderV2OperationItemOptions-accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

Accessibility level of the icon on the right side of the subheader.The options are as follows:  
**"auto"**: The icon's recognizability by accessibility services is determined by the accessibility grouping service and ArkUI.  
**"yes"**: The icon can be recognized by accessibility services.  
**"no"**: The icon cannot be recognized by accessibility services.  
**"no-hide-descendants"**: Neither the icon nor its child components can be recognized by accessibility services.Default value: **"yes"**

**Type:** string

**Default:** "auto".The options are as follows:<br/>"auto":The value is converted to "yes" or "no" based on the component."yes": the current component is selectable for the accessibility service."no": The current component is not selectable for the accessibility service."no-hide-descendants":The current component and all its child components are not selectable<br/> for the accessibility service.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-accessibilityLevel?: string--><!--Device-SubHeaderV2OperationItemOptions-accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
accessibilityText?: ResourceStr
```

Accessibility text of the icon on the right side of the subheader.Default value: **undefined**

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-accessibilityText?: ResourceStr--><!--Device-SubHeaderV2OperationItemOptions-accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action?: SubHeaderV2OperationItemAction
```

Event triggered when the item is operated. Default value: **() =&gt; void**.

**Type:** [SubHeaderV2OperationItemAction](arkts-subheaderv2operationitemaction-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-action?: SubHeaderV2OperationItemAction--><!--Device-SubHeaderV2OperationItemOptions-action?: SubHeaderV2OperationItemAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: SubHeaderV2OperationItemType
```

Content of the item in the operation area.

**Type:** [SubHeaderV2OperationItemType](arkts-subheaderv2operationitemtype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-content: SubHeaderV2OperationItemType--><!--Device-SubHeaderV2OperationItemOptions-content: SubHeaderV2OperationItemType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

Whether to receive default focus.  
**true**: Receive default focus.  
**false**: Do not receive default focus.Default value: **false**

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-defaultFocus?: boolean--><!--Device-SubHeaderV2OperationItemOptions-defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id?: string
```

Sets the id for operation item.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItemOptions-id?: string--><!--Device-SubHeaderV2OperationItemOptions-id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

