# getSerialPortList

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## getSerialPortList

```TypeScript
function getSerialPortList(): Promise<SerialPort[]>
```

获取串口列表。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>--><!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SerialPort[]&gt; | Promise used to return the list of serial port devices. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 203 | This function is prohibited by enterprise management policies. |

