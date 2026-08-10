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

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(callback: AsyncCallback<void>): void
```

显示输入法选择对话框。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.inputMethodList/InputMethodListDialog

<!--Device-InputMethodSetting-displayOptionalInputMethod(callback: AsyncCallback<void>): void--><!--Device-InputMethodSetting-displayOptionalInputMethod(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当输入法选择对话框显示成功。err为undefined，否则为错误对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().displayOptionalInputMethod((err: BusinessError) => {
  if (err) {
    console.error(`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in displaying optionalInputMethod.');
});
```

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(): Promise<void>
```

显示输入法选择对话框。使用promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.inputMethodList/InputMethodListDialog

<!--Device-InputMethodSetting-displayOptionalInputMethod(): Promise<void>--><!--Device-InputMethodSetting-displayOptionalInputMethod(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().displayOptionalInputMethod().then(() => {
  console.info('Succeeded in displaying optionalInputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}`);
})
```

## getAllInputMethods

```TypeScript
getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void
```

获取所有输入法应用列表。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void--><!--Device-InputMethodSetting-getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;InputMethodProperty&gt;&gt; | Yes | 回调函数，返回所有输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getAllInputMethods((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting all inputMethods.');
});
```

## getAllInputMethods

```TypeScript
getAllInputMethods(): Promise<Array<InputMethodProperty>>
```

获取所有输入法应用列表。使用promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getAllInputMethods(): Promise<Array<InputMethodProperty>>--><!--Device-InputMethodSetting-getAllInputMethods(): Promise<Array<InputMethodProperty>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;InputMethodProperty&gt;&gt; | Promise对象，返回所有输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getAllInputMethods().then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in getting all inputMethods.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}`);
})
```

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(): Array<InputMethodProperty>
```

获取所有输入法应用列表。同步接口。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getAllInputMethodsSync(): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getAllInputMethodsSync(): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;InputMethodProperty&gt; | 返回所有输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getAllInputMethodsSync();
```

## getInputMethodState

```TypeScript
getInputMethodState(): Promise<EnabledState>
```

查询输入法的启用状态。使用promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getInputMethodState(): Promise<EnabledState>--><!--Device-InputMethodSetting-getInputMethodState(): Promise<EnabledState>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;EnabledState&gt; | Promise对象，返回EnabledState.DISABLED表示未启用; 返回EnabledState.BASIC_MODE表示基础模式; 返回 EnabledState.FULL_EXPERIENCE_MODE表示完整体验模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800004 | not an input method application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethodState().then((status: inputMethod.EnabledState) => {
  console.info(`Succeeded in getInputMethodState, status: ${status}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getInputMethodState, code: ${err.code}, message: ${err.message}`);
})
```

## getInputMethods

```TypeScript
getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void
```

获取已激活/未激活的输入法应用列表。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void--><!--Device-InputMethodSetting-getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;InputMethodProperty&gt;&gt; | Yes | 回调函数，返回已激活/未激活输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethods(true, (err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(`Failed to getInputMethods, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting inputMethods.');
});
```

## getInputMethods

```TypeScript
getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>
```

获取已激活/未激活的输入法应用列表。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>--><!--Device-InputMethodSetting-getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;InputMethodProperty&gt;&gt; | Promise对象，返回已激活/未激活输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethods(true).then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in getting inputMethods.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getInputMethods, code: ${err.code}, message: ${err.message}`);
})
```

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean): Array<InputMethodProperty>
```

获取已激活/未激活的输入法应用列表。同步接口。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;InputMethodProperty&gt; | 返回已激活/未激活输入法列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getInputMethodsSync(true);
```

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void
```

查询当前输入法应用的所有子类型。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void--><!--Device-InputMethodSetting-listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Yes | 回调函数，返回当前输入法应用的所有子类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
inputMethodSetting.listCurrentInputMethodSubtype((err: BusinessError, data: Array<InputMethodSubtype>) => {
  if (err) {
    console.error(`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in listing currentInputMethodSubtype.');
});
```

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>
```

查询当前输入法应用的所有子类型。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>--><!--Device-InputMethodSetting-listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Promise对象，返回当前输入法应用的所有子类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listCurrentInputMethodSubtype().then((data: Array<InputMethodSubtype>) => {
  console.info('Succeeded in listing currentInputMethodSubtype.');
}).catch((err: BusinessError) => {
  console.error(`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
})
```

## listInputMethod

```TypeScript
listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void
```

查询已安装的输入法列表。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethod.InputMethodSetting#getInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getinputmethods)

<!--Device-InputMethodSetting-listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void--><!--Device-InputMethodSetting-listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;InputMethodProperty&gt;&gt; | Yes | 回调函数，返回已安装的输入法列表。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().listInputMethod((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(`Failed to listInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in listing inputMethod.');
});
```

## listInputMethod

```TypeScript
listInputMethod(): Promise<Array<InputMethodProperty>>
```

查询已安装的输入法列表。使用promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethod.InputMethodSetting#getInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getinputmethods)

<!--Device-InputMethodSetting-listInputMethod(): Promise<Array<InputMethodProperty>>--><!--Device-InputMethodSetting-listInputMethod(): Promise<Array<InputMethodProperty>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;InputMethodProperty&gt;&gt; | Promise对象，返回已安装输入法列表。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().listInputMethod().then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in listing inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to listInputMethod, code: ${err.code}, message: ${err.message}`);
})
```

## listInputMethodSubtype

```TypeScript
listInputMethodSubtype(
      inputMethodProperty: InputMethodProperty,
      callback: AsyncCallback<Array<InputMethodSubtype>>
    ): void
```

获取指定输入法应用的所有子类型。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-listInputMethodSubtype(      inputMethodProperty: InputMethodProperty,      callback: AsyncCallback<Array<InputMethodSubtype>>    ): void--><!--Device-InputMethodSetting-listInputMethodSubtype(      inputMethodProperty: InputMethodProperty,      callback: AsyncCallback<Array<InputMethodSubtype>>    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes | 输入法应用。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Yes | 回调函数，返回指定输入法应用的所有子类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodProperty: inputMethod.InputMethodProperty = {
  name: 'com.example.keyboard',
  id: 'propertyId',
  packageName: 'com.example.keyboard',
  methodId: 'propertyId',
}
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listInputMethodSubtype(inputMethodProperty,
  (err: BusinessError, data: Array<InputMethodSubtype>) => {
    if (err) {
      console.error(`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in listing inputMethodSubtype.');
  });
```

## listInputMethodSubtype

```TypeScript
listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>
```

获取指定输入法应用的所有子类型。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodSetting-listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>--><!--Device-InputMethodSetting-listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes | 输入法应用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Promise对象，返回指定输入法应用的所有子类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodProperty: inputMethod.InputMethodProperty = {
  name: 'com.example.keyboard',
  id: 'propertyId',
  packageName: 'com.example.keyboard',
  methodId: 'propertyId',
}
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listInputMethodSubtype(inputMethodProperty).then((data: Array<InputMethodSubtype>) => {
  console.info('Succeeded in listing inputMethodSubtype.');
}).catch((err: BusinessError) => {
  console.error(`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
})
```

## off('imeChange')

```TypeScript
off(
      type: 'imeChange',
      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

取消订阅输入法及子类型变化监听事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodSetting-off(      type: 'imeChange',      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void--><!--Device-InputMethodSetting-off(      type: 'imeChange',      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeChange' | Yes | 设置监听类型，固定取值为'imeChange'。 |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) =&gt; void | No | 回调函数，返回取消订阅的输入法属性对象及子类型对象。 |

## Examples

```TypeScript
inputMethod.getSetting().off('imeChange');
```

## offImeChange

```TypeScript
offImeChange(callback?: ImeChangeCallback): void
```

取消订阅输入法或子类型切换事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodSetting-offImeChange(callback?: ImeChangeCallback): void--><!--Device-InputMethodSetting-offImeChange(callback?: ImeChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ImeChangeCallback](arkts-ime-inputmethod-imechangecallback-t.md) | No | the callback called when the current input method changes, when subscriber unsubscribes all callback functions, this parameter can be left blank. |

## on('imeChange')

```TypeScript
on(
      type: 'imeChange',
      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

订阅输入法及子类型变化监听事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodSetting-on(      type: 'imeChange',      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void--><!--Device-InputMethodSetting-on(      type: 'imeChange',      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imeChange' | Yes | 设置监听类型，固定取值为'imeChange'。 |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) =&gt; void | Yes | 回调函数，返回输入法属性对象及子类型对象。 |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethod.getSetting()
  .on('imeChange', (inputMethodProperty: inputMethod.InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => {
    console.info(`Succeeded in subscribing imeChange: inputMethodProperty.name: ${inputMethodProperty.name} ` +
      `, inputMethodSubtype.id: ${inputMethodSubtype.id}`);
  });
```

## onImeChange

```TypeScript
onImeChange(callback: ImeChangeCallback): void
```

订阅输入法或子类型切换事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodSetting-onImeChange(callback: ImeChangeCallback): void--><!--Device-InputMethodSetting-onImeChange(callback: ImeChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ImeChangeCallback](arkts-ime-inputmethod-imechangecallback-t.md) | Yes | the callback called when the current input method changes. |

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(callback: AsyncCallback<boolean>): void
```

显示输入法选择对话框。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** ohos.inputMethodList/InputMethodListDialog

<!--Device-InputMethodSetting-showOptionalInputMethods(callback: AsyncCallback<boolean>): void--><!--Device-InputMethodSetting-showOptionalInputMethods(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当输入法选择对话框显示成功，err为undefined，data为true；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().showOptionalInputMethods((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in showing optionalInputMethods.');
  } else {
    console.error(`Failed to showOptionalInputMethods.`);
  }
});
```

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(): Promise<boolean>
```

显示输入法选择对话框。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** ohos.inputMethodList/InputMethodListDialog

<!--Device-InputMethodSetting-showOptionalInputMethods(): Promise<boolean>--><!--Device-InputMethodSetting-showOptionalInputMethods(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。当输入法选择对话框显示成功，err为undefined，data为true；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().showOptionalInputMethods().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in showing optionalInputMethods.');
  } else {
    console.error(`Failed to showOptionalInputMethods.`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}`);
})
```

