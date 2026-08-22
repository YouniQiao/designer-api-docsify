# PromptAction

class PromptAction

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class PromptAction--><!--Device-unnamed-export declare class PromptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## closeCustomDialog

```TypeScript
closeCustomDialog<T extends Object>(dialogContent: ComponentContent<T>): Promise<void>
```

Close the custom dialog with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-closeCustomDialog<T extends Object>(dialogContent: ComponentContent<T>): Promise<void>--><!--Device-PromptAction-closeCustomDialog<T extends Object>(dialogContent: ComponentContent<T>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogContent | ComponentContent&lt;T&gt; | Yes | the content of custom dialog. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103303](../../apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) | The ComponentContent cannot be found. |

## closeCustomDialog

```TypeScript
closeCustomDialog(dialogId: int): void
```

Close the custom dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-closeCustomDialog(dialogId: int): void--><!--Device-PromptAction-closeCustomDialog(dialogId: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogId | int | Yes | the dialog id that returned by openCustomDialog. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## closeMenu

```TypeScript
closeMenu<T extends Object>(content: ComponentContent<T>): Promise<void>
```

Close menu with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-closeMenu<T extends Object>(content: ComponentContent<T>): Promise<void>--><!--Device-PromptAction-closeMenu<T extends Object>(content: ComponentContent<T>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103303](../../apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) | The ComponentContent cannot be found. |

## closePopup

```TypeScript
closePopup<T extends Object>(content: ComponentContent<T>): Promise<void>
```

Close popup with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-closePopup<T extends Object>(content: ComponentContent<T>): Promise<void>--><!--Device-PromptAction-closePopup<T extends Object>(content: ComponentContent<T>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content of popup. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103303](../../apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) | The ComponentContent cannot be found. |

## closeToast

```TypeScript
closeToast(toastId: int): void
```

Close the notification text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-closeToast(toastId: int): void--><!--Device-PromptAction-closeToast(toastId: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toastId | int | Yes | the toast id that returned by openToast. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [103401](../../apis-arkui/errorcode-promptAction.md#103401-toast-not-found) | Cannot find the toast. |

## getBottomOrder

```TypeScript
getBottomOrder(): LevelOrder | undefined
```

Get order value of bottom dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-getBottomOrder(): LevelOrder | undefined--><!--Device-PromptAction-getBottomOrder(): LevelOrder | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LevelOrder](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelorder-c.md) \| undefined | the display order, or undefined if there is no dialog. |

## getTopOrder

```TypeScript
getTopOrder(): LevelOrder | undefined
```

Get order value of top dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-getTopOrder(): LevelOrder | undefined--><!--Device-PromptAction-getTopOrder(): LevelOrder | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LevelOrder](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelorder-c.md) \| undefined | the display order, or undefined if there is no dialog. |

## openCustomDialog

```TypeScript
openCustomDialog<T extends Object>(dialogContent: ComponentContent<T>,
    options?: promptAction.BaseDialogOptions): Promise<void>
```

Open the custom dialog with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-openCustomDialog<T extends Object>(dialogContent: ComponentContent<T>,    options?: promptAction.BaseDialogOptions): Promise<void>--><!--Device-PromptAction-openCustomDialog<T extends Object>(dialogContent: ComponentContent<T>,    options?: promptAction.BaseDialogOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogContent | ComponentContent&lt;T&gt; | Yes | the content of custom dialog. |
| options | promptAction.BaseDialogOptions | No | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103302](../../apis-arkui/errorcode-promptAction.md#103302-custom-dialog-box-already-exists) | Dialog content already exists. |

## openCustomDialog

```TypeScript
openCustomDialog(options: promptAction.CustomDialogOptions): Promise<int>
```

Open the custom dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-openCustomDialog(options: promptAction.CustomDialogOptions): Promise<int>--><!--Device-PromptAction-openCustomDialog(options: promptAction.CustomDialogOptions): Promise<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.CustomDialogOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | return the dialog id that will be used by closeCustomDialog. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## openCustomDialogWithController

```TypeScript
openCustomDialogWithController<T extends Object>(dialogContent: ComponentContent<T>,
    controller: promptAction.DialogController,
    options?: promptAction.BaseDialogOptions): Promise<void>
```

Open the custom dialog with frameNode and controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-openCustomDialogWithController<T extends Object>(dialogContent: ComponentContent<T>,    controller: promptAction.DialogController,    options?: promptAction.BaseDialogOptions): Promise<void>--><!--Device-PromptAction-openCustomDialogWithController<T extends Object>(dialogContent: ComponentContent<T>,    controller: promptAction.DialogController,    options?: promptAction.BaseDialogOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogContent | ComponentContent&lt;T&gt; | Yes | the content of custom dialog. |
| controller | promptAction.DialogController | Yes | Dialog controller. |
| options | promptAction.BaseDialogOptions | No | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103302](../../apis-arkui/errorcode-promptAction.md#103302-custom-dialog-box-already-exists) | Dialog content already exists. |

## openMenu

```TypeScript
openMenu<T extends Object>(content: ComponentContent<T>, target: TargetInfo, options?: MenuOptions): Promise<void>
```

Open menu with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-openMenu<T extends Object>(content: ComponentContent<T>, target: TargetInfo, options?: MenuOptions): Promise<void>--><!--Device-PromptAction-openMenu<T extends Object>(content: ComponentContent<T>, target: TargetInfo, options?: MenuOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content of menu. |
| target | [TargetInfo](arkts-arkui-uicontext-targetinfo-i.md) | Yes | The target of menu. |
| options | MenuOptions | No | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The content is incorrect. |
| [103302](../../apis-arkui/errorcode-promptAction.md#103302-custom-dialog-box-already-exists) | The content already exists. |
| [103304](../../apis-arkui/errorcode-promptAction.md#103304-target-id-not-found) | The target does not exist. |
| [103305](../../apis-arkui/errorcode-promptAction.md#103305-node-not-mounted) | The target node is not in the component tree. |

## openPopup

```TypeScript
openPopup<T extends Object>(content: ComponentContent<T>, target: TargetInfo,
    options?: PopupCommonOptions): Promise<void>
```

Open popup with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-openPopup<T extends Object>(content: ComponentContent<T>, target: TargetInfo,    options?: PopupCommonOptions): Promise<void>--><!--Device-PromptAction-openPopup<T extends Object>(content: ComponentContent<T>, target: TargetInfo,    options?: PopupCommonOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content of popup. |
| target | [TargetInfo](arkts-arkui-uicontext-targetinfo-i.md) | Yes | The target of popup. |
| options | PopupCommonOptions | No | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The content is incorrect. |
| [103302](../../apis-arkui/errorcode-promptAction.md#103302-custom-dialog-box-already-exists) | The content already exists. |
| [103304](../../apis-arkui/errorcode-promptAction.md#103304-target-id-not-found) | The target does not exist. |
| [103305](../../apis-arkui/errorcode-promptAction.md#103305-node-not-mounted) | The target node is not in the component tree. |

## openToast

```TypeScript
openToast(options: promptAction.ShowToastOptions): Promise<int>
```

Displays the notification text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-openToast(options: promptAction.ShowToastOptions): Promise<int>--><!--Device-PromptAction-openToast(options: promptAction.ShowToastOptions): Promise<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.ShowToastOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | return the toast id that can be used by closeToast. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## presentCustomDialog

```TypeScript
presentCustomDialog(builder: CustomBuilder | CustomBuilderT<int>, controller?: promptAction.DialogController,
    options?: promptAction.DialogOptions): Promise<int>
```

Present the custom dialog with controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-presentCustomDialog(builder: CustomBuilder | CustomBuilderT<int>, controller?: promptAction.DialogController,    options?: promptAction.DialogOptions): Promise<int>--><!--Device-PromptAction-presentCustomDialog(builder: CustomBuilder | CustomBuilderT<int>, controller?: promptAction.DialogController,    options?: promptAction.DialogOptions): Promise<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | CustomBuilder \| CustomBuilderT&lt;int&gt; | Yes | Dialog builder. |
| controller | promptAction.DialogController | No | Dialog controller. |
| options | promptAction.DialogOptions | No | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | return the dialog id that will be used by closeCustomDialog. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## showActionMenu

```TypeScript
showActionMenu(options: promptAction.ActionMenuOptions,
    callback: AsyncCallback<promptAction.ActionMenuSuccessResponse>): void
```

Displays the menu.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-showActionMenu(options: promptAction.ActionMenuOptions,    callback: AsyncCallback<promptAction.ActionMenuSuccessResponse>): void--><!--Device-PromptAction-showActionMenu(options: promptAction.ActionMenuOptions,    callback: AsyncCallback<promptAction.ActionMenuSuccessResponse>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.ActionMenuOptions | Yes | Options. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;promptAction.ActionMenuSuccessResponse&gt; | Yes | the callback of showActionMenu. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## showActionMenu

```TypeScript
showActionMenu(options: promptAction.ActionMenuOptions): Promise<promptAction.ActionMenuSuccessResponse>
```

Displays the menu.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-showActionMenu(options: promptAction.ActionMenuOptions): Promise<promptAction.ActionMenuSuccessResponse>--><!--Device-PromptAction-showActionMenu(options: promptAction.ActionMenuOptions): Promise<promptAction.ActionMenuSuccessResponse>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.ActionMenuOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;promptAction.ActionMenuSuccessResponse&gt; | callback - the callback of showActionMenu. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## showDialog

```TypeScript
showDialog(options: promptAction.ShowDialogOptions,
    callback: AsyncCallback<promptAction.ShowDialogSuccessResponse>): void
```

Displays the dialog box.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-showDialog(options: promptAction.ShowDialogOptions,    callback: AsyncCallback<promptAction.ShowDialogSuccessResponse>): void--><!--Device-PromptAction-showDialog(options: promptAction.ShowDialogOptions,    callback: AsyncCallback<promptAction.ShowDialogSuccessResponse>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.ShowDialogOptions | Yes | Options. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;promptAction.ShowDialogSuccessResponse&gt; | Yes | the callback of showDialog. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## showDialog

```TypeScript
showDialog(options: promptAction.ShowDialogOptions): Promise<promptAction.ShowDialogSuccessResponse>
```

Displays the dialog box.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-showDialog(options: promptAction.ShowDialogOptions): Promise<promptAction.ShowDialogSuccessResponse>--><!--Device-PromptAction-showDialog(options: promptAction.ShowDialogOptions): Promise<promptAction.ShowDialogSuccessResponse>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.ShowDialogOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;promptAction.ShowDialogSuccessResponse&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## showToast

```TypeScript
showToast(options: promptAction.ShowToastOptions): void
```

Displays the notification text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-showToast(options: promptAction.ShowToastOptions): void--><!--Device-PromptAction-showToast(options: promptAction.ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | promptAction.ShowToastOptions | Yes | Options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

## updateCustomDialog

```TypeScript
updateCustomDialog<T extends Object>(dialogContent: ComponentContent<T>,
    options: promptAction.BaseDialogOptions): Promise<void>
```

Update the custom dialog with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-updateCustomDialog<T extends Object>(dialogContent: ComponentContent<T>,    options: promptAction.BaseDialogOptions): Promise<void>--><!--Device-PromptAction-updateCustomDialog<T extends Object>(dialogContent: ComponentContent<T>,    options: promptAction.BaseDialogOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogContent | ComponentContent&lt;T&gt; | Yes | the content of custom dialog. |
| options | promptAction.BaseDialogOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103303](../../apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) | The ComponentContent cannot be found. |

## updateMenu

```TypeScript
updateMenu<T extends Object>(content: ComponentContent<T>, options: MenuOptions,
    partialUpdate?: boolean): Promise<void>
```

Update menu with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-updateMenu<T extends Object>(content: ComponentContent<T>, options: MenuOptions,    partialUpdate?: boolean): Promise<void>--><!--Device-PromptAction-updateMenu<T extends Object>(content: ComponentContent<T>, options: MenuOptions,    partialUpdate?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content of menu. |
| options | MenuOptions | Yes | Options. |
| partialUpdate | boolean | No | If true, only the specified properties in the MenuOptions are updated, otherwise the rest of the properties are overwritten with the default values. Default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103303](../../apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) | The ComponentContent cannot be found. |

## updatePopup

```TypeScript
updatePopup<T extends Object>(content: ComponentContent<T>, options: PopupCommonOptions,
    partialUpdate?: boolean): Promise<void>
```

Update popup with frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptAction-updatePopup<T extends Object>(content: ComponentContent<T>, options: PopupCommonOptions,    partialUpdate?: boolean): Promise<void>--><!--Device-PromptAction-updatePopup<T extends Object>(content: ComponentContent<T>, options: PopupCommonOptions,    partialUpdate?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content of popup. |
| options | PopupCommonOptions | Yes | Options. |
| partialUpdate | boolean | No | If true, only the specified properties in the options are updated, otherwise the rest of the properties are overwritten with the default values. Default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103301](../../apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) | The ComponentContent is incorrect. |
| [103303](../../apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) | The ComponentContent cannot be found. |

