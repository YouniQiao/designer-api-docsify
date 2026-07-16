# Rect

Represents the rectangle area on the device screen.

**Since:** 9

<!--Device-unnamed-declare interface Rect--><!--Device-unnamed-declare interface Rect-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## bottom

```TypeScript
bottom: number
```

Y coordinate of the lower right corner of the component border. The value is an integer greater than 0.<br>Unit: px

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-bottom: int--><!--Device-Rect-bottom: int-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: number
```

ID of the display to which the component border belongs. The value is an integer greater than or equal to 0.<br>Default value: the default screen ID of the device.

**Type:** number

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Rect-displayId?: int--><!--Device-Rect-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## left

```TypeScript
left: number
```

X coordinate of the upper left corner of the component border. The value is an integer greater than 0.<br>Unit: px

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-left: int--><!--Device-Rect-left: int-End-->

**System capability:** SystemCapability.Test.UiTest

## right

```TypeScript
right: number
```

X coordinate of the lower right corner of the component border. The value is an integer greater than 0.<br>Unit: px

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-right: int--><!--Device-Rect-right: int-End-->

**System capability:** SystemCapability.Test.UiTest

## top

```TypeScript
top: number
```

Y coordinate of the upper left corner of the component border. The value is an integer greater than 0.<br>Unit: px

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-top: int--><!--Device-Rect-top: int-End-->

**System capability:** SystemCapability.Test.UiTest

