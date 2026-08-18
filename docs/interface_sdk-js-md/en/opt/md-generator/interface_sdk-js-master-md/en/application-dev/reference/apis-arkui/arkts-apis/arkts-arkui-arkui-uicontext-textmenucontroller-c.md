# TextMenuController

Provides the capability to control text menus. > **NOTE：**> > - In the following non-static API examples, you must first use > [getTextMenuController()](arkts-arkui-arkui-uicontext-uicontext-c.md#gettextmenucontroller) in **UIContext** to obtain a > **TextMenuController** instance, and then call the APIs using the obtained instance.

**Since:** 16

<!--Device-unnamed-export class TextMenuController--><!--Device-unnamed-export class TextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## disableMenuItems

```TypeScript
static disableMenuItems(items: Array<TextMenuItemId>): void
```

Disables specified system service menu items in the text selection menu. > **NOTE：**> > - This API takes effect globally for the entire application process after being called. > > - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#uiability). > > - After this API is called, the editMenuOptions API of text components > will be affected. The parameter list of its onCreateMenu callback will not > include the disabled menu options. > > - Components involving text selection menus include the following: Text, > TextArea, TextInput, > Search, RichEditor, and > Web. > > - System service menu items refer to menu items other than copy, cut, select all, and paste in > [TextMenuItemId](arkts-arkui-textmenuitemid-c.md#textmenuitemid). > > - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set > **disableSystemServiceMenuItems** takes precedence. > > - This API takes effect globally, and multiple calls are subject to the last call. > > - Disabling a first-level menu item will also disable all its second-level menu items. For example, disabling the > first-level menu item **autoFill** (parent item) in [TextMenuItemId](arkts-arkui-textmenuitemid-c.md#textmenuitemid) will simultaneously > disable the second-level menu item **passwordVault** (child item) in **TextMenuItemId**. > > - Disabling individual second-level menu items is not supported. If required, this can be achieved by disabling > the corresponding first-level menu item. > > - Disabled menus can be restored in the following ways: > > - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore. > > - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore. > > - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and > the latter to an empty array to restore.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextMenuController-static disableMenuItems(items: Array<TextMenuItemId>): void--><!--Device-TextMenuController-static disableMenuItems(items: Array<TextMenuItemId>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | Array&lt;[TextMenuItemId](arkts-arkui-textmenuitemid-c.md)&gt; | Yes |

## disableSystemServiceMenuItems

```TypeScript
static disableSystemServiceMenuItems(disable: boolean): void
```

Disables all system service menu items in the text selection menu. > **NOTE：**> > - This API takes effect globally for the entire application process after being called. > > - This API can be used in [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#uiability). > > - After this API is called, the editMenuOptions API of text components > will be affected. The parameter list of its onCreateMenu callback will not > include the disabled menu options. > > - Components involving text selection menus include the following: Text, > TextArea, TextInput, > Search, RichEditor, and > Web. > > - System service menu items refer to menu items other than copy, cut, select all, and paste in > [TextMenuItemId](arkts-arkui-textmenuitemid-c.md#textmenuitemid). > > - When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set > **disableSystemServiceMenuItems** takes precedence. > > - This API takes effect globally, and multiple calls are subject to the last call. > > - Disabled menus can be restored in the following ways: > > - If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore. > > - If only **disableMenuItems** is used to disable menus, set it to an empty array to restore. > > - If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and > the latter to an empty array to restore.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextMenuController-static disableSystemServiceMenuItems(disable: boolean): void--><!--Device-TextMenuController-static disableSystemServiceMenuItems(disable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| disable | boolean | Yes |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextMenuOptions](arkts-arkui-textmenuoptions-i.md) | Yes |
