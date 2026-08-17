# TouchPadSwipeOptions

Describes information about the touchpad swipe gesture option.

**Since:** 23

<!--Device-unnamed-declare interface TouchPadSwipeOptions--><!--Device-unnamed-declare interface TouchPadSwipeOptions-End-->

**System capability:** SystemCapability.Test.UiTest

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

## speed

```TypeScript
speed?: int
```

Swipe speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 17000007 if negative. <br>Default value: 2000

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TouchPadSwipeOptions-speed?: int--><!--Device-TouchPadSwipeOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## stay

```TypeScript
stay?: boolean
```

Whether the swipe gesture stays on the touchpad for 1s before it is lifted. The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite. <br>Default value: false

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TouchPadSwipeOptions-stay?: boolean--><!--Device-TouchPadSwipeOptions-stay?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

