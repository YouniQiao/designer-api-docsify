# SerialConfigs

串口通信配置

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-serial-interface SerialConfigs--><!--Device-serial-interface SerialConfigs-End-->

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## baudRate

```TypeScript
baudRate?: int
```

波特率取值限定为整数。取值约束:标准波特率。&lt;br&gt;单位:bps。&lt;br&gt;默认值:115200。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 115200

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-baudRate?: int--><!--Device-SerialConfigs-baudRate?: int-End-->

**System capability:** SystemCapability.BusManager.Serial

## dataBits

```TypeScript
dataBits?: DataBits
```

数据位&lt;br&gt;默认值:EIGHT。

**Type:** [DataBits](arkts-basicservices-serial-databits-e.md)

**Default:** EIGHT

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-dataBits?: DataBits--><!--Device-SerialConfigs-dataBits?: DataBits-End-->

**System capability:** SystemCapability.BusManager.Serial

## parity

```TypeScript
parity?: Parity
```

校验位&lt;br&gt;默认值:NONE。

**Type:** [Parity](arkts-basicservices-serialmanager-parity-e.md)

**Default:** NONE

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-parity?: Parity--><!--Device-SerialConfigs-parity?: Parity-End-->

**System capability:** SystemCapability.BusManager.Serial

## rtscts

```TypeScript
rtscts?: boolean
```

是否开启硬件自动流控&lt;br&gt;默认值:false。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-rtscts?: boolean--><!--Device-SerialConfigs-rtscts?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

## stopBits

```TypeScript
stopBits?: StopBits
```

停止位

&lt;br&gt;默认值:ONE。

**Type:** [StopBits](arkts-basicservices-serial-stopbits-e.md)

**Default:** ONE

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-stopBits?: StopBits--><!--Device-SerialConfigs-stopBits?: StopBits-End-->

**System capability:** SystemCapability.BusManager.Serial

## xany

```TypeScript
xany?: boolean
```

是否启用XANY软件流控&lt;br&gt;默认值:false。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-xany?: boolean--><!--Device-SerialConfigs-xany?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

## xoff

```TypeScript
xoff?: boolean
```

是否启用XOFF软件流控接收&lt;br&gt;默认值:false。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-xoff?: boolean--><!--Device-SerialConfigs-xoff?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

## xon

```TypeScript
xon?: boolean
```

是否启用XON软件流控发送&lt;br&gt;默认值:false。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialConfigs-xon?: boolean--><!--Device-SerialConfigs-xon?: boolean-End-->

**System capability:** SystemCapability.BusManager.Serial

