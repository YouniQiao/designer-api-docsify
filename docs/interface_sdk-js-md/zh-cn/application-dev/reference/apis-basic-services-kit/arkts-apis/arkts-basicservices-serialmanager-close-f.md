# close

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## close

```TypeScript
function close(portId: number): void
```

关闭串口。需要先调用[requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md)申请权限，再调用[open](arkts-basicservices-serialmanager-open-f.md)打开串口。 通常在应用退出时、设备断开连接时、需要释放串口资源时调用此接口。关闭串口不会移除访问权限，如需移除权限请调用cancelSerialRight。  
**配对调用：**  
- 与[open](arkts-basicservices-serialmanager-open-f.md)方法成对使用  
- 打开串口后，使用完毕必须调用本方法关闭串口释放资源  
**前置条件：**  
- 需要先调用[getPortList](arkts-basicservices-serialmanager-getportlist-f.md)获取端口号  
- 需要先调用[requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md)申请访问权限  
- 需要先调用[open](arkts-basicservices-serialmanager-open-f.md)打开串口

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
| [31400001](../errorcode-usb.md#31400001-串口服务异常) |
| [31400003](../errorcode-usb.md#31400003-端口号不存在) |
| [31400005](../errorcode-usb.md#31400005-设备未打开) |
