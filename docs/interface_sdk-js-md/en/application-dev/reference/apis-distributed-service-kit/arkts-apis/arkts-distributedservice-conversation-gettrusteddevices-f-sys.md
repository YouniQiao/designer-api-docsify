# getTrustedDevices (System API)

## Modules to Import

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## getTrustedDevices

```TypeScript
function getTrustedDevices(): DeviceNodeInfo[]
```

获取历史可信设备列表。典型使用场景包括：跨设备数据发送前查询可用目标设备。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-conversation-function getTrustedDevices(): DeviceNodeInfo[]--><!--Device-conversation-function getTrustedDevices(): DeviceNodeInfo[]-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [DeviceNodeInfo](arkts-distributedservice-conversation-devicenodeinfo-i-sys.md)[] | 获取到的设备信息列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. The application does not have the required permission to access distributed data. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 2000001 | Internal error. |

## Examples

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let devices: conversation.DeviceNodeInfo[] = conversation.getTrustedDevices();
  console.info(`getTrustedDevices success, count: ${devices.length}`);
  for (let device of devices) {
    console.info(`device name: ${device.deviceName}, networkId: ${device.networkId}`);
  }
} catch (err) {
  const e: BusinessError = err as BusinessError;
  console.error(`getTrustedDevices errCode: ${e.code}, errMessage: ${e.message}`);
}
```

