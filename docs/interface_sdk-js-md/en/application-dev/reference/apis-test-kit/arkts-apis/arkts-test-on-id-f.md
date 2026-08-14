# id

## Modules to Import

```TypeScript
import { Component } from 'Component';
import { DisplayRotation } from 'DisplayRotation';
import { Driver } from 'Driver';
import { MatchPattern } from 'MatchPattern';
import { MouseButton } from 'MouseButton';
import { ON } from 'ON';
import { On } from 'On';
import { PointerMatrix } from 'PointerMatrix';
import { ResizeDirection } from 'ResizeDirection';
import { UIElementInfo } from 'UIElementInfo';
import { UIEventObserver } from 'UIEventObserver';
import { UiDirection } from 'UiDirection';
import { UiWindow } from 'UiWindow';
import { WindowMode } from 'WindowMode';
import { Point } from 'Point';
import { WindowFilter } from 'WindowFilter';
import { Rect } from 'Rect';
import { TouchPadSwipeOptions } from 'TouchPadSwipeOptions';
import { InputTextMode } from 'InputTextMode';
import { WindowChangeType } from 'WindowChangeType';
import { ComponentEventType } from 'ComponentEventType';
import { WindowChangeOptions } from 'WindowChangeOptions';
import { ComponentEventOptions } from 'ComponentEventOptions';
import { TouchOptions } from 'TouchOptions';
import { KeyOptions } from 'KeyOptions';
import { PenKey } from 'PenKey';
import { PenMode } from 'PenMode';
import { PenKeyOperation } from 'PenKeyOperation';
import { PenKeyOperationOptions } from 'PenKeyOperationOptions';
```

## id

```TypeScript
export function id(id: string): On
```

Specifies the id of the target Component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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


## id

```TypeScript
export function id(id: string, pattern: MatchPattern): On
```

Specifies the id of the target Component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ON-export function id(id: string, pattern: MatchPattern): On--><!--Device-ON-export function id(id: string, pattern: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | the id value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | Yes | the [MatchPattern](arkts-test-uitest-matchpattern-e.md#MatchPattern) of the text value. <br>Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#EQUALS) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

