# Point

Represents the point on the device screen.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface Point--><!--Device-unnamed-declare interface Point-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## displayId

```TypeScript
displayId?: int
```

ID of the display to which the coordinate point belongs. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Point-displayId?: int--><!--Device-Point-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## x

```TypeScript
x: int
```

Horizontal coordinate of a coordinate point, in pixels. The value is an integer greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Point-x: int--><!--Device-Point-x: int-End-->

**System capability:** SystemCapability.Test.UiTest

## y

```TypeScript
y: int
```

Vertical coordinate of a coordinate point, in pixels. The value is an integer greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Point-y: int--><!--Device-Point-y: int-End-->

**System capability:** SystemCapability.Test.UiTest

