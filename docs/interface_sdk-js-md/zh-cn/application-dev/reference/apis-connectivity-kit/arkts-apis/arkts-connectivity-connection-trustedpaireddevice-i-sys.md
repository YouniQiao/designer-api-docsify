# TrustedPairedDevice（系统接口）

Describes device of cloud pair.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-connection-interface TrustedPairedDevice--><!--Device-connection-interface TrustedPairedDevice-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## bluetoothClass

```TypeScript
bluetoothClass: int
```

Indicates the bluetoothClass of the peripheral.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-bluetoothClass: int--><!--Device-TrustedPairedDevice-bluetoothClass: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceName

```TypeScript
deviceName: string
```

The local name of the device

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-deviceName: string--><!--Device-TrustedPairedDevice-deviceName: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceNameTime

```TypeScript
deviceNameTime: long
```

Indicates the deviceNameTime of the peripheral.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-deviceNameTime: long--><!--Device-TrustedPairedDevice-deviceNameTime: long-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceType

```TypeScript
deviceType: string
```

Indicates the device type of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-deviceType: string--><!--Device-TrustedPairedDevice-deviceType: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## hiLinkVersion

```TypeScript
hiLinkVersion: string
```

Indicates the HiLink version of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-hiLinkVersion: string--><!--Device-TrustedPairedDevice-hiLinkVersion: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## macAddress

```TypeScript
macAddress: string
```

Indicates the macAddress of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-macAddress: string--><!--Device-TrustedPairedDevice-macAddress: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## manufactory

```TypeScript
manufactory: string
```

Indicates the manufactory of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-manufactory: string--><!--Device-TrustedPairedDevice-manufactory: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## modelId

```TypeScript
modelId: string
```

Indicates the modelId of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-modelId: string--><!--Device-TrustedPairedDevice-modelId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## pairState

```TypeScript
pairState: int
```

Indicates the pairState of the peripheral.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-pairState: int--><!--Device-TrustedPairedDevice-pairState: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## productId

```TypeScript
productId: string
```

Indicates the productId of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-productId: string--><!--Device-TrustedPairedDevice-productId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## secureAdvertisingInfo

```TypeScript
secureAdvertisingInfo: ArrayBuffer
```

Indicates the securityAdvInfo of the peripheral.

**类型：** ArrayBuffer

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-secureAdvertisingInfo: ArrayBuffer--><!--Device-TrustedPairedDevice-secureAdvertisingInfo: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## serviceId

```TypeScript
serviceId: string
```

Indicates the service id of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-serviceId: string--><!--Device-TrustedPairedDevice-serviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## serviceType

```TypeScript
serviceType: string
```

Indicates the service type of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-serviceType: string--><!--Device-TrustedPairedDevice-serviceType: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## sn

```TypeScript
sn: string
```

Indicates the device identify.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-sn: string--><!--Device-TrustedPairedDevice-sn: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## token

```TypeScript
token: ArrayBuffer
```

Indicates the token of the peripheral.

**类型：** ArrayBuffer

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-token: ArrayBuffer--><!--Device-TrustedPairedDevice-token: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## uuids

```TypeScript
uuids: string
```

Indicates the uuid of the peripheral.

**类型：** string

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrustedPairedDevice-uuids: string--><!--Device-TrustedPairedDevice-uuids: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

