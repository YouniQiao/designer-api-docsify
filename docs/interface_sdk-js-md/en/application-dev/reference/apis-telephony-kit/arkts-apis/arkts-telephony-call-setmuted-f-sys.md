# setMuted (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## setMuted

```TypeScript
function setMuted(callback: AsyncCallback<void>): void
```

Set mute during a call.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-call-function setMuted(callback: AsyncCallback<void>): void--><!--Device-call-function setMuted(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of setMuted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.setMuted((err: BusinessError) => {
    if (err) {
        console.error(`setMuted fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setMuted success.`);
    }
});
```


## setMuted

```TypeScript
function setMuted(): Promise<void>
```

Set mute during a call.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-call-function setMuted(): Promise<void>--><!--Device-call-function setMuted(): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setMuted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.setMuted().then(() => {
    console.info(`setMuted success.`);
}).catch((err: BusinessError) => {
    console.error(`setMuted fail, promise: err->${JSON.stringify(err)}`);
});
```

