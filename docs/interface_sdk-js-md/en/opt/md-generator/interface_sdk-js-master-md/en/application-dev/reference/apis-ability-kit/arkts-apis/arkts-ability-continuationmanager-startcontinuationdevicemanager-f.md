# startContinuationDeviceManager

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void
```

Starts the device selection module to show the list of available devices on the network. This API does not involve any filter parameters and uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(token, (err) => {
    if (err.code != 0) {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```


## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(
    token: number,
    options: ContinuationExtraParams,
    callback: AsyncCallback<void>
  ): void
```

Starts the device selection module to show the list of available devices on the network. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function startContinuationDeviceManager(    token: number,    options: ContinuationExtraParams,    callback: AsyncCallback<void>  ): void--><!--Device-continuationManager-function startContinuationDeviceManager(    token: number,    options: ContinuationExtraParams,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    },
    (err) => {
      if (err.code != 0) {
        console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```


## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>
```

Starts the device selection module to show the list of available devices on the network. This API uses a promise to  return the result.

**Since:** 9

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>--><!--Device-continuationManager-function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    }).then(() => {
      console.info('startContinuationDeviceManager finished. ');
    }).catch((err: BusinessError) => {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```
