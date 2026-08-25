# cancelSerialRight

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## cancelSerialRight

```TypeScript
function cancelSerialRight(portId: number): void
```

移除应用运行时访问串口设备的权限。此接口会调用close关闭已打开的串口。通常在需要主动释放权限、切换访问不同设备、或出于安全考虑时调用此接口。  
**前置条件：**  
- 需要先调用[getPortList](arkts-basicservices-serialmanager-getportlist-f.md)获取端口号  
- 需要先调用[requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md)申请访问权限  
**相关方法：**  
- [requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md)：申请访问权限  
- [hasSerialRight](arkts-basicservices-serialmanager-hasserialright-f.md)：检查是否有访问权限

**起始版本：** 19

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14400005](../errorcode-usb.md#14400005-数据库操作异常) |
| [31400001](../errorcode-usb.md#31400001-串口服务异常) |
| [31400002](../errorcode-usb.md#31400002-没有串口设备访问权限) |
| [31400003](../errorcode-usb.md#31400003-端口号不存在) |
