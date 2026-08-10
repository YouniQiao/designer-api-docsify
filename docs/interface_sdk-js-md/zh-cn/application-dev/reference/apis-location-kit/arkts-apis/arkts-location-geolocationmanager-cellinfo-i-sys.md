# CellInfo（系统接口）

Cell information.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-geoLocationManager-export interface CellInfo--><!--Device-geoLocationManager-export interface CellInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## additionsMap

```TypeScript
additionsMap?: Map<string, string>
```

Indicates additional information map.

**类型：** Map&lt;string, string&gt;

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-additionsMap?: Map<string, string>--><!--Device-CellInfo-additionsMap?: Map<string, string>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## arfcn

```TypeScript
arfcn: int
```

Indicates absolute radio frequency channel number (ARFCN).The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-arfcn: int--><!--Device-CellInfo-arfcn: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## cellId

```TypeScript
cellId: long
```

Indicates ID of cell.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-cellId: long--><!--Device-CellInfo-cellId: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## lac

```TypeScript
lac: int
```

Indicates location area code(LAC).The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-lac: int--><!--Device-CellInfo-lac: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## mcc

```TypeScript
mcc: int
```

Indicates mobile country code (MCC).The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-mcc: int--><!--Device-CellInfo-mcc: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## mnc

```TypeScript
mnc: int
```

Indicates mobile network code (MNC).The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-mnc: int--><!--Device-CellInfo-mnc: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## pci

```TypeScript
pci: int
```

Indicates physical cell identifier (PCI).The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-pci: int--><!--Device-CellInfo-pci: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## rat

```TypeScript
rat: int
```

Indicates radio access technology (RAT).The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-rat: int--><!--Device-CellInfo-rat: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## signalIntensity

```TypeScript
signalIntensity: int
```

Indicates signal intensity.The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-signalIntensity: int--><!--Device-CellInfo-signalIntensity: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## tac

```TypeScript
tac?: int
```

Indicates tracking area code (TAC).The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-tac?: int--><!--Device-CellInfo-tac?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## timeSinceBoot

```TypeScript
timeSinceBoot: long
```

Indicates timestamp since boot.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CellInfo-timeSinceBoot: long--><!--Device-CellInfo-timeSinceBoot: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

