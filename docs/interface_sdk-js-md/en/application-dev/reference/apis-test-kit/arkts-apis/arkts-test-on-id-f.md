# id

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## id

```TypeScript
export function id(id: string): On
```

Specifies the id of the target Component.

**Since:** 23

<!--Device-ON-export function id(id: string): On--><!--Device-ON-export function id(id: string): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | the id value. |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.id('123'); // Use the static constructor ON to create an On object and specify the ID attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.id('id', MatchPattern.REG_EXP_ICASE); // Use case-insensitive regular expression to match the ID attribute value of the component.
```

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.id(123); // Use the static constructor BY to create a By object and specify the id attribute of the target component.
```


## id

```TypeScript
export function id(id: string, pattern: MatchPattern): On
```

Specifies the id of the target Component.

**Since:** 23

<!--Device-ON-export function id(id: string, pattern: MatchPattern): On--><!--Device-ON-export function id(id: string, pattern: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | the id value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | Yes | the [MatchPattern](arkts-test-uitest-matchpattern-e.md) of the text value. <br>Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#equals) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Examples**

See [id](#id)

