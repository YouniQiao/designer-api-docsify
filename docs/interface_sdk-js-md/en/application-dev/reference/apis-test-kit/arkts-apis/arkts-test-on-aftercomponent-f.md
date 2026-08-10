# afterComponent

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## afterComponent

```TypeScript
export function afterComponent(com: Component): On
```

要求目标组件位于由给定{@link Component}指定的另一个组件之后对象，用于相对于组件定位。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-ON-export function afterComponent(com: Component): On--><!--Device-ON-export function afterComponent(com: Component): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| com | [Component](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-component-i.md) | Yes | 描述目标组件的后端组件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |

