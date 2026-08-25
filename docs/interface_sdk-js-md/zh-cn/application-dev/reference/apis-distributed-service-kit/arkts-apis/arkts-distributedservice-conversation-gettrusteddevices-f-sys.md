# getTrustedDevices（系统接口）

## 导入模块

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## getTrustedDevices

```TypeScript
function getTrustedDevices(): DeviceNodeInfo[]
```

获取历史可信设备列表。典型使用场景包括：跨设备数据发送前查询可用目标设备。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.SoftBus.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [DeviceNodeInfo](arkts-distributedservice-conversation-devicenodeinfo-i-sys.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2000001](../errorcode-conversation.md#2000001-内部错误) |
