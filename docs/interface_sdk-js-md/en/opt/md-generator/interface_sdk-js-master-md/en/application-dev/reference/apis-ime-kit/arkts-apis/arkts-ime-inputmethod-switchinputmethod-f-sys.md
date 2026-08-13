# switchInputMethod (System API)

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## switchInputMethod

```TypeScript
function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>
```

Switches to another input method. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-inputMethod-function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>--><!--Device-inputMethod-function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| subtypeId | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-configuration-persistence-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

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
