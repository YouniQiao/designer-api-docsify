# KeyOptions

表示按键操作的选项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-declare interface KeyOptions--><!--Device-unnamed-declare interface KeyOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## key1

```TypeScript
key1?: int
```

操作期间要按下的第一个键码。如果未设置，将不会注入任何按键事件。如果仅设置 key2 而未设置 key1，将会导致业务错误 17000007。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KeyOptions-key1?: int--><!--Device-KeyOptions-key1?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## key2

```TypeScript
key2?: int
```

操作期间要按下的第二个键码。 如果未设置，将不会注入任何按键事件。 如果仅设置 key2 而未设置 key1，将会导致业务错误 17000007。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KeyOptions-key2?: int--><!--Device-KeyOptions-key2?: int-End-->

**System capability:** SystemCapability.Test.UiTest

