# getCurrentInputMethod (System API)

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getCurrentInputMethod

```TypeScript
function getCurrentInputMethod(userId?: number): InputMethodProperty
```

Get the current input method of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-function getCurrentInputMethod(userId?: int): InputMethodProperty--><!--Device-inputMethod-function getCurrentInputMethod(userId?: int): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 12800023 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 12800025 |
| [12800008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800024 |
