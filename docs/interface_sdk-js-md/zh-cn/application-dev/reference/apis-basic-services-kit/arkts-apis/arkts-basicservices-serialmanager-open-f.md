# open

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## open

```TypeScript
function open(portId: number): void
```

打开串口设备。使用前需先通过[requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md)申请权限，使用完毕后需调用 [close](arkts-basicservices-serialmanager-close-f.md)关闭串口。调用成功后，可对该串口进行读写、配置参数等操作。  
**前置条件：**  
- 需要先调用[getPortList](arkts-basicservices-serialmanager-getportlist-f.md)获取端口号  
- 需要先调用[requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md)申请访问权限  
**配对调用：**  
- 必须与[close](arkts-basicservices-serialmanager-close-f.md)方法配对使用  
- 打开串口后，使用完毕必须调用close()释放资源

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
| [31400002](../errorcode-usb.md#31400002-没有串口设备访问权限) |
| [31400003](../errorcode-usb.md#31400003-端口号不存在) |
| [31400004](../errorcode-usb.md#31400004-串口设备被占用) |
