# releaseDeviceManager

## 导入模块

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## releaseDeviceManager

```TypeScript
function releaseDeviceManager(deviceManager: DeviceManager): void
```

设备管理实例不再使用后，通过该方法释放DeviceManager实例。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceManager | [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |
