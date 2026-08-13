# joinConference (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## joinConference

```TypeScript
function joinConference(mainCallId: number, callNumberList: Array<string>, callback: AsyncCallback<void>): void
```

Joins a conference call. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mainCallId | number | Yes |
| callNumberList | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callNumberList: Array<string> = [
    "138XXXXXXXX"
];
call.joinConference(1, callNumberList, (err: BusinessError) => {
    if (err) {
        console.error(`joinConference fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`joinConference success.`);
    }
});
```


## joinConference

```TypeScript
function joinConference(mainCallId: number, callNumberList: Array<string>): Promise<void>
```

Joins a conference call. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>): Promise<void>--><!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mainCallId | number | Yes |
| callNumberList | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callNumberList: Array<string> = [
    "138XXXXXXXX"
];
call.joinConference(1, callNumberList).then(() => {
    console.info(`joinConference success.`);
}).catch((err: BusinessError) => {
    console.error(`joinConference fail, promise: err->${JSON.stringify(err)}`);
});
```
