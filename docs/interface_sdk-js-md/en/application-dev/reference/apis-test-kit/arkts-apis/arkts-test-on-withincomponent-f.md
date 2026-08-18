# withinComponent

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## withinComponent

```TypeScript
export function withinComponent(com: Component): On
```

Requires that the target Component which is inside of another Component that specified by the given [Component](arkts-test-uitest-component-c.md) object,used to locate Component relatively.

**Since:** 26.0.0

<!--Device-ON-export function withinComponent(com: Component): On--><!--Device-ON-export function withinComponent(com: Component): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| com | [Component](arkts-test-uitest-component-c.md) | Yes | describes the Component which the target one is inside of. |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

