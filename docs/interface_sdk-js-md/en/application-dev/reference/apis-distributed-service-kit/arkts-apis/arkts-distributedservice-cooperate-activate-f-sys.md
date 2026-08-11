# activate (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## activate

```TypeScript
function activate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void
```

Starts screen hopping. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate)(targetNetworkId:

<!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void--><!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetNetworkId | string | Yes | Descriptor of the target device for screen hopping. |
| inputDeviceId | number | Yes | Identifier of the input device for screen hopping. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the operation result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [20900001](../../apis-input-kit/errorcode-cooperator.md#20900001-service-exception) | Service exception. Possible causes: &lt;br&gt;1. A system error, such as null pointer, container-related exception, or IPC exception. &lt;br&gt;2. N-API invocation exception or invalid N-API status. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activate(targetNetworkId, inputDeviceId, (error: BusinessError) => {
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


## activate

```TypeScript
function activate(targetNetworkId: string, inputDeviceId: number): Promise<void>
```

Starts screen hopping. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate)(targetNetworkId:

<!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number): Promise<void>--><!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetNetworkId | string | Yes | Descriptor of the target device for screen hopping. |
| inputDeviceId | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [20900001](../../apis-input-kit/errorcode-cooperator.md#20900001-service-exception) | Service exception. Possible causes: &lt;br&gt;1. A system error, such as null pointer, container-related exception, or IPC exception. &lt;br&gt;2. N-API invocation exception or invalid N-API status. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activate(targetNetworkId, inputDeviceId).then(() => {
    console.info(`Start Keyboard mouse crossing success.`);
  }, (error: BusinessError) => {
    console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```

