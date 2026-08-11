# TouchOptions

Common options for touch operations.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-declare interface TouchOptions--><!--Device-unnamed-declare interface TouchOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## duration

```TypeScript
duration?: int
```

Duration of the operation in milliseconds.&lt;br&gt;Value range: The value should be >= 1500&lt;br&gt;Unit: ms&lt;br&gt;Default value: 1500

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-duration?: int--><!--Device-TouchOptions-duration?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## pressure

```TypeScript
pressure?: double
```

Pressure value of the touch. The value range is [0, 1]. The default value is **0**. If the value is **null** or  
**undefined**, the default value is used. If the value is out of the value range, the 17000007 error code is thrown.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-pressure?: double--><!--Device-TouchOptions-pressure?: double-End-->

**System capability:** SystemCapability.Test.UiTest

## speed

```TypeScript
speed?: int
```

Speed of touch action.&lt;br&gt;Value range:[200, 40000]&lt;br&gt;Unit: px/s.&lt;br&gt;If the value is out of range or null/undefined, the default value 600 is used.&lt;br&gt;Default value: 600

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-speed?: int--><!--Device-TouchOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

