# InputMethodSetting

In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md#getSetting) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputMethod-interface InputMethodSetting--><!--Device-inputMethod-interface InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## enableInputMethod

```TypeScript
enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>
```

Enables or disables an input method. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodSetting-enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>--><!--Device-InputMethodSetting-enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of the input method. |
| extensionName | string | Yes | Extension name of the input method. |
| enabledState | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Yes | Whether the input method is enabled. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800019](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800019-unsupported-operation-by-default-input-method) | current operation cannot be applied to the preconfigured default input method. |
| [12800018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800018-input-method-not-found) | input method is not found. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

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

## enableInputMethod

ArkTS-Dyn:
```TypeScript
enableInputMethod(
      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
enableInputMethod(
      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: int): Promise<void>
```

Change the enabled state of an input method of a specified user.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800019](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800019-unsupported-operation-by-default-input-method) | current operation cannot be applied to the preconfigured default input method. |
| [12800018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800018-input-method-not-found) | input method is not found. |
| 12800023 | the specified user does not exist. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## getAllInputMethodsSync

ArkTS-Dyn:
```TypeScript
getAllInputMethodsSync(userId?: number): Array<InputMethodProperty>
```

ArkTS-Sta:
```TypeScript
getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>
```

Get all input methods sync of a specified user.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; | the list of all input methods. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) | bundle manager error. |
| 12800023 | the specified user does not exist. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## getCursorInfo

ArkTS-Dyn:
```TypeScript
getCursorInfo(userId?: number): CursorInfo
```

ArkTS-Sta:
```TypeScript
getCursorInfo(userId?: int): CursorInfo
```

Get the cursor information of a specified user.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getCursorInfo(userId?: int): CursorInfo--><!--Device-InputMethodSetting-getCursorInfo(userId?: int): CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | the information of the cursor of the specified display. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1. No edit box is bound to the current input method application under the specified user. |
| 12800023 | the specified user does not exist. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible causes: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## getDefaultInputMethodAbility

```TypeScript
getDefaultInputMethodAbility(): InputMethodProperty
```

&lt;p&gt;Get the default input method ability.&lt;/p&gt;&lt;p&gt;To optimize performance, only the 'name' and 'id' properties which can uniquely identify an input method ability are included in the returned InputMethodProperty object.&lt;/p&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty--><!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | property of the default input method.Only contains 'name' and 'id' properties. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## getInputMethodSubtypes

ArkTS-Dyn:
```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: number): Array<InputMethodSubtype>
```

ArkTS-Sta:
```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>
```

Get subtypes of a specified input method of a specified user.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>--><!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | the bundle name of the specified input method. |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | the subtype of target input method. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) | bundle manager error. |
| 12800023 | the specified user does not exist. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## getInputMethodsSync

ArkTS-Dyn:
```TypeScript
getInputMethodsSync(enable: boolean, userId?: number): Array<InputMethodProperty>
```

ArkTS-Sta:
```TypeScript
getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>
```

List enabled or disabled input methods sync of a specified user.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | If true, collect enabled input methods. If false, collect disabled input methods. |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the user ID. If not provided: If the caller is not a user 0 application, the value defaults to the caller's user ID. If the caller is a user 0 application, the value defaults to the foreground user ID of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; | the list of input methods. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) | bundle manager error. |
| 12800023 | the specified user does not exist. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo): boolean
```

Checks whether the input method panel of a specified type is shown.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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
| boolean | Whether the input method panel is shown. &lt;br&gt;- The value **true** means that the input method panel is shown. &lt;br&gt;- The value **false** means that the input method panel is hidden. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';

let info: PanelInfo = {
  type: PanelType.SOFT_KEYBOARD,
  flag: PanelFlag.FLAG_FIXED
}

let result: boolean = inputMethod.getSetting().isPanelShown(info);
console.info('Succeeded in querying isPanelShown, result: ' + result);
```

## isPanelShown

ArkTS-Dyn:
```TypeScript
isPanelShown(panelInfo: PanelInfo, displayId: number): boolean
```

ArkTS-Sta:
```TypeScript
isPanelShown(panelInfo: PanelInfo, displayId: long): boolean
```

Checks whether the input method panel of a specified type is shown on a specified screen.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes | Information about the input method panel. |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Display ID. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the input method panel is shown. &lt;br&gt;- The value **true** means that the input method panel is shown. &lt;br&gt;- The value **false** means that the input method panel is hidden. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

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

## off('imeShow')

```TypeScript
off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void
```

Unsubscribes from the soft keyboard show event of the   
[input method panel](arkts-ime-inputmethodengine-panel-i.md#Panel) in the fixed state.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeShow' | Yes | Event type, which is **'imeShow'**. |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | No | Callback to unregister.&lt;br&gt;If this parameter is not specified, this API unregisters all callbacks for the specified event type. |

## Examples

```TypeScript
inputMethod.getSetting().off('imeShow');
```

## off('imeHide')

```TypeScript
off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void
```

Unsubscribes from the soft keyboard hide event of the   
[input method panel](arkts-ime-inputmethodengine-panel-i.md#Panel) in the fixed state.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeHide' | Yes | Event type, which is **'imeHide'**. |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | No | Callback to unregister.&lt;br&gt;If this parameter is not specified, this API unregisters all callbacks for the specified event type. |

## Examples

```TypeScript
inputMethod.getSetting().off('imeHide');
```

## offImeChangeWithUserId

```TypeScript
offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void
```

Unsubscribe from the input method change event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## offImeHide

```TypeScript
offImeHide(callback?: Callback<Array<InputWindowInfo>>): void
```

Unsubscribe input window hide event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | No | the callback called when input method hides, when subscriber unsubscribes all callback functions, this parameter can be left blank. |

## offImeShow

```TypeScript
offImeShow(callback?: Callback<Array<InputWindowInfo>>):void
```

Unsubscribe input window show event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | No | the callback called when input method shows, when subscriber unsubscribes all callback functions, this parameter can be left blank. |

## on('imeShow')

```TypeScript
on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void
```

Subscribes to the soft keyboard show event of the   
[input method panel](arkts-ime-inputmethodengine-panel-i.md#Panel) in the fixed state. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

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
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## Examples

```TypeScript
inputMethod.getSetting().on('imeShow', (info: Array<inputMethod.InputWindowInfo>) => {
  console.info('Succeeded in subscribing imeShow event.');
});
```

## on('imeHide')

```TypeScript
on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void
```

Subscribes to the soft keyboard hide event of the   
[input method panel](arkts-ime-inputmethodengine-panel-i.md#Panel) in the fixed state. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

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
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## Examples

```TypeScript
inputMethod.getSetting().on('imeHide', (info: Array<inputMethod.InputWindowInfo>) => {
  console.info('Succeeded in subscribing imeHide event.');
});
```

## onImeChangeWithUserId

```TypeScript
onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void
```

Subscribe to the input method change event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## onImeHide

```TypeScript
onImeHide(callback: Callback<Array<InputWindowInfo>>): void
```

Subscribes to input window hidden events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | Yes | the callback called when input method hides. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

## onImeShow

```TypeScript
onImeShow(callback: Callback<Array<InputWindowInfo>>):void
```

Subscribes to input window show events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | Yes | the callback called when input method shows. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

