# offRttModifyInd (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## offRttModifyInd

```TypeScript
function offRttModifyInd(callback?: Callback<RttEventInfo>): void
```

Unsubscribe from the rtt modify indication.

**Since:** 22

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function offRttModifyInd(callback?: Callback<RttEventInfo>): void--><!--Device-call-function offRttModifyInd(callback?: Callback<RttEventInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RttEventInfo](arkts-telephony-call-rtteventinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
