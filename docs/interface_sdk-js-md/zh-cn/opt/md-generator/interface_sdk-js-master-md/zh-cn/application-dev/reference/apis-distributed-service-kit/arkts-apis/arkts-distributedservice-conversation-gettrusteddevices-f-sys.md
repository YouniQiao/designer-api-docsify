# getTrustedDevices（系统接口）

## getTrustedDevices

```TypeScript
function getTrustedDevices(): DeviceNodeInfo[]
```

获取历史可信设备列表。典型使用场景包括：跨设备数据发送前查询可用目标设备。

**起始版本：** 26.1.0

**废弃版本：** -1

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-conversation-function getTrustedDevices(): DeviceNodeInfo[]--><!--Device-conversation-function getTrustedDevices(): DeviceNodeInfo[]-End-->

**系统能力：** SystemCapability.Communication.SoftBus.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [DeviceNodeInfo](arkts-distributedservice-conversation-devicenodeinfo-i-sys.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2000001](../../apis-distributedservice-kit/errorcode-conversation.md#2000001-内部错误) |

## 示例

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
