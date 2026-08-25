# Component

Represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection. All APIs provided in this class use a promise to return the result and must be invoked using **await**.

**Since:** 9

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## clearText

```TypeScript
clearText(): Promise<void>
```

Clears the text information of a component. This API takes effect only for editable text components. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## click

```TypeScript
click(): Promise<void>
```

Clicks this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

Double-clicks this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## dragTo

```TypeScript
dragTo(target: Component): Promise<void>
```

Drags a component to the target component. This method is valid only for components that can be dragged. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [Component](arkts-test-uitest-component-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

Obtains the bounds information of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Rect](arkts-test-uitest-rect-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getBoundsCenter

```TypeScript
getBoundsCenter(): Promise<Point>
```

Obtains the center point of the area occupied by this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getDescription

```TypeScript
getDescription(): Promise<string>
```

Obtains the description of this component. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

Obtains the ID of the display to which the component belongs. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getHint

```TypeScript
getHint(): Promise<string>
```

Obtains the hint text of a component. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getId

```TypeScript
getId(): Promise<string>
```

Obtains the ID of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getOriginalText

```TypeScript
getOriginalText(): Promise<string>
```

Obtains the text information of this component. This API uses a promise to return the result. If the accessibilityLevel attribute of the component is set to **no** or **no-hide-descendants**, this API can be used to obtain the text information of the component, but [Component.getText()](#gettext) cannot.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getText

```TypeScript
getText(): Promise<string>
```

Obtains the text information of this component. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the accessibilityLevel
> attribute of the component is set to **no** or **no-hide-descendants**, this API cannot be used to obtain the
> text information of the component. In this case, you can use
> [Component.getOriginalText ()](#getoriginaltext) instead.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## getType

```TypeScript
getType(): Promise<string>
```

Obtains the type of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## inputText

```TypeScript
inputText(text: string): Promise<void>
```

Clears the original text in a component and inputs the specified text. This API takes effect only for editable text components. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## inputText

```TypeScript
inputText(text: string, mode: InputTextMode): Promise<void>
```

Inputs text to a component in a specified text input mode. This API takes effect only for editable text components. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| mode | [InputTextMode](arkts-test-uitest-inputtextmode-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isCheckable

```TypeScript
isCheckable(): Promise<boolean>
```

Obtains the checkable status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isChecked

```TypeScript
isChecked(): Promise<boolean>
```

Obtains the checked status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isClickable

```TypeScript
isClickable(): Promise<boolean>
```

Obtains the clickable status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

Obtains the enabled status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

Checks whether a component is focused. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isLongClickable

```TypeScript
isLongClickable(): Promise<boolean>
```

Obtains the number-clickable status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

Obtains the scrollable status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isSelected

```TypeScript
isSelected(): Promise<boolean>
```

Obtains the selected status of this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## longClick

```TypeScript
longClick(): Promise<void>
```

Long-clicks this component. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## pinchIn

```TypeScript
pinchIn(scale: number): Promise<void>
```

Pinches in a component at the specified scale. This method is valid only for components that support scaling. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## pinchOut

```TypeScript
pinchOut(scale: number): Promise<void>
```

Pinches out a component at the specified scale. This method is valid only for components that support scaling. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## scrollSearch

```TypeScript
scrollSearch(on: On): Promise<Component>
```

Scrolls on this component to search for the target component. This API is applicable to components that support scrolling. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>
```

Scrolls on this component to search for the target component. This API is applicable to components that support scrolling. You can specify the scrolling direction and the offset between the scrolling start and end points and the component border. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |
| vertical | boolean | No |
| offset | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## scrollToBottom

```TypeScript
scrollToBottom(speed?: number): Promise<void>
```

Scrolls to the bottom of this component. This API is applicable to components that support scrolling. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## scrollToTop

```TypeScript
scrollToTop(speed?: number): Promise<void>
```

Scrolls to the top of this component. This API is applicable to components that support scrolling. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |
