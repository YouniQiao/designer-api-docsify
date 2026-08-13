# activateCooperate (System API)

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## activateCooperate

```TypeScript
function activateCooperate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void
```

Starts screen hopping. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function activateCooperate(targetNetworkId: string, inputDeviceId: int, callback: AsyncCallback<void>): void--><!--Device-cooperate-function activateCooperate(targetNetworkId: string, inputDeviceId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetNetworkId | string | Yes |
| inputDeviceId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20900001](../../apis-distributedservice-kit/errorcode-devicestatus.md#20900001-input-device-operation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activateCooperate(targetNetworkId, inputDeviceId, (error: BusinessError) => {
    if (error) {
      console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
      return;
    }
    console.info(`Start Keyboard mouse crossing success.`);
  });
} catch (error) {
  console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```


## activateCooperate

```TypeScript
function activateCooperate(targetNetworkId: string, inputDeviceId: number): Promise<void>
```

Starts screen hopping. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function activateCooperate(targetNetworkId: string, inputDeviceId: int): Promise<void>--><!--Device-cooperate-function activateCooperate(targetNetworkId: string, inputDeviceId: int): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetNetworkId | string | Yes |
| inputDeviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20900001](../../apis-distributedservice-kit/errorcode-devicestatus.md#20900001-input-device-operation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activateCooperate(targetNetworkId, inputDeviceId).then(() => {
    console.info(`Start Keyboard mouse crossing success.`);
  }, (error: BusinessError) => {
    console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
