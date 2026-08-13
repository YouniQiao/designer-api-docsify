# changeConfirmation (System API)

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## changeConfirmation

```TypeScript
function changeConfirmation(sharingResource: string, state: State, callback: AsyncCallback<Result<void>>): void
```

Changes the invitation confirmation state based on the shared resource ID. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function changeConfirmation(sharingResource: string, state: State, callback: AsyncCallback<Result<void>>): void--><!--Device-sharing-function changeConfirmation(sharingResource: string, state: State, callback: AsyncCallback<Result<void>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sharingResource | string | Yes |
| state | [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;void&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.changeConfirmation('sharing_resource_test', cloudData.sharing.State.STATE_REJECTED, ((err: BusinessError, result) => {
  if (err) {
    console.error(`change confirmation failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`change confirmation succeeded, result: ${result}`);
}))
```


## changeConfirmation

```TypeScript
function changeConfirmation(sharingResource: string, state: State): Promise<Result<void>>
```

Changes the invitation confirmation state based on the shared resource ID. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sharing-function changeConfirmation(sharingResource: string, state: State): Promise<Result<void>>--><!--Device-sharing-function changeConfirmation(sharingResource: string, state: State): Promise<Result<void>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sharingResource | string | Yes |
| state | [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;void & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.changeConfirmation('sharing_resource_test', cloudData.sharing.State.STATE_REJECTED).then((result) => {
  console.info(`change confirmation succeeded, result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`change confirmation failed, code is ${err.code},message is ${err.message}`);
})
```
