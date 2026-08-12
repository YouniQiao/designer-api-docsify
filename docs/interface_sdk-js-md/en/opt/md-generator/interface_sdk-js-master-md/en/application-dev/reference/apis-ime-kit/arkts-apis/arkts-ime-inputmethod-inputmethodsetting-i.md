# InputMethodSetting

In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md#getSetting) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.

**Since:** 8

<!--Device-inputMethod-interface InputMethodSetting--><!--Device-inputMethod-interface InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(callback: AsyncCallback<void>): void
```

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodList/InputMethodListDialog](ohos.inputMethodList/InputMethodListDialog)

<!--Device-InputMethodSetting-displayOptionalInputMethod(callback: AsyncCallback<void>): void--><!--Device-InputMethodSetting-displayOptionalInputMethod(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodList/InputMethodListDialog](ohos.inputMethodList/InputMethodListDialog)

<!--Device-InputMethodSetting-displayOptionalInputMethod(): Promise<void>--><!--Device-InputMethodSetting-displayOptionalInputMethod(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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

List all input methods

**Since:** 11

<!--Device-InputMethodSetting-getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void--><!--Device-InputMethodSetting-getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List all input methods

**Since:** 11

<!--Device-InputMethodSetting-getAllInputMethods(): Promise<Array<InputMethodProperty>>--><!--Device-InputMethodSetting-getAllInputMethods(): Promise<Array<InputMethodProperty>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List all input methods sync

**Since:** 11

<!--Device-InputMethodSetting-getAllInputMethodsSync(): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getAllInputMethodsSync(): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## Examples

```TypeScript
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getAllInputMethodsSync();
```

## getInputMethodState

```TypeScript
getInputMethodState(): Promise<EnabledState>
```

The input method application calls this interface to obtain its own enabled state.

**Since:** 15

<!--Device-InputMethodSetting-getInputMethodState(): Promise<EnabledState>--><!--Device-InputMethodSetting-getInputMethodState(): Promise<EnabledState>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EnabledState](arkts-ime-inputmethod-enabledstate-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800004-not-an-input-method) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List input methods

**Since:** 9

<!--Device-InputMethodSetting-getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void--><!--Device-InputMethodSetting-getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List input methods

**Since:** 9

<!--Device-InputMethodSetting-getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>--><!--Device-InputMethodSetting-getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List enabled or disabled input methods sync

**Since:** 11

<!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean): Array<InputMethodProperty>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## Examples

```TypeScript
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getInputMethodsSync(true);
```

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void
```

List subtype of current input method

**Since:** 9

<!--Device-InputMethodSetting-listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void--><!--Device-InputMethodSetting-listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List subtype of current input method

**Since:** 9

<!--Device-InputMethodSetting-listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>--><!--Device-InputMethodSetting-listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInputMethods](#getInputMethods)

<!--Device-InputMethodSetting-listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void--><!--Device-InputMethodSetting-listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | Yes |

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInputMethods](#getInputMethods)

<!--Device-InputMethodSetting-listInputMethod(): Promise<Array<InputMethodProperty>>--><!--Device-InputMethodSetting-listInputMethod(): Promise<Array<InputMethodProperty>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

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

List subtype of the specified input method.

**Since:** 9

<!--Device-InputMethodSetting-listInputMethodSubtype(      inputMethodProperty: InputMethodProperty,      callback: AsyncCallback<Array<InputMethodSubtype>>    ): void--><!--Device-InputMethodSetting-listInputMethodSubtype(      inputMethodProperty: InputMethodProperty,      callback: AsyncCallback<Array<InputMethodSubtype>>    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

List subtype of the specified input method.

**Since:** 9

<!--Device-InputMethodSetting-listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>--><!--Device-InputMethodSetting-listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

Unsubscribe input method or subtype change.

**Since:** 9

<!--Device-InputMethodSetting-off(      type: 'imeChange',      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void--><!--Device-InputMethodSetting-off(      type: 'imeChange',      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeChange' | Yes |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) = & gt; void | No |

## Examples

```TypeScript
inputMethod.getSetting().off('imeChange');
```

## on('imeChange')

```TypeScript
on(
      type: 'imeChange',
      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

Subscribe input method or subtype change.

**Since:** 9

<!--Device-InputMethodSetting-on(      type: 'imeChange',      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void--><!--Device-InputMethodSetting-on(      type: 'imeChange',      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeChange' | Yes |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) = & gt; void | Yes |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethod.getSetting()
  .on('imeChange', (inputMethodProperty: inputMethod.InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => {
    console.info(`Succeeded in subscribing imeChange: inputMethodProperty.name: ${inputMethodProperty.name} ` +
      `, inputMethodSubtype.id: ${inputMethodSubtype.id}`);
  });
```

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(callback: AsyncCallback<boolean>): void
```

Show input method setting extension dialog

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [inputMethodList/InputMethodListDialog](ohos.inputMethodList/InputMethodListDialog)

<!--Device-InputMethodSetting-showOptionalInputMethods(callback: AsyncCallback<boolean>): void--><!--Device-InputMethodSetting-showOptionalInputMethods(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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

Show input method setting extension dialog

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [inputMethodList/InputMethodListDialog](ohos.inputMethodList/InputMethodListDialog)

<!--Device-InputMethodSetting-showOptionalInputMethods(): Promise<boolean>--><!--Device-InputMethodSetting-showOptionalInputMethods(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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
