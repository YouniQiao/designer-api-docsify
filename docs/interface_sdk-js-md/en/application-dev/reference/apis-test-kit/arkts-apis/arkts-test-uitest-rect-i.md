# Rect

Represents the rectangle area on the device screen.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface Rect--><!--Device-unnamed-declare interface Rect-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## bottom

```TypeScript
bottom: int
```

Y coordinate of the lower right corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-bottom: int--><!--Device-Rect-bottom: int-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: int
```

ID of the display to which the component border belongs. The value is an integer greater than or equal to 0. &lt;br&gt;Default value: the default screen ID of the device.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Rect-displayId?: int--><!--Device-Rect-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## left

```TypeScript
left: int
```

X coordinate of the upper left corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-left: int--><!--Device-Rect-left: int-End-->

**System capability:** SystemCapability.Test.UiTest

## right

```TypeScript
right: int
```

X coordinate of the lower right corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-right: int--><!--Device-Rect-right: int-End-->

**System capability:** SystemCapability.Test.UiTest

## top

```TypeScript
top: int
```

Y coordinate of the upper left corner of the component border, in pixels. The value is an integer greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-top: int--><!--Device-Rect-top: int-End-->

**System capability:** SystemCapability.Test.UiTest

