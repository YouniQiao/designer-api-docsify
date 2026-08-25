# createDeviceManager

## 导入模块

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## createDeviceManager

```TypeScript
function createDeviceManager(bundleName: string): DeviceManager
```

创建一个设备管理实例，是分布式设备管理方法的调用入口。该实例用于获取可信设备列表以及本地设备的名称、 类型、标识和网络标识等信息。当设备管理实例不再使用时，应调用releaseDeviceManager释放该实例，避免资源泄漏。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
