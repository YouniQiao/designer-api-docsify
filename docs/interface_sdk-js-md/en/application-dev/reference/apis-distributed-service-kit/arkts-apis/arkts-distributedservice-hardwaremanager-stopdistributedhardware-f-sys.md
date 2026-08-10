# stopDistributedHardware (System API)

## Modules to Import

```TypeScript
import { hardwareManager } from 'kits/@kit.DistributedServiceKit';
```

## stopDistributedHardware

```TypeScript
function stopDistributedHardware(description: HardwareDescriptor): Promise<void>
```

停止被控端分布式硬件业务。使用promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_DISTRIBUTED_HARDWARE

<!--Device-hardwareManager-function stopDistributedHardware(description: HardwareDescriptor): Promise<void>--><!--Device-hardwareManager-function stopDistributedHardware(description: HardwareDescriptor): Promise<void>-End-->

**System capability:** SystemCapability.DistributedHardware.DistributedHardwareFWK

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | [HardwareDescriptor](arkts-distributedservice-hardwaremanager-hardwaredescriptor-i-sys.md) | Yes | 硬件描述信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Input parameter error. |
| 24200101 | The specified distributed hardware is not started. |
| 24200102 | The specified source device is not connected. |
| 201 | Permission verification failed. |
| 202 | Permission denied, non-system app called system api. |

## Examples

```TypeScript
import { hardwareManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let description: hardwareManager.HardwareDescriptor = {
    type: 1,
    srcNetworkId: '1111'
  };
  hardwareManager.stopDistributedHardware(description).then(() => {
    console.info('stop distributed hardware successfully');
  }).catch((error: BusinessError) => {
    console.error('stop distributed hardware failed, cause:' + error);
  })
  console.info('stop distributed hardware successfully');
} catch (error) {
  console.error('stop distributed hardware failed:' + error);
}
```

