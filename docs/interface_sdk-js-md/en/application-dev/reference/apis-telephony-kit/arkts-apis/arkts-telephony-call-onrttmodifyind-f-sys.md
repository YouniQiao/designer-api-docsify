# onRttModifyInd (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## onRttModifyInd

```TypeScript
function onRttModifyInd(callback: Callback<RttEventInfo>): void
```

Subscribe to the rtt modify indication.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onRttModifyInd(callback: Callback<RttEventInfo>): void--><!--Device-call-function onRttModifyInd(callback: Callback<RttEventInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[RttEventInfo](arkts-telephony-call-rtteventinfo-i-sys.md)&gt; | Yes | Indicates the callback for getting the rtt event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

