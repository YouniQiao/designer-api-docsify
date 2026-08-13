# switchInputMethod

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## switchInputMethod

```TypeScript
function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void
```

Switch input method. The caller must be the current inputmethod.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 9 - 10: ohos.permission.CONNECT_IME_ABILITY

<!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void--><!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-configuration-persistence-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
});
```


## switchInputMethod

```TypeScript
function switchInputMethod(target: InputMethodProperty): Promise<boolean>
```

Switch input method. The caller must be the current inputmethod.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 9 - 10: ohos.permission.CONNECT_IME_ABILITY

<!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty): Promise<boolean>--><!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-configuration-persistence-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
});
```
