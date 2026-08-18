# activateCooperateWithOptions (System API)

## Modules to Import

```TypeScript
```

## activateCooperateWithOptions

```TypeScript
function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: number,
    cooperateOptions?: CooperateOptions
  ): Promise<void>
```

Starts screen hopping based on the specified options. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,    cooperateOptions?: CooperateOptions  ): Promise<void>--><!--Device-cooperate-function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,    cooperateOptions?: CooperateOptions  ): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetNetworkId | string | Yes |
| inputDeviceId | number | Yes |
| cooperateOptions | [CooperateOptions](arkts-distributedservice-cooperate-cooperateoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20900001](../../apis-distributedservice-kit/errorcode-devicestatus.md#20900001-input-device-operation-failed) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activateCooperateWithOptions(targetNetworkId, inputDeviceId).then(() => {
    console.info(`activateCooperateWithOptions success.`);
  }, (error: BusinessError) => {
    console.error(`activateCooperateWithOptions, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`activateCooperateWithOptions, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
