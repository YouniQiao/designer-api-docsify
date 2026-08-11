# RectChangeOptions

Describes the value and reason returned upon a window rectangle (position and size) change.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-window-interface RectChangeOptions--><!--Device-window-interface RectChangeOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## reason

```TypeScript
reason: RectChangeReason
```

Reason for the window rectangle change.

**Type:** [RectChangeReason](arkts-arkui-uiextension-rectchangereason-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RectChangeOptions-reason: RectChangeReason--><!--Device-RectChangeOptions-reason: RectChangeReason-End-->

**System capability:** SystemCapability.Window.SessionManager

## rect

```TypeScript
rect: Rect
```

New value of the window rectangle.

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RectChangeOptions-rect: Rect--><!--Device-RectChangeOptions-rect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

