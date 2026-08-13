# onPostDialDelay (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## onPostDialDelay

```TypeScript
function onPostDialDelay(callback: Callback<string>): void
```

Subscribe to the postDialDelay event.

**Since:** 26.1.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onPostDialDelay(callback: Callback<string>): void--><!--Device-call-function onPostDialDelay(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
