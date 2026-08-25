# bindDeviceDriver

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## bindDeviceDriver

```TypeScript
function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>,
    callback: AsyncCallback<RemoteDeviceDriver>): void
```

根据queryDevices()返回的设备信息绑定设备。必须与unbindDevice接口成对使用。需要调用[deviceManager.queryDevices()](arkts-driverdevelopment-devicemanager-querydevices-f.md)获取设备信息列表。

**起始版本：** 11

**废弃版本：** 19

**替代接口：** [bindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-binddriverwithdeviceid-f.md)(deviceId: long, onDisconnect: AsyncCallback&lt;long&gt;)

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| onDisconnect | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RemoteDeviceDriver](arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [22900001](../errorcode-deviceManager.md#22900001-扩展外设驱动服务异常或bustype参数错误) |


## bindDeviceDriver

```TypeScript
function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>
```

根据queryDevices()返回的设备信息绑定设备。必须与unbindDevice接口成对使用。使用Promise异步回调。需要调用[deviceManager.queryDevices](arkts-driverdevelopment-devicemanager-querydevices-f.md)获取设备信息列表。

**起始版本：** 11

**废弃版本：** 19

**替代接口：** [bindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-binddriverwithdeviceid-f.md)(deviceId: long, onDisconnect: AsyncCallback&lt;long&gt;)

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| onDisconnect | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RemoteDeviceDriver](arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [22900001](../errorcode-deviceManager.md#22900001-扩展外设驱动服务异常或bustype参数错误) |
