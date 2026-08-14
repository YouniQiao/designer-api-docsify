# Rect

Represents the rectangle area on the device screen.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare interface Rect--><!--Device-unnamed-declare interface Rect-End-->

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

## bottom

```TypeScript
bottom: int
```

Y coordinate of the lower right corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-bottom: int--><!--Device-Rect-bottom: int-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: int
```

ID of the display to which the component border belongs. The value is an integer greater than or equal to 0. <br>Default value: the default screen ID of the device.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Rect-displayId?: int--><!--Device-Rect-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## left

```TypeScript
left: int
```

X coordinate of the upper left corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-left: int--><!--Device-Rect-left: int-End-->

**System capability:** SystemCapability.Test.UiTest

## right

```TypeScript
right: int
```

X coordinate of the lower right corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-right: int--><!--Device-Rect-right: int-End-->

**System capability:** SystemCapability.Test.UiTest

## top

```TypeScript
top: int
```

Y coordinate of the upper left corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-top: int--><!--Device-Rect-top: int-End-->

**System capability:** SystemCapability.Test.UiTest

