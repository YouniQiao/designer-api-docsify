# AccessibilityElement

An accessibility node element that provides capabilities such as querying parent/child elements, finding elements by content or focus direction, and performing accessibility actions. It is applicable to scenarios where an accessibility app needs to interact with and operate on UI nodes.Before calling methods of AccessibilityElement, obtain an AccessibilityElement instance through [AccessibilityExtensionContext.getAccessibilityFocusedElement()](arkts-accessibility-accessibilityextensioncontext-c-sys.md#getaccessibilityfocusedelement) or [AccessibilityExtensionContext.getRootInActiveWindow()](arkts-accessibility-accessibilityextensioncontext-c-sys.md#getrootinactivewindow).

**Since:** 9

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## enableScreenCurtain

```TypeScript
enableScreenCurtain(isEnable: boolean): void
```

Enables or disables the screen curtain. When the screen curtain is enabled, the screen content is hidden (the screen dims), but the device still responds to operations normally.

**Since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isEnable](#isenable) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## executeAction

```TypeScript
executeAction(action: AccessibilityAction, parameters?: Parameter): Promise<void>
```

Performs an action on an accessibility node element based on the action type and parameters specified. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | [AccessibilityAction](arkts-accessibility-accessibility-accessibilityaction-e-sys.md) | Yes |
| parameters | [Parameter](arkts-accessibility-accessibilityextensioncontext-parameter-c-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300005](../errorcode-accessibility.md#9300005-operation-not-supported) |

## findElement('textType')

```TypeScript
findElement(type: 'textType', condition: string): Promise<Array<AccessibilityElement>>
```

Searches for all node elements based on the accessibility text type configured in the component's accessibilityTextHint attribute. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [type](#type) | 'textType' | Yes |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## findElement('elementId')

```TypeScript
findElement(type: 'elementId', condition: number): Promise<AccessibilityElement>
```

Queries the node element in the current active window based on the element ID. This API uses a promise to return the result.This method and [findElementById](#findelementbyid) both find a node element by element ID. They are functionally equivalent. It is recommended to use findElementById.

**Since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [type](#type) | 'elementId' | Yes |
| condition | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## findElementByContent

```TypeScript
findElementByContent(condition: string): Promise<Array<AccessibilityElement>>
```

Searches for node elements by their content text, and returns all node elements that contain the specified text. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## findElementByFocusDirection

```TypeScript
findElementByFocusDirection(condition: FocusDirection): Promise<AccessibilityElement>
```

Searches for an element based on the focus direction. This API uses a promise to return the result.Compared with [findElementsByCondition](#findelementsbycondition), this method is mainly used to search for web components, while findElementsByCondition is mainly used to search for UI components.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## findElementByFocusDirection

```TypeScript
findElementByFocusDirection(condition: FocusDirection, type: FocusRuleType): Promise<AccessibilityElement>
```

Searches for an element based on the focus direction and focus rule type. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | Yes |
| [type](#type) | [FocusRuleType](arkts-accessibility-accessibility-focusruletype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## findElementById

```TypeScript
findElementById(condition: number): Promise<AccessibilityElement>
```

Searches for a node element in the active window by element ID. This API uses a promise to return the result.This method is functionally equivalent to [findElement('elementId')](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md#findelementcontent) and is recommended for priority use.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## findElementsByAccessibilityHintText

```TypeScript
findElementsByAccessibilityHintText(condition: string): Promise<Array<AccessibilityElement>>
```

Searches for elements by hint text, and returns all node elements whose accessibilityTextHint attribute matches the text. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## findElementsByCondition

```TypeScript
findElementsByCondition(rule: FocusRule, condition: FocusCondition): Promise<FocusMoveResult>
```

Queries focusable nodes that meet the conditions. This API uses a promise to return the result.Compared with [findElementByFocusDirection](#findelementbyfocusdirection), this method is mainly used to find UI components, while findElementByFocusDirection is mainly used to find Web components.

**Since:** 23

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [FocusRule](arkts-accessibility-focusrule-t-sys.md) | Yes |
| condition | [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FocusMoveResult](arkts-accessibility-accessibilityextensioncontext-focusmoveresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## findElementsByCondition

```TypeScript
findElementsByCondition(rule: FocusRule, condition: FocusCondition, type: FocusRuleType): Promise<FocusMoveResult>
```

Searches for focusable nodes of the target type based on the rule and query condition. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [FocusRule](arkts-accessibility-focusrule-t-sys.md) | Yes |
| condition | [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | Yes |
| [type](#type) | [FocusRuleType](arkts-accessibility-accessibility-focusruletype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FocusMoveResult](arkts-accessibility-accessibilityextensioncontext-focusmoveresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getChildren

```TypeScript
getChildren(): Promise<Array<AccessibilityElement>>
```

Obtains the list of child elements of this element. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getCursorPosition

```TypeScript
getCursorPosition(callback: AsyncCallback<number>): void
```

Obtains the cursor position in a text component. This API uses an asynchronous callback to return the result.

**Since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getCursorPosition

```TypeScript
getCursorPosition(): Promise<number>
```

Obtains the cursor position in a text component. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getParent

```TypeScript
getParent(): Promise<AccessibilityElement>
```

Obtains the parent element of an accessibility node. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getRoot

```TypeScript
getRoot(): Promise<AccessibilityElement>
```

Obtains the root element of the active window. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## accessibilityFocused

```TypeScript
accessibilityFocused?: boolean
```

Whether the element gains focus for accessibility purposes. The value **true** indicates that the element has gained focus, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityGroup

```TypeScript
accessibilityGroup?: boolean
```

Whether the element is an accessibility group. The value **true** indicates that the element is an accessibility group, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

Accessibility level of the component.  
**'auto'**: The accessibility grouping service and ArkUI jointly determine whether the component can be recognized by accessibility.  
**'yes'**: The component can be recognized by accessibility.  
**'no'**: The component cannot be recognized by accessibility.  
**'no-hide-descendants'**: The component and all its child components cannot be recognized by accessibility. Default value: **'auto'**.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId?: number
```

ID of the next component to gain focus.Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityPreviousFocusId

```TypeScript
accessibilityPreviousFocusId?: number
```

ID of the previous component to gain focus.Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityScrollable

```TypeScript
accessibilityScrollable?: boolean
```

Whether the element is scrollable for accessibility purposes. This attribute has a higher priority than scrollable. That is, when the value of accessibilityScrollable conflicts with that of scrollable, the value of accessibilityScrollable prevails.The value **true** indicates that the element is scrollable, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityStateDescription

```TypeScript
accessibilityStateDescription?: string
```

Custom accessibility state announcement text of the element.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityText

```TypeScript
accessibilityText?: string
```

Accessibility text information of the element.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityVisible

```TypeScript
accessibilityVisible?: boolean
```

Whether the component is visible for accessibility. The value **true** indicates that the component is visible, and **false** indicates the opposite. Default value: **true**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## belongTreeId

```TypeScript
belongTreeId?: number
```

ID of the component tree to which the element belongs. Default value: **-1**.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName?: string
```

Bundle name.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## checkable

```TypeScript
checkable?: boolean
```

Whether the element is checkable. The value **true** indicates that the element is checkable, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## checked

```TypeScript
checked?: boolean
```

Whether the element is checked. The value **true** indicates that the element is checked, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## childrenIds

```TypeScript
childrenIds?: Array<number>
```

List of child element IDs of the component. Default value: empty array.

**Type:** Array&lt;number&gt;

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## childrenTreeId

```TypeScript
childrenTreeId?: number
```

ID of the child component tree of the element. Default value: **-1**.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## clickable

```TypeScript
clickable?: boolean
```

Whether the element is clickable. The value **true** indicates that the element is clickable, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## clip

```TypeScript
clip?: boolean
```

Whether the component needs clipping. The value **true** indicates that clipping is needed, and **false** indicates the opposite. Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## componentId

```TypeScript
componentId?: number
```

ID of the component to which the element belongs.Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## componentType

```TypeScript
componentType?: string
```

Type of the component to which the element belongs.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## contents

```TypeScript
contents?: Array<string>
```

Content displayed by the element. Default value: empty array.

**Type:** Array&lt;string&gt;

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## currentIndex

```TypeScript
currentIndex?: number
```

Index of the current item.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## currentItem

```TypeScript
currentItem?: AccessibilityGrid
```

Current item in the component grid.

**Type:** [AccessibilityGrid](arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md)

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## customActions

```TypeScript
customActions?: Array<string>
```

List of custom actions supported by the element.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## customComponentType

```TypeScript
customComponentType?: string
```

Custom component type. Corresponds to the [AccessibilityRoleType](../../apis-arkui/arkts-components/arkts-arkui-accessibilityroletype-e.md) type of the element.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## description

```TypeScript
description?: string
```

Description of the element.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## editable

```TypeScript
editable?: boolean
```

Whether the element is editable. The value **true** indicates that the element is editable, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## endIndex

```TypeScript
endIndex?: number
```

Index of the last list item displayed on the screen.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## error

```TypeScript
error?: string
```

Error state of the element.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## extraInfo

```TypeScript
extraInfo?: string
```

Extra information of the element. The value is a JSON string.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## focusable

```TypeScript
focusable?: boolean
```

Whether the element can gain focus (here it refers to accessibility focus, which is different from input focus). The value **true** indicates that the element can gain focus, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## hintText

```TypeScript
hintText?: string
```

Hint text.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## hotArea

```TypeScript
hotArea?: Rect
```

Touchable area of the element.

**Type:** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## inputType

```TypeScript
inputType?: number
```

Type of the input text. Different values correspond to different input modes: **0** indicates no specific type; **1** indicates text; **2** indicates email; **3** indicates date; **4** indicates time; **5** indicates number; **6** indicates password; **7** indicates phone number; **8** indicates username; **9** indicates new password.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## inspectorKey

```TypeScript
inspectorKey?: string
```

Inspector key.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isActive

```TypeScript
isActive?: boolean
```

Whether the element is active. The value **true** indicates that the element is active, and **false** indicates the opposite.Default value: **true**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isEnable

```TypeScript
isEnable?: boolean
```

Whether the element is enabled. The value **true** indicates that the element is enabled, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isEssential

```TypeScript
isEssential?: boolean
```

Whether the element is essential to the user. The value **true** indicates that the element is essential, and **false** indicates the opposite. Default value: **false**.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isFocused

```TypeScript
isFocused?: boolean
```

Whether the element has gained focus (here it refers to accessibility focus, which is different from input focus). The value **true** indicates that the element has gained focus, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isHint

```TypeScript
isHint?: boolean
```

Whether the element is a hint. The value **true** indicates that the element is a hint, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isPassword

```TypeScript
isPassword?: boolean
```

Whether the element is a password. The value **true** indicates that the element is a password, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isVisible

```TypeScript
isVisible?: boolean
```

Whether the element is visible. The value **true** indicates that the element is visible, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## itemCount

```TypeScript
itemCount?: number
```

Total number of items.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## lastContent

```TypeScript
lastContent?: string
```

Content of the last item.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## layer

```TypeScript
layer?: number
```

Display layer of the element.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## longClickable

```TypeScript
longClickable?: boolean
```

Whether the element is number-clickable. The value **true** indicates that the element is number-clickable, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## mainWindowId

```TypeScript
mainWindowId?: number
```

Main window ID of the component. Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## navDestinationId

```TypeScript
navDestinationId?: number
```

Navigation destination ID of the component. Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## offset

```TypeScript
offset?: number
```

Pixel offset of the content area relative to the top coordinate of the scrollable component (such as List and Grid), in pixels (px).Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## pageId

```TypeScript
pageId?: number
```

Page ID.Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## parentId

```TypeScript
parentId?: number
```

Parent element ID of the component. Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## pluralLineSupported

```TypeScript
pluralLineSupported?: boolean
```

Whether the element supports multi-line text. The value **true** indicates that the element supports multi-line text, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## rect

```TypeScript
rect?: Rect
```

Area of the element.

**Type:** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## resourceName

```TypeScript
resourceName?: string
```

Resource name of the element.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## screenRect

```TypeScript
screenRect?: Rect
```

Display area of the element.

**Type:** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## scrollable

```TypeScript
scrollable?: boolean
```

Whether the element is scrollable. The value **true** indicates that the element is scrollable, and **false** indicates the opposite. When the value conflicts with that of accessibilityScrollable, the value of accessibilityScrollable prevails.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## selected

```TypeScript
selected?: boolean
```

Whether the element is selected. The value **true** indicates that the element is selected, and **false** indicates the opposite.Default value: **false**.

**Type:** boolean

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## sourceType

```TypeScript
sourceType?: AccessibilitySourceType
```

Source type of the component, used to distinguish default components from newly added or modified virtual components.

**Type:** [AccessibilitySourceType](arkts-accessibility-accessibility-accessibilitysourcetype-e-sys.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## spans

```TypeScript
spans?: AccessibilitySpan[]
```

Array of accessibility hyperlink text information of the component. Default value: empty array.

**Type:** [AccessibilitySpan](arkts-accessibility-accessibilityextensioncontext-accessibilityspan-i-sys.md)[]

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## startIndex

```TypeScript
startIndex?: number
```

Index of the first list item on the screen.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## supportedActionNames

```TypeScript
supportedActionNames?: Array<string>
```

Supported action names. Default value: empty array.

**Type:** Array&lt;string&gt;

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## text

```TypeScript
text?: string
```

Text content of the element.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## textLengthLimit

```TypeScript
textLengthLimit?: number
```

Maximum text length of the element. Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## textMoveUnit

```TypeScript
textMoveUnit?: accessibility.TextMoveUnit
```

Movement unit for text reading.Default value: **char**.

**Type:** accessibility.TextMoveUnit

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## textType

```TypeScript
textType?: string
```

Accessibility text type of the element, configured by the accessibilityTextHint attribute of the component.

**Type:** string

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## triggerAction

```TypeScript
triggerAction?: AccessibilityAction
```

Action that triggers the element event.

**Type:** [AccessibilityAction](arkts-accessibility-accessibility-accessibilityaction-e-sys.md)

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## type

```TypeScript
type?: WindowType
```

Window type of the element.

**Type:** [WindowType](arkts-accessibility-windowtype-t.md)

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## valueMax

```TypeScript
valueMax?: number
```

Maximum value.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## valueMin

```TypeScript
valueMin?: number
```

Minimum value.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## valueNow

```TypeScript
valueNow?: number
```

Current value.Default value: **0**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## windowId

```TypeScript
windowId?: number
```

Window ID.Default value: **-1**.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.
