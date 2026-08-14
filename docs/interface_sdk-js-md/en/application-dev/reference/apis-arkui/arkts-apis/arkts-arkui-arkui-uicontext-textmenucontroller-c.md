# TextMenuController

Provides the capability to control text menus. > **NOTE：**> > - In the following non-static API examples, you must first use > [getTextMenuController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getTextMenuController) in **UIContext** to obtain a > **TextMenuController** instance, and then call the APIs using the obtained instance.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

**Deprecated since:** -1

<!--Device-unnamed-export class TextMenuController--><!--Device-unnamed-export class TextMenuController-End-->

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

## disableMenuItems

```TypeScript
static disableMenuItems(items: Array<TextMenuItemId>): void
```

Disables specified system service menu items in the text selection menu. > **NOTE：**> > - This API takes effect globally for the entire application process after being called. > > - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility). > > - After this API is called, the editMenuOptions API of text components > will be affected. The parameter list of its onCreateMenu callback will not > include the disabled menu options. > > - Components involving text selection menus include the following: Text, > TextArea, TextInput, > Search, RichEditor, and > Web. > > - System service menu items refer to menu items other than copy, cut, select all, and paste in > TextMenuItemId. > > - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set > **disableSystemServiceMenuItems** takes precedence. > > - This API takes effect globally, and multiple calls are subject to the last call. > > - Disabling a first-level menu item will also disable all its second-level menu items. For example, disabling the > first-level menu item **autoFill** (parent item) in TextMenuItemId will simultaneously > disable the second-level menu item **passwordVault** (child item) in **TextMenuItemId**. > > - Disabling individual second-level menu items is not supported. If required, this can be achieved by disabling > the corresponding first-level menu item. > > - Disabled menus can be restored in the following ways: > > - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore. > > - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore. > > - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and > the latter to an empty array to restore.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextMenuController-static disableMenuItems(items: Array<TextMenuItemId>): void--><!--Device-TextMenuController-static disableMenuItems(items: Array<TextMenuItemId>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;TextMenuItemId&gt; | Yes | List of menu items to disable. |

## disableSystemServiceMenuItems

```TypeScript
static disableSystemServiceMenuItems(disable: boolean): void
```

Disables all system service menu items in the text selection menu. > **NOTE：**> > - This API takes effect globally for the entire application process after being called. > > - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility). > > - After this API is called, the editMenuOptions API of text components > will be affected. The parameter list of its onCreateMenu callback will not > include the disabled menu options. > > - Components involving text selection menus include the following: Text, > TextArea, TextInput, > Search, RichEditor, and > Web. > > - System service menu items refer to menu items other than copy, cut, select all, and paste in > TextMenuItemId. > > - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set > **disableSystemServiceMenuItems** takes precedence. > > - This API takes effect globally, and multiple calls are subject to the last call. > > - Disabled menus can be restored in the following ways: > > - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore. > > - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore. > > - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and > the latter to an empty array to restore.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextMenuController-static disableSystemServiceMenuItems(disable: boolean): void--><!--Device-TextMenuController-static disableSystemServiceMenuItems(disable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disable | boolean | Yes | Whether to disable system service menu items. The value **true** means to disable system service menu items, and **false** means the opposite. |

## setMenuOptions

```TypeScript
setMenuOptions(options: TextMenuOptions): void
```

Sets menu options.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 16.

<!--Device-TextMenuController-setMenuOptions(options: TextMenuOptions): void--><!--Device-TextMenuController-setMenuOptions(options: TextMenuOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | TextMenuOptions | Yes | Menu options. <br>Default value: {showMode: TextMenuShowMode.DEFAULT}. |

