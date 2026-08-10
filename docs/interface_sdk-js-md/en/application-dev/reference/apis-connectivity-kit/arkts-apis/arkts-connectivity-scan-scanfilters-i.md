# ScanFilters

扫描过滤器。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-scan-interface ScanFilters--><!--Device-scan-interface ScanFilters-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address?: string
```

设备地址。长度必须为17，由16进制数字和冒号组成，形如 "11:22:33:AA:BB:FF"。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilters-address?: string--><!--Device-ScanFilters-address?: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## deviceName

```TypeScript
deviceName?: string
```

设备名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilters-deviceName?: string--><!--Device-ScanFilters-deviceName?: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## manufacturerData

```TypeScript
manufacturerData?: ArrayBuffer
```

制造商数据。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilters-manufacturerData?: ArrayBuffer--><!--Device-ScanFilters-manufacturerData?: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## manufacturerDataMask

```TypeScript
manufacturerDataMask?: ArrayBuffer
```

制造商数据掩码。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilters-manufacturerDataMask?: ArrayBuffer--><!--Device-ScanFilters-manufacturerDataMask?: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## manufacturerId

```TypeScript
manufacturerId?: int
```

厂商ID。取值范围为全体整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilters-manufacturerId?: int--><!--Device-ScanFilters-manufacturerId?: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## rssi

```TypeScript
rssi?: int
```

接收信号强度指示。单位为： 分贝毫瓦，取值应为[-128,127]内的整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilters-rssi?: int--><!--Device-ScanFilters-rssi?: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

