# combineConference (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## combineConference

```TypeScript
function combineConference(callId: number, callback: AsyncCallback<void>): void
```

Merge calls, merge two calls into conference calls.

**Since:** 11

<!--Device-call-function combineConference(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function combineConference(callId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 8300007 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.combineConference(1, (err: BusinessError) => {
    if (err) {
        console.error(`combineConference fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`combineConference success.`);
    }
});
```


## combineConference

```TypeScript
function combineConference(callId: number): Promise<void>
```

Merge calls, merge two calls into conference calls.

**Since:** 11

<!--Device-call-function combineConference(callId: int): Promise<void>--><!--Device-call-function combineConference(callId: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 8300007 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.combineConference(1).then(() => {
    console.info(`combineConference success.`);
}).catch((err: BusinessError) => {
    console.error(`combineConference fail, promise: err->${JSON.stringify(err)}`);
});
```
