# TextMenuController

Provides the capability to control text menus.

> **NOTE：**&gt;
> - In the following non-static API examples, you must first use
> [getTextMenuController()](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md#gettextmenucontroller) in **UIContext** to obtain a
> **TextMenuController** instance, and then call the APIs using the obtained instance.

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

> **NOTE：**&gt;
> - This API takes effect globally for the entire application process after being called.&gt;
> - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md).&gt;
> - After this API is called, the editMenuOptions API of text components
> will be affected. The parameter list of its onCreateMenu callback will not
> include the disabled menu options.&gt;
> - Components involving text selection menus include the following: Text,
> TextArea, TextInput,
> Search, RichEditor, and
> Web.&gt;
> - System service menu items refer to menu items other than copy, cut, select all, and paste in
> TextMenuItemId.&gt;
> - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set
> **disableSystemServiceMenuItems** takes precedence.&gt;
> - This API takes effect globally, and multiple calls are subject to the last call.&gt;
> - Disabling a first-level menu item will also disable all its second-level menu items. For example, disabling the
> first-level menu item **autoFill** (parent item) in TextMenuItemId will simultaneously
> disable the second-level menu item **passwordVault** (child item) in **TextMenuItemId**.&gt;
> - Disabling individual second-level menu items is not supported. If required, this can be achieved by disabling
> the corresponding first-level menu item.&gt;
> - Disabled menus can be restored in the following ways:&gt;
> - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore.&gt;
> - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore.&gt;
> - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and
> the latter to an empty array to restore.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextMenuController-static disableMenuItems(items: Array<TextMenuItemId>): void--><!--Device-TextMenuController-static disableMenuItems(items: Array<TextMenuItemId>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;TextMenuItemId&gt; | Yes | List of menu items to disable. |

**Examples**

```TypeScript
import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // Disable search and translate menu items.
    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE])
  }

  aboutToDisappear(): void {
    // Restore system service menu items.
    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "This is a TextInput. Long press to display the text selection menu." })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                // menuItems does not contain search and translate options.
                return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

## disableSystemServiceMenuItems

```TypeScript
static disableSystemServiceMenuItems(disable: boolean): void
```

Disables all system service menu items in the text selection menu.

> **NOTE：**&gt;
> - This API takes effect globally for the entire application process after being called.&gt;
> - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md).&gt;
> - After this API is called, the editMenuOptions API of text components
> will be affected. The parameter list of its onCreateMenu callback will not
> include the disabled menu options.&gt;
> - Components involving text selection menus include the following: Text,
> TextArea, TextInput,
> Search, RichEditor, and
> Web.&gt;
> - System service menu items refer to menu items other than copy, cut, select all, and paste in
> TextMenuItemId.&gt;
> - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set
> **disableSystemServiceMenuItems** takes precedence.&gt;
> - This API takes effect globally, and multiple calls are subject to the last call.&gt;
> - Disabled menus can be restored in the following ways:&gt;
> - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore.&gt;
> - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore.&gt;
> - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and
> the latter to an empty array to restore.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextMenuController-static disableSystemServiceMenuItems(disable: boolean): void--><!--Device-TextMenuController-static disableSystemServiceMenuItems(disable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disable | boolean | Yes | Whether to disable system service menu items. The value **true** means to disable system service menu items, and **false** means the opposite. |

**Examples**

```TypeScript
import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // Disable all system service menu items.
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // Restore system service menu items when the page disappears.
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "This is a TextInput. Long press to display the text selection menu." })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                // menuItems does not contain the disabled system menu items.
                return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

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

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // Set the UIContext to preferentially display the context menu on selection in a separate window.
    this.getUIContext()
      .getTextMenuController()
      .setMenuOptions(
        {
          showMode: TextMenuShowMode.PREFER_WINDOW
        }
      );
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "This is a TextInput. Long press to display the text selection menu." })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })

        Text("This is a Text. Long press to display the text selection menu.")
          .height(60)
          .copyOption(CopyOptions.InApp)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
      }.width('100%')
    }
    .height('100%')
  }
}
```

