# promptAction

This module provides API for creating and displaying toasts, dialog boxes, and action menus. > **NOTE：**> > - This module cannot be used in the file declaration of the [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md). In > other words, the APIs of this module can be used only after a component instance is created; they cannot be called > in the lifecycle of the UIAbility. > > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used > where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see > [UIContext](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md). It is recommended that you use the dialog box APIs provided by > **UIContext**<!--Del-->, except for UI-less scenarios such as > [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)<!--DelEnd-->.

**Since:** 9

<!--Device-unnamed-declare namespace promptAction--><!--Device-unnamed-declare namespace promptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [showToast](arkts-arkui-promptaction-showtoast-f.md) | Creates and displays a toast. > **NOTE：**> > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use showToast instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showToast** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 10, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. > > - The toast has a fixed style and does not support content customization. For specific supported capabilities, see ShowToastOptions. |
| [openToast](arkts-arkui-promptaction-opentoast-f.md) | Shows a toast. This API uses a promise to return the toast ID. > **NOTE：**> > - Subwindows with **showMode** set to **TOP_MOST** or **SYSTEM_TOP_MOST** do not support **openToast** in input > method type windows. For details, see the constraints in the input method framework > [createPanel](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) > . > > - Directly using **openToast** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the > [openToast](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-promptaction-c.md#opentoast) API through this object. |
| [closeToast](arkts-arkui-promptaction-closetoast-f.md) | Closes the specified toast. > **NOTE：**> > Directly using **closeToast** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the > [closeToast](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-promptaction-c.md#closetoast) API through this object. |
| [showDialog](arkts-arkui-promptaction-showdialog-f.md) | Creates and displays a dialog box. This API uses an asynchronous callback to return the result. > **NOTE：**> > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use showDialog instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showDialog** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 10, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. |
| [showDialog](arkts-arkui-promptaction-showdialog-f.md) | Creates and displays a dialog box in the given settings. This API uses a promise to return the result. > **NOTE：**> > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use showDialog instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showDialog** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 10, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. |
| [openCustomDialog](arkts-arkui-promptaction-opencustomdialog-f.md) | Opens a custom dialog box. This API uses a promise to return the result. <!--Del-->This API cannot be used in **ServiceExtension**.<!--DelEnd--> By default, the width of the dialog box in portrait mode is the width of the window where it is located minus the left and right margins (40 vp for 2-in-1 devices and 16 vp for other devices), and the maximum width is 400 vp. > **NOTE：**> > - This API is supported since API version 11 and deprecated since API version 18. You are advised to use openCustomDialog instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **openCustomDialog** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 12, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. |
| [closeCustomDialog](arkts-arkui-promptaction-closecustomdialog-f.md) | Closes the specified custom dialog box. > **NOTE：**> > - This API is supported since API version 11 and deprecated since API version 18. You are advised to use closeCustomDialog instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **closeCustomDialog** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 12, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. |
| [showActionMenu](arkts-arkui-promptaction-showactionmenu-f.md) | Creates and displays an action menu. This API uses an asynchronous callback to return the result. > **NOTE：**> > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use showActionMenu instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showActionMenu** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 11, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. |
| [showActionMenu](arkts-arkui-promptaction-showactionmenu-f.md) | Creates and displays an action menu in the given settings. This API uses a promise to return the result. > **NOTE：**> > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use showActionMenu instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showActionMenu** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 10, you can use the [getPromptAction](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md#getpromptaction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. |

### Classes

| Name | Description |
| --- | --- |
| [CommonController](arkts-arkui-promptaction-commoncontroller-c.md) | Implements a common controller for managing components related to **promptAction**. |
| [DialogController](arkts-arkui-promptaction-dialogcontroller-c.md) | Implements a custom dialog controller that inherits from [CommonController](arkts-arkui-promptaction-commoncontroller-c.md). It can be used as a member variable of **UIContext** to display custom dialog boxes. For specific usage, see the examples for [openCustomDialogWithController](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-promptaction-c.md#opencustomdialogwithcontroller) and [presentCustomDialog](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-promptaction-c.md#presentcustomdialog). |

### Interfaces

| Name | Description |
| --- | --- |
| [ShowToastOptions](arkts-arkui-promptaction-showtoastoptions-i.md) |  |
| [Button](arkts-arkui-promptaction-button-i.md) | Describes the menu item button in the action menu. |
| [ShowDialogSuccessResponse](arkts-arkui-promptaction-showdialogsuccessresponse-i.md) | Describes the dialog box response result. |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | Describes the options for showing the dialog box. |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) | Defines the options of the dialog box. |
| [CustomDialogOptions](arkts-arkui-promptaction-customdialogoptions-i.md) | Extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) to provide enhanced customization capabilities for the dialog box. |
| [DialogOptions](arkts-arkui-promptaction-dialogoptions-i.md) | Extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) to provide enhanced customization capabilities for the dialog box. |
| [ActionMenuSuccessResponse](arkts-arkui-promptaction-actionmenusuccessresponse-i.md) | Describes the action menu response result. |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i.md) | Describes the options for showing the action menu. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i-sys.md) | Describes the options for showing the dialog box. |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i-sys.md) | Defines the options of the dialog box. |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i-sys.md) | Describes the options for showing the action menu. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e.md) | Enumerates display modes for toasts. By default, the toast is displayed within the application and supports display in subwindows. |
| [CommonState](arkts-arkui-promptaction-commonstate-e.md) | Enumerates states of the custom dialog box. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e-sys.md) | Enumerates display modes for toasts. By default, the toast is displayed within the application and supports display in subwindows. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [DialogOptionsCornerRadius](arkts-arkui-promptaction-dialogoptionscornerradius-t.md) | Defines the allowed data types for specifying the background corner radius of a dialog box. |
| [DialogOptionsBorderWidth](arkts-arkui-promptaction-dialogoptionsborderwidth-t.md) | Defines the allowed data types for specifying the background border width of a dialog box. |
| [DialogOptionsBorderColor](arkts-arkui-promptaction-dialogoptionsbordercolor-t.md) | Defines the allowed data types for specifying the background border color of a dialog box. |
| [DialogOptionsBorderStyle](arkts-arkui-promptaction-dialogoptionsborderstyle-t.md) | Defines the allowed data types for specifying the background border style of a dialog box. |
| [DialogOptionsShadow](arkts-arkui-promptaction-dialogoptionsshadow-t.md) | Defines the allowed data types for specifying the background shadow of a dialog box. |

