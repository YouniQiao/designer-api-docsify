# UiComponent

In **UiTest**, the **UiComponent** class represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection. All APIs provided in this class use a promise to return the result and must be invoked using **await**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component](arkts-test-uitest-component-c.md)

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## click

```TypeScript
click(): Promise<void>
```

Clicks this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [click](arkts-test-uitest-component-c.md#click)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

Double-clicks this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [doubleClick](arkts-test-uitest-component-c.md#doubleclick)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## getId

```TypeScript
getId(): Promise<number>
```

Obtains the ID of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getId](arkts-test-uitest-component-c.md#getid)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getKey

```TypeScript
getKey(): Promise<string>
```

Obtains the key of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getId](arkts-test-uitest-component-c.md#getid)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getText

```TypeScript
getText(): Promise<string>
```

Obtains the text information of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getText](arkts-test-uitest-component-c.md#gettext)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getType

```TypeScript
getType(): Promise<string>
```

Obtains the type of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getType](arkts-test-uitest-component-c.md#gettype)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## inputText

```TypeScript
inputText(text: string): Promise<void>
```

Inputs text to a component. This API takes effect only for editable text components. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputText](arkts-test-uitest-component-c.md#inputtext)(text: string)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## isClickable

```TypeScript
isClickable(): Promise<boolean>
```

Obtains the clickable status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isClickable](arkts-test-uitest-component-c.md#isclickable)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

Obtains the enabled status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isEnabled](arkts-test-uitest-component-c.md#isenabled)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

Obtains the focused status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isFocused](arkts-test-uitest-component-c.md#isfocused)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

Obtains the scrollable status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isScrollable](arkts-test-uitest-component-c.md#isscrollable)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isSelected

```TypeScript
isSelected(): Promise<boolean>
```

Obtains the selected status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isSelected](arkts-test-uitest-component-c.md#isselected)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## longClick

```TypeScript
longClick(): Promise<void>
```

Long-clicks this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [longClick](arkts-test-uitest-component-c.md#longclick)

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## scrollSearch

```TypeScript
scrollSearch(by: By): Promise<UiComponent>
```

Scrolls on this component to search for the target component (applicable to components that support scrolling, such as **List**). This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [scrollSearch](arkts-test-uitest-component-c.md#scrollsearch)(on: On)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt; |
