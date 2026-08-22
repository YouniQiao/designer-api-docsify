# isAfter

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## isAfter

```TypeScript
export function isAfter(on: On): On
```

Requires that the target Component which is after another Component that specified by the given [On](arkts-test-uitest-on-c.md) object,used to locate Component relatively.

**Since:** 23

<!--Device-ON-export function isAfter(on: On): On--><!--Device-ON-export function isAfter(on: On): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | describes the attribute requirements of Component which the target one is in back of. |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located after the given attribute component.
let on: On = ON.type('Text').isAfter(ON.text('123')); // Search for the first Text component located after the component whose text is 123.
```

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// Use the static constructor BY to create a by object and specify that the target component is located after the given attribute component.
let by: By = BY.type('Text').isAfter(BY.text('123')); // Search for the first Text component located after the component whose text is 123.
```

