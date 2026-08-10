# SppOptions

Describes the spp parameters.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-socket-interface SppOptions--><!--Device-socket-interface SppOptions-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## psm

```TypeScript
psm?: int
```

l2cap protocol service multiplexer

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

<!--Device-SppOptions-psm?: int--><!--Device-SppOptions-psm?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## secure

```TypeScript
secure: boolean
```

Indicates secure channel or not

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-SppOptions-secure: boolean--><!--Device-SppOptions-secure: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## type

```TypeScript
type: SppType
```

Spp link type

**类型：** [SppType](arkts-connectivity-socket-spptype-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-SppOptions-type: SppType--><!--Device-SppOptions-type: SppType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## uuid

```TypeScript
uuid: string
```

Indicates the UUID in the SDP record.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-SppOptions-uuid: string--><!--Device-SppOptions-uuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

