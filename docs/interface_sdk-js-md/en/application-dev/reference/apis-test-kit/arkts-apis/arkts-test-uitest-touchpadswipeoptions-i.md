# TouchPadSwipeOptions

Describes information about the touchpad swipe gesture option.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface TouchPadSwipeOptions--><!--Device-unnamed-declare interface TouchPadSwipeOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## speed

```TypeScript
speed?: int
```

Swipe speed.&lt;br&gt;Value range:[200, 40000]&lt;br&gt;Unit: px/s.&lt;br&gt;Throws error code 17000007 if negative.&lt;br&gt;Default value: 2000

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TouchPadSwipeOptions-speed?: int--><!--Device-TouchPadSwipeOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## stay

```TypeScript
stay?: boolean
```

Whether the swipe gesture stays on the touchpad for 1s before it is lifted.The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite.&lt;br&gt;Default value: false

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TouchPadSwipeOptions-stay?: boolean--><!--Device-TouchPadSwipeOptions-stay?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

