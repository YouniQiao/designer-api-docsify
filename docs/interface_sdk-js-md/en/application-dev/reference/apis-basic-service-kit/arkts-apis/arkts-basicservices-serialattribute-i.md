# SerialAttribute

Represents the configuration parameters of a serial port.

**Since:** 19

<!--Device-serialManager-interface SerialAttribute--><!--Device-serialManager-interface SerialAttribute-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## baudRate

```TypeScript
baudRate: BaudRates
```

Baud rate.

**Type:** BaudRates

**Since:** 19

<!--Device-SerialAttribute-baudRate: BaudRates--><!--Device-SerialAttribute-baudRate: BaudRates-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## dataBits

```TypeScript
dataBits?: DataBits
```

Data bits. The default value is **8**.

**Type:** DataBits

**Default:** DATABIT_8

**Since:** 19

<!--Device-SerialAttribute-dataBits?: DataBits--><!--Device-SerialAttribute-dataBits?: DataBits-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## parity

```TypeScript
parity?: Parity
```

Parity check. The default value is **None**, indicating that no parity check is performed.

**Type:** Parity

**Default:** NONE

**Since:** 19

<!--Device-SerialAttribute-parity?: Parity--><!--Device-SerialAttribute-parity?: Parity-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## stopBits

```TypeScript
stopBits?: StopBits
```

Stop bits. The default value is **1**.

**Type:** StopBits

**Default:** STOPBIT_1

**Since:** 19

<!--Device-SerialAttribute-stopBits?: StopBits--><!--Device-SerialAttribute-stopBits?: StopBits-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

