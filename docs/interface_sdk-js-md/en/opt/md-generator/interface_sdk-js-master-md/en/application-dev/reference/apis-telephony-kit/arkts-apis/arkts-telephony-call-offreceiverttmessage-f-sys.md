# offReceiveRttMessage (System API)

## Modules to Import

```TypeScript
```

## offReceiveRttMessage

```TypeScript
function offReceiveRttMessage(callback?: Callback<RttMessageInfo>): void
```

Unsubscribe from the rtt message event.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function offReceiveRttMessage(callback?: Callback<RttMessageInfo>): void--><!--Device-call-function offReceiveRttMessage(callback?: Callback<RttMessageInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RttMessageInfo](arkts-telephony-call-rttmessageinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
