# getSubCallIdList (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## getSubCallIdList

```TypeScript
function getSubCallIdList(callId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains the list of subcall IDs. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-call-function getSubCallIdList(callId: int, callback: AsyncCallback<Array<string>>): void--><!--Device-call-function getSubCallIdList(callId: int, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getSubCallIdList(1, (err: BusinessError, data: Array<string>) => {
    if (err) {
        console.error(`getSubCallIdList fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getSubCallIdList success, data->${JSON.stringify(data)}`);
    }
});
```


## getSubCallIdList

```TypeScript
function getSubCallIdList(callId: number): Promise<Array<string>>
```

Obtains the list of subcall IDs. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-call-function getSubCallIdList(callId: int): Promise<Array<string>>--><!--Device-call-function getSubCallIdList(callId: int): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getSubCallIdList(1).then((data: Array<string>) => {
    console.info(`getSubCallIdList success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSubCallIdList fail, promise: err->${JSON.stringify(err)}`);
});
```
