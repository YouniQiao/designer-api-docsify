# DialogPresenter

Provides unified dialog APIs.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-unnamed-export class DialogPresenter--><!--Device-unnamed-export class DialogPresenter-End-->

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

## dismiss

```TypeScript
dismiss(target: int | ComponentContent<Object>): Promise<void>
```

Dismisses a dialog box. Accepts either the dialog ID (returned by present) or the ComponentContent reference.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-dismiss(target: int | ComponentContent<Object>): Promise<void>--><!--Device-DialogPresenter-dismiss(target: int | ComponentContent<Object>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | int \| ComponentContent&lt;Object&gt; | Yes | The dialog ID or ComponentContent to dismiss. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103301](../errorcode-promptAction.md#103301-dialog-content-error) | Dialog content error. The ComponentContent is incorrect. |
| [103303](../errorcode-promptAction.md#103303-custom-dialog-box-not-found) | Dialog content not found. The ComponentContent cannot be found. |

## present

```TypeScript
present(options?: dialog.DialogStyleOptions): Promise<DialogResult>
```

Presents a fixed-style dialog box.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-present(options?: dialog.DialogStyleOptions): Promise<DialogResult>--><!--Device-DialogPresenter-present(options?: dialog.DialogStyleOptions): Promise<DialogResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | dialog.DialogStyleOptions | No | Dialog options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DialogResult](arkts-arkui-arkui-dialog-dialogresult-i.md)&gt; | Promise used to return the dialog result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 103306 | The dialog cannot be opened due to node mount failure. |
| 103308 | The dialog cannot be opened due to subwindow create failure. |

## present

```TypeScript
present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>
```

Presents a custom-style dialog box with the provided content. The content parameter accepts CustomBuilder or ComponentContent via union type: - CustomBuilder: Builder function for custom dialog content. - ComponentContent: ComponentContent supporting state-driven updates. isModal = true and showInSubWindow = true cannot be used at the same time.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>--><!--Device-DialogPresenter-present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | CustomBuilder \| [CustomBuilderWithId](arkts-arkui-custombuilderwithid-t.md) \| ComponentContent&lt;Object&gt; | Yes | Custom dialog content. |
| options | dialog.DialogCustomOptions | No | Custom dialog options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DialogResult](arkts-arkui-arkui-dialog-dialogresult-i.md)&gt; | Promise used to return the dialog result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103301](../errorcode-promptAction.md#103301-dialog-content-error) | Dialog content error. The ComponentContent is incorrect. |
| [103302](../errorcode-promptAction.md#103302-custom-dialog-box-already-exists) | Dialog content already exist. The ComponentContent has already been opened. |
| 103306 | The dialog cannot be opened due to node mount failure. |
| 103308 | The dialog cannot be opened due to subwindow create failure. |

## update

```TypeScript
update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>
```

Updates a presented custom dialog box.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>--><!--Device-DialogPresenter-update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;Object&gt; | Yes | The content used to identify the dialog. |
| options | dialog.DialogBaseOptions | No | Options to update. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103301](../errorcode-promptAction.md#103301-dialog-content-error) | Dialog content error. The ComponentContent is incorrect. |
| [103303](../errorcode-promptAction.md#103303-custom-dialog-box-not-found) | Dialog content not found. The ComponentContent cannot be found. |

