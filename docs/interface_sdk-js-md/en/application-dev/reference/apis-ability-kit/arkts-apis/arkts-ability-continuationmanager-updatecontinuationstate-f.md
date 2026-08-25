# updateContinuationState

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
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

Instructs the device selection module to update the device connection state. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| deviceId | string | Yes |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |


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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |
