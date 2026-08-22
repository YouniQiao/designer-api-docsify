# longClickable

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## longClickable

```TypeScript
export function longClickable(b?: boolean): On
```

Specifies the longClickable status of the target Component.

**Since:** 23

<!--Device-ON-export function longClickable(b?: boolean): On--><!--Device-ON-export function longClickable(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | the longClickable status. <br>Default value: true |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.longClickable(true); // Use the static constructor ON to create an On object and specify the longClickable attribute of the target component.
```

