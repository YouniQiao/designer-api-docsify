# getCurrentInputMethodSubtype (System API)

## Modules to Import

```TypeScript
```

## getCurrentInputMethodSubtype

```TypeScript
function getCurrentInputMethodSubtype(userId?: number): InputMethodSubtype
```

Get the current input method subtype of a specified user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-function getCurrentInputMethodSubtype(userId?: int): InputMethodSubtype--><!--Device-inputMethod-function getCurrentInputMethodSubtype(userId?: int): InputMethodSubtype-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 12800023 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 12800025 |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800024 |
