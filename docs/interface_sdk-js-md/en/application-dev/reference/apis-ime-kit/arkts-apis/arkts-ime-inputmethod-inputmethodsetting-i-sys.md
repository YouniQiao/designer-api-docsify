# InputMethodSetting

In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.

**Since:** 8

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## enableInputMethod

```TypeScript
enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>
```

Enables or disables an input method. This API uses a promise to return the result.   
**Example**   
```ts 
import { BusinessError } from '@kit.BasicServicesKit'; 
 
function enableInputMethodSafely() {
 const currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod(); 
 if (!currentIme) {
 console.error("Failed to get current input method"); 
 return; 
 } 
 
 inputMethod.getSetting() 
 .enableInputMethod(currentIme.name, currentIme.id, inputMethod.EnabledState.BASIC_MODE) 
 .then(() =&gt; {
 console.info('Succeeded in enable inputmethod.'); 
 }) 
 .catch((err: BusinessError) =&gt; {
 console.error(`Failed to enableInputMethod. Code: \${err.code}, message: \${err.message}`); 
 }); 
} 
 
enableInputMethodSafely(); 
```

**Since:** 20

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| extensionName | string | Yes |
| [enabledState](arkts-ime-inputmethod-inputmethodproperty-i.md) | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800018](../errorcode-inputmethod-framework.md#12800018-input-method-not-found) |
| [12800019](../errorcode-inputmethod-framework.md#12800019-unsupported-operation-by-default-input-method) |

## enableInputMethod

```TypeScript
enableInputMethod(
      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: number): Promise<void>
```

Change the enabled state of an input method of a specified user.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| extensionName | string | Yes |
| [enabledState](arkts-ime-inputmethod-inputmethodproperty-i.md) | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800018](../errorcode-inputmethod-framework.md#12800018-input-method-not-found) |
| [12800019](../errorcode-inputmethod-framework.md#12800019-unsupported-operation-by-default-input-method) |
| 12800023 |
| 12800024 |
| 12800025 |

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(userId?: number): Array<InputMethodProperty>
```

Get all input methods sync of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800023 |
| 12800024 |
| 12800025 |

## getCursorInfo

```TypeScript
getCursorInfo(userId?: number): CursorInfo
```

Obtains the cursor information of a specified user. If the edit box does not notify the input method service of the cursor information, all attribute values returned are **0**.   
**Example**   
```ts 
import { BusinessError } from '@kit.BasicServicesKit'; 
 
try {
 let cursorInfo: inputMethod.CursorInfo = inputMethod.getSetting().getCursorInfo(); 
 console.info(`get cursorInfo success, left: \${cursorInfo.left}, top: \${cursorInfo.top}, width: \${cursorInfo.width}, height: \${cursorInfo.height}, displayId: \${cursorInfo.displayId}`); 
} catch (err) {
 let error = err as BusinessError; 
 console.error(`Failed to get cursorInfo. Code: \${error.code}, message: \${error.message}`); 
} 
```

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800023 |
| 12800024 |
| 12800025 |

## getDefaultInputMethodAbility

```TypeScript
getDefaultInputMethodAbility(): InputMethodProperty
```

Obtains the default input method capabilities. To optimize performance, the returned **InputMethodProperty** object ensures that only the `name` and `id` attributes that uniquely identify the input method capability are correct. Other attributes may be empty.   
**Example**   
```ts 
try {
 const defaultAbility: inputMethod.InputMethodProperty = inputMethod.getSetting().getDefaultInputMethodAbility(); 
 console.info('Succeeded in getting default input method ability, name: ' + defaultAbility.name + ', id: ' + defaultAbility.id); 
} catch (err) {
 console.error(`Failed to getDefaultInputMethodAbility. Code: \${err.code}, message: \${err.message}`); 
} 
```

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean, userId?: number): Array<InputMethodProperty>
```

List enabled or disabled input methods sync of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800023 |
| 12800024 |
| 12800025 |

## getInputMethodSubtypes

```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: number): Array<InputMethodSubtype>
```

Get subtypes of a specified input method of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800023 |
| 12800024 |
| 12800025 |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo): boolean
```

Checks whether the input method panel of a specified type is shown.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo, displayId: number): boolean
```

Checks whether the input method panel of a specified type is shown on a specified screen.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## off('imeShow')

```TypeScript
off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void
```

Unsubscribes from the soft keyboard show event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeShow' | Yes |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | No |

## off('imeHide')

```TypeScript
off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void
```

Unsubscribes from the soft keyboard hide event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeHide' | Yes |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | No |

## offImeChangeWithUserId

```TypeScript
offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void
```

Unsubscribe from the input method change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('imeShow')

```TypeScript
on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void
```

Subscribes to the soft keyboard show event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeShow' | Yes |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('imeHide')

```TypeScript
on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void
```

Subscribes to the soft keyboard hide event of the [input method panel](arkts-ime-inputmethodengine-panel-i.md) in the fixed state. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeHide' | Yes |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onImeChangeWithUserId

```TypeScript
onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void
```

Subscribe to the input method change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
