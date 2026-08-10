# kickOutFromConference (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## kickOutFromConference

```TypeScript
function kickOutFromConference(callId: int, callback: AsyncCallback<void>): void
```

Kick out call from the conference call.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function kickOutFromConference(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function kickOutFromConference(callId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the identifier of the call which kick out. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of kickOutFromConference. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.kickOutFromConference(1, (err: BusinessError) => {
    if (err) {
        console.error(`kickOutFromConference fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`kickOutFromConference success.`);
    }
});
```


## kickOutFromConference

```TypeScript
function kickOutFromConference(callId: int): Promise<void>
```

Kick out call from the conference call.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function kickOutFromConference(callId: int): Promise<void>--><!--Device-call-function kickOutFromConference(callId: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the identifier of the call which kick out. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the kickOutFromConference. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.kickOutFromConference(1).then(() => {
    console.info(`kickOutFromConference success.`);
}).catch((err: BusinessError) => {
    console.error(`kickOutFromConference fail, promise: err->${JSON.stringify(err)}`);
});
```

