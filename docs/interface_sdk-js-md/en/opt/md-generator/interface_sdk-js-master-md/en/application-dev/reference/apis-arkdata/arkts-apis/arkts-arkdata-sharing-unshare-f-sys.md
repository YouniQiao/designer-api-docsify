# unshare (System API)

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## unshare

```TypeScript
function unshare(
      sharingResource: string,
      participants: Array<Participant>,
      callback: AsyncCallback<Result<Array<Result<Participant>>>>
    ): void
```

Unshares data based on the specified shared resource ID and participants. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function unshare(      sharingResource: string,      participants: Array<Participant>,      callback: AsyncCallback<Result<Array<Result<Participant>>>>    ): void--><!--Device-sharing-function unshare(      sharingResource: string,      participants: Array<Participant>,      callback: AsyncCallback<Result<Array<Result<Participant>>>>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sharingResource | string | Yes |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;Array&lt;Result&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
})
cloudData.sharing.unshare('sharing_resource_test', participants, ((err: BusinessError, result) => {
  if (err) {
    console.error(`unshare failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`unshare succeeded, result: ${result}`);
}))
```


## unshare

```TypeScript
function unshare(
      sharingResource: string,
      participants: Array<Participant>
    ): Promise<Result<Array<Result<Participant>>>>
```

Unshares data based on the specified shared resource ID and participants. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function unshare(      sharingResource: string,      participants: Array<Participant>    ): Promise<Result<Array<Result<Participant>>>>--><!--Device-sharing-function unshare(      sharingResource: string,      participants: Array<Participant>    ): Promise<Result<Array<Result<Participant>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sharingResource | string | Yes |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;Array&lt;Result&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
})
cloudData.sharing.unshare('sharing_resource_test', participants).then((result) => {
  console.info(`unshare succeeded, result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`unshare failed, code is ${err.code},message is ${err.message}`);
})
```
