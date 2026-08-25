# UiWindow

The **UiWindow** class represents a window on the UI and provides APIs for obtaining window attributes, dragging a window, and adjusting the window size. All APIs provided in this class use a promise to return the result and must be invoked using **await**.

**Since:** 9

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## close

```TypeScript
close(): Promise<void>
```

Closes a window. This API uses a promise to return the result.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## focus

```TypeScript
focus(): Promise<void>
```

Focuses a window. This API uses a promise to return the result.

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

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

Obtains the bounds information of a window. This API uses a promise to return the result.

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

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

Obtains the bundle name of the application to which a window belongs. This API uses a promise to return the result.

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

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

Obtains the ID of the display to which a window belongs. This API uses a promise to return the result.

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

## getTitle

```TypeScript
getTitle(): Promise<string>
```

Obtains the window title. This API uses a promise to return the result.

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

## getWindowMode

```TypeScript
getWindowMode(): Promise<WindowMode>
```

Obtains the window mode. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WindowMode](arkts-test-uitest-windowmode-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## isActive

```TypeScript
isActive(): Promise<boolean>
```

Checks whether a window is active. This API uses a promise to return the result.

**Since:** 11

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

## isActived

```TypeScript
isActived(): Promise<boolean>
```

Checks whether a window is active. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [isActive](#isactive)

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

Checks whether a window is focused. This API uses a promise to return the result.

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

## maximize

```TypeScript
maximize(): Promise<void>
```

Maximizes a window. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that can be maximized.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## minimize

```TypeScript
minimize(): Promise<void>
```

Minimizes a window. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that can be minimized.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves a window to the target point. This API uses a promise to return the result. This API is applicable to moveable windows.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## resize

```TypeScript
resize(wide: number, height: number, direction: ResizeDirection): Promise<void>
```

Resizes a window based on the specified width, height, and direction. This API uses a promise to return the result. This API is applicable to resizable windows.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wide | number | Yes |
| height | number | Yes |
| direction | [ResizeDirection](arkts-test-uitest-resizedirection-e.md) | Yes |

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a window to its previous mode. This API uses a promise to return the result.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## split

```TypeScript
split(): Promise<void>
```

Switches to the split-screen mode. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that support screen splitting.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
