# type

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## type

```TypeScript
export function type(tp: string): On
```

Specifies the type of the target Component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ON-export function type(tp: string): On--><!--Device-ON-export function type(tp: string): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tp | string | Yes | The type value. |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |


## type

```TypeScript
export function type(tp: string, pattern: MatchPattern): On
```

Specifies the type of the target Component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ON-export function type(tp: string, pattern: MatchPattern): On--><!--Device-ON-export function type(tp: string, pattern: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tp | string | Yes | The type value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | Yes | the [MatchPattern](arkts-test-uitest-matchpattern-e.md#MatchPattern) of the text value. &lt;br&gt;Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#EQUALS) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

