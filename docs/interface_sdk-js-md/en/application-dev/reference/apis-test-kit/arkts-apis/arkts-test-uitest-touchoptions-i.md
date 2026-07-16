# TouchOptions

Common options for touch operations.

**Since:** 26.0.0

<!--Device-unnamed-declare interface TouchOptions--><!--Device-unnamed-declare interface TouchOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## duration

```TypeScript
duration?: number
```

Duration of the operation in milliseconds.<br>Value range: The value should be >= 1500<br>Unit: ms<br>Default value: 1500

**Type:** number

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-duration?: int--><!--Device-TouchOptions-duration?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## pressure

```TypeScript
pressure?: number
```

The pressure of the touch.<br>Value range:[0.0, 1.0]<br>Default value: 1.0

**Type:** number

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-pressure?: double--><!--Device-TouchOptions-pressure?: double-End-->

**System capability:** SystemCapability.Test.UiTest

## speed

```TypeScript
speed?: number
```

Speed of touch action.<br>Value range:[200, 40000]<br>Unit: px/s.<br>Throws error code 17000007 if negative.<br>Default value: 600

**Type:** number

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-speed?: int--><!--Device-TouchOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

