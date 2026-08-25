# closePipe

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): number
```

关闭设备连接通道。
1. 调用[usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md)获取设备列表；
2. 调用[usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md)获取设备请求权限；
3. 调用[usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md)得到devicepipe作为参数。

**起始版本：** 9

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
