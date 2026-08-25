# @ohos.busManager.serial(串口通信管理)

本模块提供串口通信管理功能，适用于需要与串口设备进行数据交互的场景，如工业控制、传感器数据采集、嵌入式设备通信等。支持获取串口设备列表、 打开和关闭串口、读写数据、硬件流控信号管理等功能，帮助开发者便捷地实现与外部串口设备的通信，提高设备互联效率。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BusManager.Serial

## 导入模块

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getSerialPortList(串口通信管理)](arkts-basicservices-serial-getserialportlist-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addPortAuthorization(串口通信管理)](arkts-basicservices-serial-addportauthorization-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [SerialConfigs(串口通信管理)](arkts-basicservices-serial-serialconfigs-i.md) |
| [SerialPort(串口通信管理)](arkts-basicservices-serial-serialport-i.md) |
| [SerialPortInfo(串口通信管理)](arkts-basicservices-serial-serialportinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [DataBits(串口通信管理)](arkts-basicservices-serial-databits-e.md) |
| [Parity(串口通信管理)](arkts-basicservices-serial-parity-e.md) |
| [StopBits(串口通信管理)](arkts-basicservices-serial-stopbits-e.md) |
