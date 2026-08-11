# resumeDistributedHardware (System API)

## Modules to Import

```TypeScript
import { hardwareManager } from 'kits/@kit.DistributedServiceKit';
```

## resumeDistributedHardware

```TypeScript
function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>
```

Resumes the distributed hardware service on the controlled device. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_DISTRIBUTED_HARDWARE

<!--Device-hardwareManager-function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>--><!--Device-hardwareManager-function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>-End-->

**System capability:** SystemCapability.DistributedHardware.DistributedHardwareFWK

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| description | [HardwareDescriptor](arkts-distributedservice-hardwaremanager-hardwaredescriptor-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 24200101 |
| 24200102 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { hardwareManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let description: hardwareManager.HardwareDescriptor = {
    type: 1,
    srcNetworkId: '1111'
  };
  hardwareManager.resumeDistributedHardware(description).then(() => {
    console.info('resume distributed hardware successfully');
  }).catch((error: BusinessError) => {
    console.error('resume distributed hardware failed, cause:' + error);
  })
  console.info('resume distributed hardware successfully');
} catch (error) {
  console.error('resume distributed hardware failed:' + error);
}
```
