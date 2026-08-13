# promptAction

This module provides API for creating and displaying toasts, dialog boxes, and action menus. > **NOTE：**> > - This module cannot be used in the file declaration of the [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility). In > other words, the APIs of this module can be used only after a component instance is created; they cannot be called > in the lifecycle of the UIAbility. > > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used > where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext). It is recommended that you use the dialog box APIs provided by > **UIContext**&lt;!--Del--&gt;, except for UI-less scenarios such as > [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)&lt;!--DelEnd--&gt;.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare namespace promptAction--><!--Device-unnamed-declare namespace promptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [showToast](arkts-arkui-promptaction-showtoast-f.md#showToast) |
| [openToast](arkts-arkui-promptaction-opentoast-f.md#openToast) |
| [closeToast](arkts-arkui-promptaction-closetoast-f.md#closeToast) |
| [showDialog](arkts-arkui-promptaction-showdialog-f.md#showDialog) |
| [showDialog](arkts-arkui-promptaction-showdialog-f.md#showDialog) |
| [openCustomDialog](arkts-arkui-promptaction-opencustomdialog-f.md#openCustomDialog) |
| [closeCustomDialog](arkts-arkui-promptaction-closecustomdialog-f.md#closeCustomDialog) |
| [showActionMenu](arkts-arkui-promptaction-showactionmenu-f.md#showActionMenu) |
| [showActionMenu](arkts-arkui-promptaction-showactionmenu-f.md#showActionMenu) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CommonController](arkts-arkui-promptaction-commoncontroller-c.md) |
| [DialogController](arkts-arkui-promptaction-dialogcontroller-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ShowToastOptions](arkts-arkui-promptaction-showtoastoptions-i.md) |
| [Button](arkts-arkui-promptaction-button-i.md) |
| [ShowDialogSuccessResponse](arkts-arkui-promptaction-showdialogsuccessresponse-i.md) |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) |
| [CustomDialogOptions](arkts-arkui-promptaction-customdialogoptions-i.md) |
| [DialogOptions](arkts-arkui-promptaction-dialogoptions-i.md) |
| [ActionMenuSuccessResponse](arkts-arkui-promptaction-actionmenusuccessresponse-i.md) |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i-sys.md) |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i-sys.md) |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e.md) |
| [CommonState](arkts-arkui-promptaction-commonstate-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DialogOptionsCornerRadius](arkts-arkui-promptaction-dialogoptionscornerradius-t.md) |
| [DialogOptionsBorderWidth](arkts-arkui-promptaction-dialogoptionsborderwidth-t.md) |
| [DialogOptionsBorderColor](arkts-arkui-promptaction-dialogoptionsbordercolor-t.md) |
| [DialogOptionsBorderStyle](arkts-arkui-promptaction-dialogoptionsborderstyle-t.md) |
| [DialogOptionsShadow](arkts-arkui-promptaction-dialogoptionsshadow-t.md) |
