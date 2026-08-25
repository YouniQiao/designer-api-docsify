# writeSync

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## writeSync

```TypeScript
function writeSync(portId: number, buffer: Uint8Array, timeout?: number): number
```

向串口设备同步写数据，使用前需先调用[open](arkts-basicservices-serialmanager-open-f.md)打开串口设备。每次写入数据长度不超过4KB，数据过大会导致数据丢失，长数据建议分包写入。适用于需要阻塞式等待写入完成、发送重要指令 、或对写入顺序有严格要求的场景。  
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
| buffer | Uint8Array | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [31400001](../errorcode-usb.md#31400001-串口服务异常) |
| [31400003](../errorcode-usb.md#31400003-端口号不存在) |
| [31400005](../errorcode-usb.md#31400005-设备未打开) |
| [31400006](../errorcode-usb.md#31400006-传输超时) |
| [31400007](../errorcode-usb.md#31400007-io异常) |
