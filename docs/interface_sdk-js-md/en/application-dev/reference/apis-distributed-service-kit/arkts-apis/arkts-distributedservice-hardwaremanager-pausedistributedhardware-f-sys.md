# pauseDistributedHardware (System API)

## Modules to Import

```TypeScript
import { hardwareManager } from 'kits/@kit.DistributedServiceKit';
```

## pauseDistributedHardware

```TypeScript
function pauseDistributedHardware(description: HardwareDescriptor): Promise<void>
```

Pauses the distributed hardware service on the controlled device. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_DISTRIBUTED_HARDWARE

**System capability:** SystemCapability.DistributedHardware.DistributedHardwareFWK

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| description | [HardwareDescriptor](arkts-distributedservice-hardwaremanager-hardwaredescriptor-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 24200101 |
| 24200102 |
