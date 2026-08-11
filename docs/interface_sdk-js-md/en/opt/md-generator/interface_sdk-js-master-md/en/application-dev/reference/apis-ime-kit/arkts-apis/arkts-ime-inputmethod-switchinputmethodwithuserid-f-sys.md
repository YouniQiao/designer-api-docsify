# switchInputMethodWithUserId (System API)

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## switchInputMethodWithUserId

```TypeScript
function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: number): Promise<void>
```

Switch input method and subtype of a specified user.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>--><!--Device-inputMethod-function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| subtypeId | string | No |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 12800023 |
| [12800005](../errorcode-inputmethod-framework.md#12800005-configuration-persistence-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 12800025 |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| 12800024 |
