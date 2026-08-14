# Magnifier

Provides the capability of displaying and hiding of the magnifier. The magnifier enlarges the component content for you to view the component details. > **NOTE：**> > - In the following API examples, you must first use [getMagnifier()](arkts-arkui-arkui-uicontext-uicontext-c.md#getMagnifier) in **UIContext** > to obtain a **Magnifier** instance, and then call the APIs using the obtained instance. > > - The magnifier capability of this class does not affect that of text components. For text components, you are > advised to use the built-in magnifier capability.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

<!--Device-unnamed-export class Magnifier--><!--Device-unnamed-export class Magnifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar } from 'AtomicServiceBar';
import { ComponentUtils } from 'ComponentUtils';
import { ContextMenuController } from 'ContextMenuController';
import { CursorController } from 'CursorController';
import { DialogPresenter } from 'DialogPresenter';
import { DragController } from 'DragController';
import { Font } from 'Font';
import { KeyboardAvoidMode } from 'KeyboardAvoidMode';
import { MediaQuery } from 'MediaQuery';
import { OverlayManager } from 'OverlayManager';
import { PromptAction } from 'PromptAction';
import { Router } from 'Router';
import { UIContext } from 'UIContext';
import { UIInspector } from 'UIInspector';
import { UIObserver } from 'UIObserver';
import { PageInfo } from 'PageInfo';
import { SwiperDynamicSyncScene } from 'SwiperDynamicSyncScene';
import { SwiperDynamicSyncSceneType } from 'SwiperDynamicSyncSceneType';
import { MarqueeDynamicSyncScene } from 'MarqueeDynamicSyncScene';
import { MarqueeDynamicSyncSceneType } from 'MarqueeDynamicSyncSceneType';
import { MeasureUtils } from 'MeasureUtils';
import { FrameCallback } from 'FrameCallback';
import { OverlayManagerOptions } from 'OverlayManagerOptions';
import { TargetInfo } from 'TargetInfo';
import { TextMenuController } from 'TextMenuController';
import { NodeIdentity } from 'NodeIdentity';
import { NodeRenderState } from 'NodeRenderState';
import { NodeRenderStateChangeCallback } from 'NodeRenderStateChangeCallback';
import { Magnifier } from 'Magnifier';
import { ResolvedUIContext } from 'ResolvedUIContext';
import { TextSelectionClearPolicy } from 'TextSelectionClearPolicy';
import { CustomKeyboardContinueFeature } from 'CustomKeyboardContinueFeature';
```

## bind

```TypeScript
bind(id: string): void
```

Binds the magnifier to the component with the specified ID. > **NOTE：**> > Obtain the Magnifier instance by using the getMagnifier() method in UIContext.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Magnifier-bind(id: string): void--><!--Device-Magnifier-bind(id: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Component ID, which can be set through the universal attribute id or key. If the component ID is an empty string or no component is found based on the specified ID, the magnifier is not displayed. |

## show

```TypeScript
show(x: number, y: number): void
```

Sets the position of the component content displayed by the magnifier relative to the upper left corner of the component. After the setting is successful, the magnifier displays the content centered at the coordinate point. > **NOTE：**> > When the content of the component bound to the magnifier changes, the magnifier does not automatically update the > displayed content. You need to call the **show** API to update the displayed content of the magnifier.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Magnifier-show(x: number, y: number): void--><!--Device-Magnifier-show(x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | Horizontal coordinate of the component content displayed by the magnifier, relative to the component itself, in vp. If the coordinate value is greater than the component width or less than 0, the magnifier is not displayed. If the value is **undefined**, the current display status of the magnifier is retained. |
| y | number | Yes | Vertical coordinate of the component content displayed by the magnifier, relative to the component itself, in vp. If the coordinate value is greater than the component height or less than 0, the magnifier is not displayed. If the value is **undefined**, the current display status of the magnifier is retained. |

## unbind

```TypeScript
unbind(): void
```

Unbinds the magnifier from the current component.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Magnifier-unbind(): void--><!--Device-Magnifier-unbind(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

