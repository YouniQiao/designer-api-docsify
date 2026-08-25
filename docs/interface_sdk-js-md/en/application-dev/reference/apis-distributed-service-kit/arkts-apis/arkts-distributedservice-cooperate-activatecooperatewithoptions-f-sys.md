# activateCooperateWithOptions (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## activateCooperateWithOptions

```TypeScript
function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: number,
    cooperateOptions?: CooperateOptions
  ): Promise<void>
```

Starts screen hopping based on the specified options. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.COOPERATE_MANAGER

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
| [20900001](../errorcode-devicestatus.md#20900001-input-device-operation-failed) |
