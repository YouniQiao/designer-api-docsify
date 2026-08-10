# RectChangeOptions

组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化返回的值及变化原因。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-uiExtension-interface RectChangeOptions--><!--Device-uiExtension-interface RectChangeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiExtension } from 'kits/@kit.ArkUI';
```

## reason

```TypeScript
reason: RectChangeReason
```

组件矩形变化的原因。

**Type:** [RectChangeReason](arkts-arkui-uiextension-rectchangereason-e.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-RectChangeOptions-reason: RectChangeReason--><!--Device-RectChangeOptions-reason: RectChangeReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rect

```TypeScript
rect: window.Rect
```

组件矩形变化后的值。

**Type:** window.Rect

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-RectChangeOptions-rect: window.Rect--><!--Device-RectChangeOptions-rect: window.Rect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

