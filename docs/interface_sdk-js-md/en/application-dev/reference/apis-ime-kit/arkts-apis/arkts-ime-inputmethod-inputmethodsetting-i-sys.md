# InputMethodSetting

InputMethodSetting提供输入法配置与查询能力，面向前台应用提供以下功能：

- **输入法变化订阅**：通过  
[on('imeChange')](inputMethod.InputMethodSetting.on( type: 'imeChange', callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void ))订阅输入法及子类型变化事件，当用户切换输入法时收到通知。  
- **输入法列表查询**：通过  
[getInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getinputmethods)查询已激活/未激活输入法列表，通过  
[getAllInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getallinputmethods)查询所有已安装输入法列表，通过  
[listInputMethodSubtype](arkts-ime-inputmethod-inputmethodsetting-i.md#listinputmethodsubtype)查询指定输入法的子类型列表。  
- **面板可见性查询**：通过isPanelShown查询输入法面板是否显示。  
- **输入法选择对话框**：通过showOptionalInputMethods显示输入法选择对话框（已废弃，建议使用InputMethodListDialog）。

需通过[getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting)获取InputMethodSetting实例后使用。

下列API均需使用[getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting)获取到InputMethodSetting实例后，通过实例调用。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputMethod-interface InputMethodSetting--><!--Device-inputMethod-interface InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## enableInputMethod

```TypeScript
enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>
```

修改输入法的启用状态。使用promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodSetting-enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>--><!--Device-InputMethodSetting-enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 输入法包名。 |
| extensionName | string | Yes | 输入法扩展名。 |
| enabledState | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Yes | 输入法启用状态。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800019 | current operation cannot be applied to the preconfigured default input method. |
| 12800018 | input method is not found. |
| 201 | permissions check fails. |
| 202 | not system application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

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

修改指定用户输入法的启用状态。

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
| bundleName | string | Yes | 输入法的包名。 |
| extensionName | string | Yes | 输入法的扩展名。 |
| enabledState | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Yes | 要修改的启用状态。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 用户ID。如果不提供：如果调用者不是用户0的应用，该值默认为调用者的用户ID。如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800019 | current operation cannot be applied to the preconfigured default input method. |
| 12800018 | input method is not found. |
| 12800023 | the specified user does not exist. |
| 201 | permissions check fails. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
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

获取指定用户的所有输入法应用列表。同步接口。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 用户ID。如果不提供：如果调用者不是用户0的应用，该值默认为调用者的用户ID。如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;InputMethodProperty&gt; | 返回所有输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800023 | the specified user does not exist. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
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

获取指定用户的光标信息。当编辑框未给输入法服务通知光标信息时，返回所有属性值都为0。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getCursorInfo(userId?: int): CursorInfo--><!--Device-InputMethodSetting-getCursorInfo(userId?: int): CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的用户ID。 <如果调用者不是用户0应用，该值默认为调用者的用户ID。 如果调用者是用户0应用，则该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | 指定用户下的光标信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1. No edit box is bound to the current input method application under the specified user. |
| 12800023 | the specified user does not exist. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible causes: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let cursorInfo: inputMethod.CursorInfo = inputMethod.getSetting().getCursorInfo();
  console.info(`get cursorInfo success, left: ${cursorInfo.left}, top: ${cursorInfo.top}, width: ${cursorInfo.width}, height: ${cursorInfo.height}, displayId: ${cursorInfo.displayId}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get cursorInfo. Code: ${error.code}, message: ${error.message}`);
}
```

## getDefaultInputMethodAbility

```TypeScript
getDefaultInputMethodAbility(): InputMethodProperty
```

获取默认输入法能力。为优化性能，返回的InputMethodProperty对象仅保证能够唯一标识输入法能力的`name`和`id`属性正确，其他属性可能为空。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty--><!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 默认输入法属性，仅保证`name`和`id`属性正确，其他属性可能为空。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
try {
  const defaultAbility: inputMethod.InputMethodProperty = inputMethod.getSetting().getDefaultInputMethodAbility();
  console.info('Succeeded in getting default input method ability, name: ' + defaultAbility.name + ', id: ' + defaultAbility.id);
} catch (err) {
  console.error(`Failed to getDefaultInputMethodAbility. Code: ${err.code}, message: ${err.message}`);
}
```

## getInputMethodSubtypes

ArkTS-Dyn:
```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: number): Array<InputMethodSubtype>
```

ArkTS-Sta:
```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>
```

获取指定用户指定输入法的子类型列表。同步接口。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>--><!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 指定输入法的包名。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 用户ID。如果不提供：如果调用者不是用户0的应用，该值默认为调用者的用户ID。如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | 返回指定输入法应用的所有子类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800023 | the specified user does not exist. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
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

获取指定用户已激活/未激活的输入法应用列表。同步接口

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 用户ID。如果不提供：如果调用者不是用户0的应用，该值默认为调用者的用户ID。如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;InputMethodProperty&gt; | 返回已激活/未激活输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800023 | the specified user does not exist. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo): boolean
```

查询指定类型的输入法面板是否处于显示状态。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo): boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes | 输入法面板的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 面板显隐状态查询结果。&lt;br/&gt;- true表示被查询的输入法面板处于显示状态。&lt;br/&gt;- false表示被查询的输入法面板处于隐藏状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 202 | not system application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

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

查询指定类型的输入法面板在指定屏幕上是否处于显示状态。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | Yes | 输入法面板的属性。 |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 屏幕ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 面板显隐状态查询结果。&lt;br/&gt;- true表示被查询的输入法面板处于显示状态。&lt;br/&gt;- false表示被查询的输入法面板处于隐藏状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

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

取消订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘显示事件。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeShow' | Yes | 设置监听类型，固定取值'imeShow'。 |
| callback | (info: Array&lt;InputWindowInfo&gt;) =&gt; void | No | 取消订阅的回调函数。 &lt;br&gt;参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethod.getSetting().off('imeShow');
```

## off('imeHide')

```TypeScript
off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void
```

取消订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘隐藏事件。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeHide' | Yes | 设置监听类型，固定取值'imeHide'。 |
| callback | (info: Array&lt;InputWindowInfo&gt;) =&gt; void | No | 取消订阅的回调函数。 &lt;br&gt;参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethod.getSetting().off('imeHide');
```

## offImeChangeWithUserId

```TypeScript
offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void
```

取消订阅输入法及子类型变化监听事件，携带发生输入法变更的用户ID。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void--><!--Device-InputMethodSetting-offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | No | 回调函数，返回取消订阅的输入法属性对象、子类型对象及用户ID。 参数不填写时，取消订阅所有的回调事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

## offImeHide

```TypeScript
offImeHide(callback?: Callback<Array<InputWindowInfo>>): void
```

取消订阅输入法Panel固定态软键盘隐藏事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;InputWindowInfo&gt;&gt; | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offImeShow

```TypeScript
offImeShow(callback?: Callback<Array<InputWindowInfo>>):void
```

取消订阅输入法Panel固定态软键盘显示事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;InputWindowInfo&gt;&gt; | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## on('imeShow')

```TypeScript
on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void
```

订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘显示事件。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputMethodSetting-on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeShow' | Yes | 设置监听类型，固定取值为'imeShow'。 |
| callback | (info: Array&lt;InputWindowInfo&gt;) =&gt; void | Yes | 回调函数，返回输入法固定态软键盘信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

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

订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘隐藏事件。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputMethodSetting-on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeHide' | Yes | 设置监听类型，固定取值为'imeHide'。 |
| callback | (info: Array&lt;InputWindowInfo&gt;) =&gt; void | Yes | 回调函数，返回输入法固定态软键盘信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

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

订阅输入法及子类型变化监听事件，携带发生输入法变更的用户ID。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void--><!--Device-InputMethodSetting-onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | Yes | 回调函数，返回输入法属性对象、子类型对象及用户ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

## onImeHide

```TypeScript
onImeHide(callback: Callback<Array<InputWindowInfo>>): void
```

订阅输入法Panel固定态软键盘隐藏事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;InputWindowInfo&gt;&gt; | Yes | 回调函数，返回输入法固定态软键盘信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

## onImeShow

```TypeScript
onImeShow(callback: Callback<Array<InputWindowInfo>>):void
```

订阅输入法Panel固定态软键盘显示事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;InputWindowInfo&gt;&gt; | Yes | 回调函数，返回输入法固定态软键盘信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

