# CursorController

Provides the capability to set cursor styles.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - In the following API examples, you must first use [getCursorController()](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md#getcursorcontroller) in
> **UIContext** to obtain a **CursorController** instance, and then call the APIs using the obtained instance.

**Since:** 12

<!--Device-unnamed-export class CursorController--><!--Device-unnamed-export class CursorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## restoreDefault

```TypeScript
restoreDefault(): void
```

Restores the default cursor style.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CursorController-restoreDefault(): void--><!--Device-CursorController-restoreDefault(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

In this example, the restoreDefault API of CursorController is used to restore the cursor style when the cursor moves out of the green frame.

```TypeScript
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Green).position({x: 150 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.EAST);
          } else {
            console.info("restoreDefault");
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```

## setCursor

```TypeScript
setCursor(value: PointerStyle): void
```

Sets the cursor style.

> **NOTE：**
> 
> This API does not take effect immediately. The cursor style will be updated in the next rendering frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CursorController-setCursor(value: PointerStyle): void--><!--Device-CursorController-setCursor(value: PointerStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PointerStyle](../../apis-default/arkts-apis/arkts-pointerstyle-t.md) | Yes | Pointer style. |

**Examples**

In this example, the setCursor API of CursorController is used to set the cursor style to PointerStyle.WEST when the cursor moves into the blue frame.

```TypeScript
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Blue).position({x: 100 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.WEST);
          } else {
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```

## setCustomCursor

```TypeScript
setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void
```

Sets the custom cursor style.

> **NOTE：**
> 
> This API does not take effect immediately. The cursor style will be updated in the next rendering frame.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CursorController-setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void--><!--Device-CursorController-setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | image.PixelMap | Yes | Pixel map of the custom mouse cursor style. |
| focusX | int | No | X coordinate of the custom cursor's hotspot. The hotspot refers to the actual location where the click occurs.<br>Default value: **0**<br>Unit: px<br>Value range: [0, +∞) |
| focusY | int | No | Y coordinate of the custom cursor's hotspot.<br>Default value: **0**<br>Unit: px<br>Value range: [0, +∞) |

