# requestSerialRight

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## requestSerialRight

```TypeScript
function requestSerialRight(portId: number): Promise<boolean>
```

请求应用访问串口设备的权限。应用退出时自动移除对串口设备的访问权限，在应用重启后需要重新申请授权。使用Promise异步回调。通常在首次访问串口设备前、检测到无权限时调用此接口向用户申请授权，如需移除权限请调用 [cancelSerialRight](arkts-basicservices-serialmanager-cancelserialright-f.md)。  
**前置条件：**  
- 需要先调用[getPortList](arkts-basicservices-serialmanager-getportlist-f.md)获取端口号

**起始版本：** 19

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14400005](../errorcode-usb.md#14400005-数据库操作异常) |
| [31400001](../errorcode-usb.md#31400001-串口服务异常) |
| [31400003](../errorcode-usb.md#31400003-端口号不存在) |
