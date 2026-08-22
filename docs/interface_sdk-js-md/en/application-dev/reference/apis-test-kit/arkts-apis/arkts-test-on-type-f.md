# type

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## type

```TypeScript
export function type(tp: string): On
```

Specifies the type of the target Component.

**Since:** 23

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

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.type('Button'); // Use the static constructor ON to create an On object and specify the type attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { On, ON, MatchPattern } from '@kit.TestKit';

let on: On = ON.type('Button', MatchPattern.EQUALS); // Use the static constructor ON to create an On object and specify the type attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.type('Button'); // Use the static constructor BY to create a By object and specify the type attribute of the target component.
```


## type

```TypeScript
export function type(tp: string, pattern: MatchPattern): On
```

Specifies the type of the target Component.

**Since:** 23

<!--Device-ON-export function type(tp: string, pattern: MatchPattern): On--><!--Device-ON-export function type(tp: string, pattern: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tp | string | Yes | The type value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | Yes | the [MatchPattern](arkts-test-uitest-matchpattern-e.md) of the text value. <br>Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#equals) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Examples**

See [type](#type)

