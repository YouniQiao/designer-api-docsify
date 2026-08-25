# createDeviceManager（系统接口）

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DistributedServiceKit';
```

## createDeviceManager

```TypeScript
function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void
```

创建一个设备管理器实例。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [createDeviceManager](arkts-distributedservice-distributeddevicemanager-createdevicemanager-f.md)

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceManager&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
