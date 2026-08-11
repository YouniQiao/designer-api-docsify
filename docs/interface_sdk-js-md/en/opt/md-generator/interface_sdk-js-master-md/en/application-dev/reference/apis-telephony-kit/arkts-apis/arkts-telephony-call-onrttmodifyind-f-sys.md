# onRttModifyInd (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## onRttModifyInd

```TypeScript
function onRttModifyInd(callback: Callback<RttEventInfo>): void
```

Subscribe to the rtt modify indication.

**Since:** 22

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onRttModifyInd(callback: Callback<RttEventInfo>): void--><!--Device-call-function onRttModifyInd(callback: Callback<RttEventInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RttEventInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
