# belongingDisplay

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## belongingDisplay

```TypeScript
export function belongingDisplay(displayId: int): On
```

Specifies the displayId to which the target Component belongs.

**Since:** 23

<!--Device-ON-export function belongingDisplay(displayId: int): On--><!--Device-ON-export function belongingDisplay(displayId: int): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | int | Yes | the Id of the specified display. |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.belongingDisplay(0); // Use the static constructor ON to create an On object and specify the ID of the display to which the target component belongs.
```

