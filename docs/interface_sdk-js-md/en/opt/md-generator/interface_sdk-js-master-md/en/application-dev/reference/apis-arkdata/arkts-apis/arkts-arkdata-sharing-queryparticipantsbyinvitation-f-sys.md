# queryParticipantsByInvitation (System API)

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## queryParticipantsByInvitation

```TypeScript
function queryParticipantsByInvitation(
      invitationCode: string,
      callback: AsyncCallback<Result<Array<Participant>>>
    ): void
```

Queries the participants based on the sharing invitation code. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function queryParticipantsByInvitation(      invitationCode: string,      callback: AsyncCallback<Result<Array<Participant>>>    ): void--><!--Device-sharing-function queryParticipantsByInvitation(      invitationCode: string,      callback: AsyncCallback<Result<Array<Participant>>>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| invitationCode | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.queryParticipantsByInvitation('sharing_invitation_code_test', ((err: BusinessError, result) => {
  if (err) {
    console.error(`query participants by invitation failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`query participants by invitation succeeded, result: ${result}`);
}))
```


## queryParticipantsByInvitation

```TypeScript
function queryParticipantsByInvitation(invitationCode: string): Promise<Result<Array<Participant>>>
```

Queries the participants based on the sharing invitation code. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function queryParticipantsByInvitation(invitationCode: string): Promise<Result<Array<Participant>>>--><!--Device-sharing-function queryParticipantsByInvitation(invitationCode: string): Promise<Result<Array<Participant>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| invitationCode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.queryParticipantsByInvitation('sharing_invitation_code_test').then((result) => {
  console.info(`query participants by invitation succeeded, result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`query participants by invitation failed, code is ${err.code},message is ${err.message}`);
})
```
