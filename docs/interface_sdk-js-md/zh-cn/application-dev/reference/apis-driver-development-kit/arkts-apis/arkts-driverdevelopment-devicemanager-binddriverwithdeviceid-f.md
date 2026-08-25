# bindDriverWithDeviceId

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## bindDriverWithDeviceId

```TypeScript
function bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>
```

根据queryDevices()返回的设备信息绑定设备，必须与unbindDriverWithDeviceId接口成对使用。使用Promise异步回调。需要调用[deviceManager.queryDevices](arkts-driverdevelopment-devicemanager-querydevices-f.md)获取设备信息列表。

**起始版本：** 19

**需要权限：** ohos.permission.ACCESS_DDK_DRIVERS

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
| [26300001](../errorcode-deviceManager.md#26300001-扩展外设驱动服务异常) |
| [26300002](../errorcode-deviceManager.md#26300002-驱动服务端不允许驱动客户端绑定) |
