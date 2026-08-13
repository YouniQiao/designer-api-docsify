# CursorController

Provides the capability to set cursor styles. > **NOTE：**> > - The initial APIs of this class are supported since API version 12. > > - In the following API examples, you must first use [getCursorController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getCursorController) in > **UIContext** to obtain a **CursorController** instance, and then call the APIs using the obtained instance.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-export class CursorController--><!--Device-unnamed-export class CursorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## restoreDefault

```TypeScript
restoreDefault(): void
```

Restores the default cursor style.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CursorController-restoreDefault(): void--><!--Device-CursorController-restoreDefault(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCursor

```TypeScript
setCursor(value: PointerStyle): void
```

Sets the cursor style. > **NOTE：**> > This API does not take effect immediately. The cursor style will be updated in the next rendering frame.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CursorController-setCursor(value: PointerStyle): void--><!--Device-CursorController-setCursor(value: PointerStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PointerStyle](arkts-arkui-pointerstyle-t.md) | Yes |

## setCustomCursor

```TypeScript
setCustomCursor(value: image.PixelMap, focusX?: number, focusY?: number): void
```

Sets the custom cursor style. > **NOTE：**> > This API does not take effect immediately. The cursor style will be updated in the next rendering frame.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CursorController-setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void--><!--Device-CursorController-setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | image.PixelMap | Yes |
| [focusX](../../apis-input-kit/arkts-apis/arkts-input-pointer-customcursor-i.md) | number | No |
| [focusY](../../apis-input-kit/arkts-apis/arkts-input-pointer-customcursor-i.md) | number | No |
