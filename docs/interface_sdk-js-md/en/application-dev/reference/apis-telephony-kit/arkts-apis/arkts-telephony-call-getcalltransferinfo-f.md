# getCallTransferInfo

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## getCallTransferInfo

```TypeScript
function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>
```

Obtains call transfer information with the phone number. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_CALL_TRANSFER_INFO

<!--Device-call-function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>--><!--Device-call-function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [CallTransferType](arkts-telephony-call-calltransfertype-e.md) | Yes | Type of call forwarding to be obtained. |
| number | string | Yes | Number used to obtain the call forwarding status. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CallTransferResult](arkts-telephony-call-calltransferresult-i.md)&gt; | Promise used to return the call forwarding result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8401002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8401002-incorrect-number) | Invalid input call number. |
| [8401003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8401003-frequent-operations) | Operation too frequent. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

