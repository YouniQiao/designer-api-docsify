# SerialConfigs

Serial port communication configuration.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-serial-interface SerialConfigs--><!--Device-serial-interface SerialConfigs-End-->

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from '@kit.BasicServicesKit';
```

## baudRate

```TypeScript
baudRate?: number
```

Baud rate. The value must be an integer. Value constraint: standard baud rates. &lt;br&gt;Unit: bit/s &lt;br&gt;Default value: 115200

**Type:** number

**Default:** 115200

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-baudRate?: int--><!--Device-SerialConfigs-baudRate?: int-End-->

**System capability:** SystemCapability.BusManager.Serial

## dataBits

```TypeScript
dataBits?: DataBits
```

Data bits. &lt;br&gt;Default value: EIGHT

**Type:** DataBits

**Default:** EIGHT

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-dataBits?: DataBits--><!--Device-SerialConfigs-dataBits?: DataBits-End-->

**System capability:** SystemCapability.BusManager.Serial

## parity

```TypeScript
parity?: Parity
```

Parity bit. &lt;br&gt;Default value: NONE

**Type:** Parity

**Default:** NONE

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-parity?: Parity--><!--Device-SerialConfigs-parity?: Parity-End-->

**System capability:** SystemCapability.BusManager.Serial

## rtscts

```TypeScript
rtscts?: boolean
```

Whether to enable hardware-based automatic flow control. &lt;br&gt;Default value: false.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-rtscts?: boolean--><!--Device-SerialConfigs-rtscts?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

## stopBits

```TypeScript
stopBits?: StopBits
```

Stop bits. Default value: ONE

**Type:** StopBits

**Default:** ONE

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-stopBits?: StopBits--><!--Device-SerialConfigs-stopBits?: StopBits-End-->

**System capability:** SystemCapability.BusManager.Serial

## xany

```TypeScript
xany?: boolean
```

Whether to enable XANY to control the flow. &lt;br&gt;Default value: false

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-xany?: boolean--><!--Device-SerialConfigs-xany?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

## xoff

```TypeScript
xoff?: boolean
```

Whether to enable XOFF to control the reception of flows. &lt;br&gt;Default value: false

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-xoff?: boolean--><!--Device-SerialConfigs-xoff?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

## xon

```TypeScript
xon?: boolean
```

Whether to enable XON to control the sending of flows. &lt;br&gt;Default value: false

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-xon?: boolean--><!--Device-SerialConfigs-xon?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial
