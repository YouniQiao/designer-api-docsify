# unbindDevice

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## unbindDevice

```TypeScript
function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void
```

解除设备绑定。必须先通过bindDevice接口绑定设备。

**起始版本：** 10

**废弃版本：** 19

**替代接口：** [unbindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-unbinddriverwithdeviceid-f.md)(deviceId: long)

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [22900001](../errorcode-deviceManager.md#22900001-扩展外设驱动服务异常或bustype参数错误) |


## unbindDevice

```TypeScript
function unbindDevice(deviceId: number): Promise<number>
```

解除设备绑定。必须先通过bindDevice接口绑定设备。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 19

**替代接口：** [unbindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-unbinddriverwithdeviceid-f.md)(deviceId: long)

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [22900001](../errorcode-deviceManager.md#22900001-扩展外设驱动服务异常或bustype参数错误) |
