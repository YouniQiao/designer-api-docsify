# SerialPortInfo

串口设备信息

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-serial-interface SerialPortInfo--><!--Device-serial-interface SerialPortInfo-End-->

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## manufacturer

```TypeScript
manufacturer?: string
```

USB虚拟串口设备的制造商名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPortInfo-manufacturer?: string--><!--Device-SerialPortInfo-manufacturer?: string-End-->

**System capability:** SystemCapability.BusManager.Serial

## portName

```TypeScript
portName: string
```

端口名称

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPortInfo-portName: string--><!--Device-SerialPortInfo-portName: string-End-->

**System capability:** SystemCapability.BusManager.Serial

## productId

```TypeScript
productId?: int
```

USB虚拟串口设备的productId

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPortInfo-productId?: int--><!--Device-SerialPortInfo-productId?: int-End-->

**System capability:** SystemCapability.BusManager.Serial

## vendorId

```TypeScript
vendorId?: int
```

USB虚拟串口的vendorId

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPortInfo-vendorId?: int--><!--Device-SerialPortInfo-vendorId?: int-End-->

**System capability:** SystemCapability.BusManager.Serial

