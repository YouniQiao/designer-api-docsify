# afterComponent

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## afterComponent

```TypeScript
export function afterComponent(com: Component): On
```

Requires that the target Component which is after another Component that specified by the given [Component](arkts-test-uitest-component-c.md#Component) object,used to locate Component relatively.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-ON-export function afterComponent(com: Component): On--><!--Device-ON-export function afterComponent(com: Component): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| com | [Component](arkts-test-uitest-component-c.md) | Yes | describes the Component which the target one is in back of. |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

