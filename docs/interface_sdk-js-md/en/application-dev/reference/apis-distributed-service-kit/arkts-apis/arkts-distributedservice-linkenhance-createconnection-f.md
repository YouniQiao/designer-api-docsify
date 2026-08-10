# createConnection

## Modules to Import

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## createConnection

```TypeScript
function createConnection(deviceId: string, name: string): Connection
```

作为客户端的设备创建连接对象，以便后续向服务端设备发起连接。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-linkEnhance-function createConnection(deviceId: string, name: string): Connection--><!--Device-linkEnhance-function createConnection(deviceId: string, name: string): Connection-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 连接的目标设备的deviceId，即对端设备的BLE MAC地址。BLE MAC的获取方法，请参考 [查找设备](../../../connectivity/bluetooth/ble-development-guide.md)。 |
| name | string | Yes | 连接的目标设备的服务名，非空字符串，最大长度255字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Connection](arkts-distributedservice-linkenhance-connection-i.md) | 创建成功的连接对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32390206 | Invalid parameter. |
| 801 | Capability not supported because the linkEnhance function has been trimmed<br>**Applicable version:** 26.0.0 and later |
| 201 | Permission denied. |

## Examples

On the device that functions as the client, call the createConnection() to create a Connection object.

```TypeScript
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55"; // BLE MAC address, which needs to be obtained through Bluetooth scanning. For details, see parameter description.
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

