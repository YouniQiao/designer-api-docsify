# @ohos.usbManager.serial

本模块主要用于管理串口设备的访问和通信，提供打开和关闭设备、读写数据、配置参数、权限管理等功能，解决了应用与串口设备通信时的权限申请、设备配置、数据传输等问题，使用该模块可以简化串口设备访问流程，提高开发效率。  
**典型使用流程：**  
**使用场景**：  
- **嵌入式设备通信**：与各类嵌入式设备进行数据交互，如传感器数据采集、设备状态监控等  
- **工业设备调试**：连接工业控制设备，进行参数配置、命令下发、日志输出等调试操作  
- **串口外设数据交互**：与串口外设进行数据通信，如打印机、扫描仪、调制解调器等设备的数据收发

**起始版本：** 19

**系统能力：** SystemCapability.USB.USBManager.Serial

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [cancelSerialRight](arkts-basicservices-serialmanager-cancelserialright-f.md) |
| [close](arkts-basicservices-serialmanager-close-f.md) |
| [getAttribute](arkts-basicservices-serialmanager-getattribute-f.md) |
| [getPortList](arkts-basicservices-serialmanager-getportlist-f.md) |
| [hasSerialRight](arkts-basicservices-serialmanager-hasserialright-f.md) |
| [open](arkts-basicservices-serialmanager-open-f.md) |
| [read](arkts-basicservices-serialmanager-read-f.md) |
| [readSync](arkts-basicservices-serialmanager-readsync-f.md) |
| [requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md) |
| [setAttribute](arkts-basicservices-serialmanager-setattribute-f.md) |
| [write](arkts-basicservices-serialmanager-write-f.md) |
| [writeSync](arkts-basicservices-serialmanager-writesync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addSerialRight](arkts-basicservices-serialmanager-addserialright-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [SerialAttribute](arkts-basicservices-serialmanager-serialattribute-i.md) |
| [SerialPort](arkts-basicservices-serialmanager-serialport-i.md) |

### 枚举

| 名称 |
| --- |
| [BaudRates](arkts-basicservices-serialmanager-baudrates-e.md) |
| [DataBits](arkts-basicservices-serialmanager-databits-e.md) |
| [Parity](arkts-basicservices-serialmanager-parity-e.md) |
| [StopBits](arkts-basicservices-serialmanager-stopbits-e.md) |
