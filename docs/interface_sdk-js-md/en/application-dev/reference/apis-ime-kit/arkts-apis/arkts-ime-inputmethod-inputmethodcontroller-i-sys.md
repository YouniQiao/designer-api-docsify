# InputMethodController (System API)

```TypeScript
interface InputMethodController
```

In the following API examples, you need to use [getController]_[getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain the InputMethodController instance and then invoke the corresponding method through the instance. <br> <br>InputMethodController is an input method client controller that provides core capabilities for foreground applications to interact with input methods. After obtaining an instance through `inputMethod.getController()`, you can perform the following operations: <br> <br>- Binding management: Create a binding with the input method through [attach]_[attach](arkts-ime-inputmethod-inputmethodcontroller-i.md#attach-1). Run the [detach](arkts-ime-inputmethod-inputmethodcontroller-i.md#detach-1) command to unbind the user. The attach and detach functions must be used in pairs. <br>-Keyboard control: Press [showTextInput](arkts-ime-inputmethod-inputmethodcontroller-i.md#showtextinput-1) to start the soft keyboard and enter the editing state. Press [hideTextInput](arkts-ime-inputmethod-inputmethodcontroller-i.md#hidetextinput-1) to hide the soft keyboard and exit the editing state. showTextInput and hideTextInput must be used in pairs. <br>-Synchronize the editing box status: The [updateCursor](arkts-ime-inputmethod-inputmethodcontroller-i.md#updatecursor-1), [changeSelection](arkts-ime-inputmethod-inputmethodcontroller-i.md#changeselection) _, and [updateAttribute](arkts-ime-inputmethod-inputmethodcontroller-i.md#updateattribute-1) interfaces are used to synchronize the editing box status information such as the cursor, selection area, and attribute to the input method. <br>-Event subscription: The on('insertText') and on('deleteLeft') interfaces are used to subscribe to the text operation events sent by the input method application. <br> <br> Typical invoking sequence: `getController()` → `attach()` → `showTextInput()`/`hideTextInput()` → `detach()` <br> <br>  
> ** Note: ** <br>
> <br>
> attach and detach must be used together, and showTextInput and hideTextInput must be used together. Otherwise, resource leakage or status inconsistency may occur. In ArkTS dynamic calls, BusinessError 401 is thrown when an invalid event type or callback function is passed in on/off. When registering a listener, callback must be a function. When listening is canceled, if callback is not transferred or null or undefined is transferred, all callbacks of the event are removed. If other values are transferred, the event must be a function.

**Since:** 6

<!--Device-inputMethod-interface InputMethodController--><!--Device-inputMethod-interface InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(displayId: number): Promise<void>
```

Hides the soft keyboard on a specified screen. This API uses a promise to return the result. <br> <br>  
> **NOTE:** <br>
> <br>
> This API can be called only when the edit box is attached to the input method. That is, it can be called to <br>
> hide the soft keyboard only when the edit box is focused.

**Since:** 23

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodController-hideSoftKeyboard(displayId: long): Promise<void>--><!--Device-InputMethodController-hideSoftKeyboard(displayId: long): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | number | Yes | Screen ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

<!--Del-->
**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayId: number = 30;
inputMethod.getController().hideSoftKeyboard(displayId).then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

<!--DelEnd-->

## showSoftKeyboard

```TypeScript
showSoftKeyboard(displayId: number): Promise<void>
```

Shows the soft keyboard on a specified screen. This API uses a promise to return the result. <br> <br>Paired calls: <br> <br>- This method is used together with **hideSoftKeyboard** to control the showing and hiding of the soft keyboard. <br>- Generally, after calling **showSoftKeyboard** to show the soft keyboard, you can call **hideSoftKeyboard** to hide the soft keyboard when needed. <br>- This API can be called only when the edit box is attached to the input method. <br> <br>  
> **NOTE:** <br>
> <br>
> This API can be called only when the edit box is attached to the input method. That is, it can be called to <br>
> show the soft keyboard only when the edit box is focused.

**Since:** 23

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodController-showSoftKeyboard(displayId: long): Promise<void>--><!--Device-InputMethodController-showSoftKeyboard(displayId: long): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | number | Yes | Screen ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

<!--Del-->
**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayId: number = 20;
inputMethod.getController().showSoftKeyboard(displayId).then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

<!--DelEnd-->
