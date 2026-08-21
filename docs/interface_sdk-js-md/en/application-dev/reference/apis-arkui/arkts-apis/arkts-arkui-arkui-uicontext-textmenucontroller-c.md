# TextMenuController

Provides the capability to control text menus.

> **NOTE：**
> 
> - In the following non-static API examples, you must first use &gt; [getTextMenuController()](arkts-arkui-arkui-uicontext-uicontext-c.md#gettextmenucontroller) in **UIContext** to obtain a &gt; **TextMenuController** instance, and then call the APIs using the obtained instance.

**Since:** 16

<!--Device-unnamed-export class TextMenuController--><!--Device-unnamed-export class TextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## disableMenuItems

```TypeScript
static disableMenuItems(items: Array<TextMenuItemId>): void
```

Disables specified system service menu items in the text selection menu.

> **NOTE：**
> 
> - This API takes effect globally for the entire application process after being called.
> 
> - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md).
> 
> - After this API is called, the editMenuOptions API of text components &gt; will be affected. The parameter list of its onCreateMenu callback will not &gt; include the disabled menu options.
> 
> - Components involving text selection menus include the following: Text, &gt; TextArea, TextInput, &gt; Search, RichEditor, and &gt; Web.
> 
> - System service menu items refer to menu items other than copy, cut, select all, and paste in &gt; TextMenuItemId.
> 
> - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set &gt; **disableSystemServiceMenuItems** takes precedence.
> 
> - This API takes effect globally, and multiple calls are subject to the last call.
> 
> - Disabling a first-level menu item will also disable all its second-level menu items. For example, disabling the &gt; first-level menu item **autoFill** (parent item) in TextMenuItemId will simultaneously &gt; disable the second-level menu item **passwordVault** (child item) in **TextMenuItemId**.
> 
> - Disabling individual second-level menu items is not supported. If required, this can be achieved by disabling &gt; the corresponding first-level menu item.
> 
> - Disabled menus can be restored in the following ways:
> 
> - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore.
> 
> - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore.
> 
> - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and &gt; the latter to an empty array to restore.

**Since:** 20

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

Disables all system service menu items in the text selection menu.

> **NOTE：**
> 
> - This API takes effect globally for the entire application process after being called.
> 
> - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md).
> 
> - After this API is called, the editMenuOptions API of text components &gt; will be affected. The parameter list of its onCreateMenu callback will not &gt; include the disabled menu options.
> 
> - Components involving text selection menus include the following: Text, &gt; TextArea, TextInput, &gt; Search, RichEditor, and &gt; Web.
> 
> - System service menu items refer to menu items other than copy, cut, select all, and paste in &gt; TextMenuItemId.
> 
> - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set &gt; **disableSystemServiceMenuItems** takes precedence.
> 
> - This API takes effect globally, and multiple calls are subject to the last call.
> 
> - Disabled menus can be restored in the following ways:
> 
> - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore.
> 
> - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore.
> 
> - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and &gt; the latter to an empty array to restore.

**Since:** 20

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 16.

<!--Device-TextMenuController-setMenuOptions(options: TextMenuOptions): void--><!--Device-TextMenuController-setMenuOptions(options: TextMenuOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | TextMenuOptions | Yes | Menu options. <br>Default value: {showMode: TextMenuShowMode.DEFAULT}. |

