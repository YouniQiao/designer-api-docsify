# Rect

Represents the rectangle area on the device screen.

**Since:** 23

<!--Device-unnamed-declare interface Rect--><!--Device-unnamed-declare interface Rect-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## bottom

```TypeScript
bottom: int
```

Y coordinate of the lower right corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** int

**Since:** 23

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-top: int--><!--Device-Rect-top: int-End-->

**System capability:** SystemCapability.Test.UiTest

