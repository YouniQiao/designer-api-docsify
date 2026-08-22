# InputMethodSetting

@brief In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.

**Since:** 23

<!--Device-inputMethod-interface InputMethodSetting--><!--Device-inputMethod-interface InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## enableInputMethod

```TypeScript
enableInputMethod(
      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: int): Promise<void>
```

@brief Change the enabled state of an input method of a specified user.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-enableInputMethod(      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: int): Promise<void>--><!--Device-InputMethodSetting-enableInputMethod(      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Indicates the bundle name of the input method. |
| extensionName | string | Yes | Indicates the extension name of the input method. |
| enabledState | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Yes | Indicates the enabledState to be changed. |
| userId | int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| [12800018](../errorcode-inputmethod-framework.md#12800018-input-method-not-found) | input method is not found. |
| [12800019](../errorcode-inputmethod-framework.md#12800019-unsupported-operation-by-default-input-method) | current operation cannot be applied to the preconfigured default input method. |
| 12800023 | the specified user does not exist. |
| 12800024 | the specified user is not in the foreground. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableInputMethodSafely() {
  const currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
  if (!currentIme) {
    console.error("Failed to get current input method");
    return;
  }

  inputMethod.getSetting()
    .enableInputMethod(currentIme.name, currentIme.id, inputMethod.EnabledState.BASIC_MODE)
    .then(() => {
      console.info('Succeeded in enable inputmethod.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to enableInputMethod. Code: ${err.code}, message: ${err.message}`);
    });
}

enableInputMethodSafely();
```

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>
```

@brief Get all input methods sync of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; | the list of all input methods. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) | bundle manager error. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800023 | the specified user does not exist. |
| 12800024 | the specified user is not in the foreground. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |

**Examples**

```TypeScript
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getAllInputMethodsSync();
```

## getDefaultInputMethodAbility

```TypeScript
getDefaultInputMethodAbility(): InputMethodProperty
```

@brief Obtains the default input method capabilities. To optimize performance, the returned **InputMethodProperty** object ensures that only the `name` and `id` attributes that uniquely identify the input method capability are correct. Other attributes may be empty. <br> <br>**Example** <br> <br>```ts <br>try { <br> const defaultAbility: inputMethod.InputMethodProperty = inputMethod.getSetting().getDefaultInputMethodAbility(); <br> console.info('Succeeded in getting default input method ability, name: ' + defaultAbility.name + ', id: ' + defaultAbility.id); <br>} catch (err) { <br> console.error(`Failed to getDefaultInputMethodAbility. Code: \${err.code}, message: \${err.message}`); <br>} <br>```

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty--><!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Default input method attributes. Only the `name` and `id` attributes are guaranteed to be correct. Other attributes may be empty. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>
```

@brief List enabled or disabled input methods sync of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | If true, collect enabled input methods. If false, collect disabled input methods. |
| userId | int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; | the list of input methods. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) | bundle manager error. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800023 | the specified user does not exist. |
| 12800024 | the specified user is not in the foreground. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |

**Examples**

```TypeScript
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getInputMethodsSync(true);
```

## getInputMethodSubtypes

```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>
```

@brief Get subtypes of a specified input method of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>--><!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | the bundle name of the specified input method. |
| userId | int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | the subtype of target input method. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) | bundle manager error. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800023 | the specified user does not exist. |
| 12800024 | the specified user is not in the foreground. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo): boolean
```

@brief Checks whether the input method panel of a specified type is shown.

**Since:** 23

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo): boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes | Information about the input method panel. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the input method panel is shown. <br>- The value **true** means that the input method panel is shown. <br>- The value **false** means that the input method panel is hidden. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Examples**

```TypeScript
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';

let info: PanelInfo = {
  type: PanelType.SOFT_KEYBOARD,
  flag: PanelFlag.FLAG_FIXED
}

let result: boolean = inputMethod.getSetting().isPanelShown(info);
console.info('Succeeded in querying isPanelShown, result: ' + result);
```

```TypeScript
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';

let displayId: number = 10;
let info: PanelInfo = {
  type: PanelType.SOFT_KEYBOARD,
  flag: PanelFlag.FLAG_FIXED
}

let result: boolean = inputMethod.getSetting().isPanelShown(info, displayId);
console.info('Succeeded in querying isPanelShown, result: ' + result);
```

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo, displayId: long): boolean
```

@brief Checks whether the input method panel of a specified type is shown on a specified screen.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes | Information about the input method panel. |
| displayId | long | Yes | Display ID. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the input method panel is shown. <br>- The value **true** means that the input method panel is shown. <br>- The value **false** means that the input method panel is hidden. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Examples**

See [isPanelShown](#ispanelshown)

## off('imeHide')

```TypeScript
off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void
```

@brief Unsubscribes from the soft keyboard hide event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state.

**Since:** 10

<!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeHide' | Yes | Event type, which is **'imeHide'**. |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | No | Callback to unregister. <br>If this parameter is not specified, this API unregisters all callbacks for the specified event type. |

**Examples**

```TypeScript
inputMethod.getSetting().off('imeHide');
```

## off('imeShow')

```TypeScript
off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void
```

@brief Unsubscribes from the soft keyboard show event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state.

**Since:** 10

<!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeShow' | Yes | Event type, which is **'imeShow'**. |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | No | Callback to unregister. <br>If this parameter is not specified, this API unregisters all callbacks for the specified event type. |

**Examples**

```TypeScript
inputMethod.getSetting().off('imeShow');
```

## offImeChangeWithUserId

```TypeScript
offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void
```

@brief Unsubscribe from the input method change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void--><!--Device-InputMethodSetting-offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | No | the callback called when the current input method changes, when the subscriber unsubscribes all callbacks, this parameter can be left blank. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## offImeHide

```TypeScript
offImeHide(callback?: Callback<Array<InputWindowInfo>>): void
```

@brief Unsubscribe input window hide event.

**Since:** 23

<!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | No | the callback called when input method hides, when subscriber unsubscribes all callback functions, this parameter can be left blank. |

## offImeShow

```TypeScript
offImeShow(callback?: Callback<Array<InputWindowInfo>>):void
```

@brief Unsubscribe input window show event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | No | the callback called when input method shows, when subscriber unsubscribes all callback functions, this parameter can be left blank. |

## on('imeHide')

```TypeScript
on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void
```

@brief Subscribes to the soft keyboard hide event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-InputMethodSetting-on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeHide' | Yes | Event type, which is **'imeHide'**. |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | Yes | Callback used to return the soft keyboard information of the input method panel in the fixed state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

**Examples**

```TypeScript
inputMethod.getSetting().on('imeHide', (info: Array<inputMethod.InputWindowInfo>) => {
  console.info('Succeeded in subscribing imeHide event.');
});
```

## on('imeShow')

```TypeScript
on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void
```

@brief Subscribes to the soft keyboard show event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-InputMethodSetting-on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeShow' | Yes | Event type, which is **'imeShow'**. |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | Yes | Callback used to return the soft keyboard information of the input method panel in the fixed state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

**Examples**

```TypeScript
inputMethod.getSetting().on('imeShow', (info: Array<inputMethod.InputWindowInfo>) => {
  console.info('Succeeded in subscribing imeShow event.');
});
```

## onImeChangeWithUserId

```TypeScript
onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void
```

@brief Subscribe to the input method change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void--><!--Device-InputMethodSetting-onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | Yes | the callback called when the current input method changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## onImeHide

```TypeScript
onImeHide(callback: Callback<Array<InputWindowInfo>>): void
```

@brief Subscribes to input window hidden events.

**Since:** 23

<!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | Yes | the callback called when input method hides. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## onImeShow

```TypeScript
onImeShow(callback: Callback<Array<InputWindowInfo>>):void
```

@brief Subscribes to input window show events.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | Yes | the callback called when input method shows. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

