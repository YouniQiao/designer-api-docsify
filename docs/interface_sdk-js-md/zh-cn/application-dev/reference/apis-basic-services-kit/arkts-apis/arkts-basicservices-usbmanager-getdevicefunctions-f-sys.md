# getDeviceFunctions（系统接口）

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## getDeviceFunctions

```TypeScript
function getDeviceFunctions(): FunctionType
```

在设备模式下，获取当前的USB功能列表的数字组合掩码。适用于需要检查当前USB功能状态、确认功能配置、或在功能切换前后进行状态对比的场景。开发者模式关闭时，如果没有设备接入，接口返回`undefined`，注意需要对接口返回值做判 空处理。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
