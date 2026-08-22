# text

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## text

```TypeScript
export function text(txt: string, pattern?: MatchPattern): On
```

Specifies the text for the target Component.

**Since:** 23

<!--Device-ON-export function text(txt: string, pattern?: MatchPattern): On--><!--Device-ON-export function text(txt: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| txt | string | Yes | the text value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | the [MatchPattern](arkts-test-uitest-matchpattern-e.md) of the text value. <br>Default value: MatchPattern.EQUALS |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.text('123'); // Use the static constructor ON to create an On object and specify the text attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { BY, By } from '@kit.TestKit';

let by: By = BY.text('123'); // Use the static constructor BY to create a By object and specify the text attribute of the target component.
```

