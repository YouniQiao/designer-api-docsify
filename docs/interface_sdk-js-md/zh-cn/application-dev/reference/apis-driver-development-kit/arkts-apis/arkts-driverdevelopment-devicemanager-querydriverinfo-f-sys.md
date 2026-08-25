# queryDriverInfo（系统接口）

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## queryDriverInfo

```TypeScript
function queryDriverInfo(driverUid?: string): Array<Readonly<DriverInfo>>
```

查询扩展外设驱动详细信息列表。如果没有设备接入，那么将会返回一个空的列表。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| driverUid | string | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;Readonly&lt;[DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [26300001](../errorcode-deviceManager.md#26300001-扩展外设驱动服务异常) |
