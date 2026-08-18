# RectChangeOptions

Describes the value and reason returned upon a window rectangle (position and size) change.

**Since:** 23

<!--Device-window-interface RectChangeOptions--><!--Device-window-interface RectChangeOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
import { floatView } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';
```

## reason

```TypeScript
reason: RectChangeReason
```

Reason for the window rectangle change.

**Type:** RectChangeReason

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RectChangeOptions-reason: RectChangeReason--><!--Device-RectChangeOptions-reason: RectChangeReason-End-->

**System capability:** SystemCapability.Window.SessionManager

## rect

```TypeScript
rect: Rect
```

New value of the window rectangle.

**Type:** Rect

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RectChangeOptions-rect: Rect--><!--Device-RectChangeOptions-rect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

