# unbindDriverWithDeviceId

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## unbindDriverWithDeviceId

```TypeScript
function unbindDriverWithDeviceId(deviceId: number): Promise<number>
```

解除设备绑定，调用前需要先通过bindDriverWithDeviceId绑定设备。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.ACCESS_DDK_DRIVERS

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
| [26300001](../errorcode-deviceManager.md#26300001-扩展外设驱动服务异常) |
| [26300003](../errorcode-deviceManager.md#26300003-驱动客户端未绑定任何驱动服务端) |
