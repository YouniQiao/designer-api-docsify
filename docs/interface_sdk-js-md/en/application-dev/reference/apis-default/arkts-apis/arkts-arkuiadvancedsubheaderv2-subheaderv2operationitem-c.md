# SubHeaderV2OperationItem

Represents an item in the operation area.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class SubHeaderV2OperationItem--><!--Device-unnamed-export declare class SubHeaderV2OperationItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: SubHeaderV2OperationItemOptions)
```

Constructor of **SubHeaderV2OperationItem**.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-constructor(options: SubHeaderV2OperationItemOptions)--><!--Device-SubHeaderV2OperationItem-constructor(options: SubHeaderV2OperationItemOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SubHeaderV2OperationItemOptions](arkts-arkuiadvancedsubheaderv2-subheaderv2operationitemoptions-i.md) | Yes | Operation item configuration information. Defines the options for initializing a **SubHeaderV2OperationItem** object. |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

Accessibility description.

Default value: **"Double-tap to activate"**

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

Accessibility level of the icon on the right side of the subheader.

The options are as follows:

**"auto"**: The icon's recognizability by accessibility services is determined by the accessibility grouping service and ArkUI.

**"yes"**: The icon can be recognized by accessibility services.

**"no"**: The icon cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the icon nor its child components can be recognized by accessibility services.

Default value: **"yes"**

Decorator: @Trace

**Type:** string

**Default:** "auto".The options are as follows:<br/> "auto":The value is converted to "yes" or "no" based on the component. "yes": the current component is selectable for the accessibility service. "no": The current component is not selectable for the accessibility service. "no-hide-descendants":The current component and all its child components are not selectable<br/> for the accessibility service.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityLevel?: string--><!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

Accessibility text of the icon on the right side of the subheader.

Default value: **undefined**

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityText?: ResourceStr--><!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
@Trace
  public action?: SubHeaderV2OperationItemAction
```

Event triggered when the item is operated. Default value: **() =&gt; void**.

Decorator: @Trace

**Type:** [SubHeaderV2OperationItemAction](arkts-subheaderv2operationitemaction-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public action?: SubHeaderV2OperationItemAction--><!--Device-SubHeaderV2OperationItem-@Trace  public action?: SubHeaderV2OperationItemAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Trace
  public content: SubHeaderV2OperationItemType
```

Content of the item in the operation area.

Decorator: @Trace

**Type:** [SubHeaderV2OperationItemType](arkts-subheaderv2operationitemtype-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public content: SubHeaderV2OperationItemType--><!--Device-SubHeaderV2OperationItem-@Trace  public content: SubHeaderV2OperationItemType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
@Trace
  public defaultFocus?: boolean
```

Whether to receive default focus.

**true**: Receive default focus.

**false**: Do not receive default focus.

Default value: **false**

Decorator: @Trace

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public defaultFocus?: boolean--><!--Device-SubHeaderV2OperationItem-@Trace  public defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
@Trace
  public id?: string
```

Sets the id for operation item.

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2OperationItem-@Trace  public id?: string--><!--Device-SubHeaderV2OperationItem-@Trace  public id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

