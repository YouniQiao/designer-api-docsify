# startManualNetworkScan (System API)

## Modules to Import

```TypeScript
```

## startManualNetworkScan

```TypeScript
function startManualNetworkScan(slotId: number, callback: Callback<NetworkSearchRealTimeResult>): void
```

start ManualNetworkScan , Real-time report.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function startManualNetworkScan(slotId: int, callback: Callback<NetworkSearchRealTimeResult>): void--><!--Device-radio-function startManualNetworkScan(slotId: int, callback: Callback<NetworkSearchRealTimeResult>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkSearchRealTimeResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
