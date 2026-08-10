# getSerialPortList

## 导入模块

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## getSerialPortList

```TypeScript
function getSerialPortList(): Promise<SerialPort[]>
```

获取串口列表。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>--><!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;SerialPort[]&gt; | Promise used to return the list of serial port devices. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 35700001 | Service error. |
| 203 | This function is prohibited by enterprise management policies. |

