# text

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## text

```TypeScript
export function text(txt: string, pattern?: MatchPattern): On
```

Specifies the text for the target Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ON-export function text(txt: string, pattern?: MatchPattern): On--><!--Device-ON-export function text(txt: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| txt | string | Yes | the text value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | the [MatchPattern](arkts-test-uitest-matchpattern-e.md#MatchPattern) of the text value. &lt;br&gt;Default value: MatchPattern.EQUALS |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

