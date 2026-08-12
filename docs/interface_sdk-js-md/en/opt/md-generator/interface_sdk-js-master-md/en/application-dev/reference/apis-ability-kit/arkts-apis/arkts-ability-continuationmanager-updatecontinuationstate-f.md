# updateContinuationState

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## updateContinuationState

```TypeScript
function updateContinuationState(
    token: number,
    deviceId: string,
    status: DeviceConnectState,
    callback: AsyncCallback<void>
  ): void
```

Instructs the device selection module to update the device connection state. This API uses an asynchronous callback  to return the result.

**Since:** 9

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function updateContinuationState(    token: number,    deviceId: string,    status: DeviceConnectState,    callback: AsyncCallback<void>  ): void--><!--Device-continuationManager-function updateContinuationState(    token: number,    deviceId: string,    status: DeviceConnectState,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| deviceId | string | Yes |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
let deviceId: string = "test deviceId";
try {
  continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
    if (err.code != 0) {
      console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('updateContinuationState finished. ');
  });
} catch (err) {
  console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
}
```


## updateContinuationState

```TypeScript
function updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>
```

Instructs the device selection module to update the device connection state. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>--><!--Device-continuationManager-function updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| deviceId | string | Yes |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
let deviceId: string = "test deviceId";
try {
  continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
    .then(() => {
      console.info('updateContinuationState finished. ');
    })
    .catch((err: BusinessError) => {
      console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
}
```
