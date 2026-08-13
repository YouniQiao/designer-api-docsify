# confirmInvitation (System API)

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## confirmInvitation

```TypeScript
function confirmInvitation(invitationCode: string, state: State, callback: AsyncCallback<Result<string>>): void
```

Confirms the invitation based on the sharing invitation code and obtains the shared resource ID. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function confirmInvitation(invitationCode: string, state: State, callback: AsyncCallback<Result<string>>): void--><!--Device-sharing-function confirmInvitation(invitationCode: string, state: State, callback: AsyncCallback<Result<string>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| invitationCode | string | Yes |
| state | [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let shareResource: string;
cloudData.sharing.confirmInvitation('sharing_invitation_code_test', cloudData.sharing.State.STATE_ACCEPTED, ((err: BusinessError, result) => {
  if (err) {
    console.error(`confirm invitation failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`confirm invitation succeeded, result: ${result}`);
  shareResource = result.value;
}))
```


## confirmInvitation

```TypeScript
function confirmInvitation(invitationCode: string, state: State): Promise<Result<string>>
```

Confirms the invitation based on the sharing invitation code and obtains the shared resource ID. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function confirmInvitation(invitationCode: string, state: State): Promise<Result<string>>--><!--Device-sharing-function confirmInvitation(invitationCode: string, state: State): Promise<Result<string>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| invitationCode | string | Yes |
| state | [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let shareResource: string | undefined;
cloudData.sharing.confirmInvitation('sharing_invitation_code_test', cloudData.sharing.State.STATE_ACCEPTED).then((result: cloudData.sharing.Result<string>) => {
  console.info(`confirm invitation succeeded, result: ${result}`);
  shareResource = result.value;
}).catch((err: BusinessError) => {
  console.error(`confirm invitation failed, code is ${err.code},message is ${err.message}`);
})
```
