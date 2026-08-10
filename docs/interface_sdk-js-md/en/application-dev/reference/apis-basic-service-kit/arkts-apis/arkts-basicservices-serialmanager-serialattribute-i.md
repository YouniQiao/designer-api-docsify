# SerialAttribute

串口的配置参数。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-serialManager-interface SerialAttribute--><!--Device-serialManager-interface SerialAttribute-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## baudRate

```TypeScript
baudRate: BaudRates
```

串口波特率。

**Type:** [BaudRates](arkts-basicservices-serialmanager-baudrates-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SerialAttribute-baudRate: BaudRates--><!--Device-SerialAttribute-baudRate: BaudRates-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## dataBits

```TypeScript
dataBits?: DataBits
```

串口数据位，默认值为8位。

**Type:** [DataBits](arkts-basicservices-serial-databits-e.md)

**Default:** DATABIT_8

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SerialAttribute-dataBits?: DataBits--><!--Device-SerialAttribute-dataBits?: DataBits-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## parity

```TypeScript
parity?: Parity
```

串口奇偶校验，默认值为None，无奇偶校验。

**Type:** [Parity](arkts-basicservices-serialmanager-parity-e.md)

**Default:** NONE

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SerialAttribute-parity?: Parity--><!--Device-SerialAttribute-parity?: Parity-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## stopBits

```TypeScript
stopBits?: StopBits
```

串口停止位，默认值为1位。

**Type:** [StopBits](arkts-basicservices-serial-stopbits-e.md)

**Default:** STOPBIT_1

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SerialAttribute-stopBits?: StopBits--><!--Device-SerialAttribute-stopBits?: StopBits-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

