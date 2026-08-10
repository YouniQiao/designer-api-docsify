# switchInputMethod (System API)

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## switchInputMethod

```TypeScript
function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>
```

切换输入法，使用promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-inputMethod-function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>--><!--Device-inputMethod-function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 目标输入法包名。 |
| subtypeId | string | No | 输入法子类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 201 | permissions check fails. |
| 202 | not system application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

async function switchInputMethodWithSubtype() {
  // 1. Obtain the current input method.
  const currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
  if (!currentIme) {
    console.error("Failed to get current input method");
    return;
  }
  // 2. Switch the input method.
  await inputMethod.switchInputMethod(currentIme.name);
  console.info('Succeeded in switching inputmethod.');
  // 3. Obtain the current input method subtype.
  const currentSubtype: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
  if (!currentSubtype) {
    console.error("Failed to get current input subtype");
    return;
  }
  // 4. Switch the input method subtype.
  await inputMethod.switchInputMethod(currentIme.name, currentSubtype.id);
  console.info('Succeeded in switching inputmethod.');
}

switchInputMethodWithSubtype();
```

