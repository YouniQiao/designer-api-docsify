# OperationOption

Declare type OperationOption

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class OperationOption--><!--Device-unnamed-export declare class OperationOption-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## accessibilityDescription

```TypeScript
public accessibilityDescription?: ResourceStr
```

Accessible description. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.Default value: "Loading" when the operation type is **LOADING** and **"Double-tap to activate"** otherwise.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public accessibilityDescription?: ResourceStr--><!--Device-OperationOption-public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
public accessibilityLevel?: string
```

Accessibility level. It determines whether the component can be recognized by accessibility services.The options are as follows:  
**"auto"**: This option is treated as "yes" by the system for this component.  
**"yes"**: The component can be recognized by accessibility services.  
**"no"**: The component cannot be recognized by accessibility services.  
**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.Default value: **"auto"**

**Type:** string

**Default:** "auto"

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public accessibilityLevel?: string--><!--Device-OperationOption-public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
public accessibilityText?: ResourceStr
```

Accessibility text, that is, accessible label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.Default value: value of the **value** property if the operation type is **TEXT_ARROW** or **BUTTON** and an empty string otherwise.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public accessibilityText?: ResourceStr--><!--Device-OperationOption-public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
public action?: () => void
```

Right-side button click event.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public action?: () => void--><!--Device-OperationOption-public action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
public defaultFocus?: boolean
```

Whether to receive default focus.  
**true**: Receive default focus.  
**false**: Do not receive default focus.Default value: **false**

**Type:** boolean

**Default:** { false }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public defaultFocus?: boolean--><!--Device-OperationOption-public defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
public id?: string
```

Set the id for operation.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public id?: string--><!--Device-OperationOption-public id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: ResourceStr
```

Text content.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationOption-public value: ResourceStr--><!--Device-OperationOption-public value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

