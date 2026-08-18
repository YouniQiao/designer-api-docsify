# queryDeviceInfo（系统接口）

## 导入模块

```TypeScript
```

## queryDeviceInfo

```TypeScript
function queryDeviceInfo(deviceId?: number): Array<Readonly<DeviceInfo>>
```

查询扩展外设详细信息列表。如果没有设备接入，那么将会返回一个空的列表。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

<!--Device-deviceManager-function queryDeviceInfo(deviceId?: long): Array<Readonly<DeviceInfo>>--><!--Device-deviceManager-function queryDeviceInfo(deviceId?: long): Array<Readonly<DeviceInfo>>-End-->

**系统能力：** SystemCapability.Driver.ExternalDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Readonly & lt;DeviceInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [26300001](../../apis-driverdevelopment-kit/errorcode-deviceManager.md#26300001-扩展外设驱动服务异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  let deviceInfos: Array<deviceManager.DeviceInfo> = deviceManager.queryDeviceInfo(12345678);
  for (let item of deviceInfos) {
    console.info(`Device id is ${item.deviceId}`);
  }
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to query device info. Code is ${err.code}, message is ${err.message}`);
}
```
