# NetworkState

Describes the network registration state.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-radio-export interface NetworkState--><!--Device-radio-export interface NetworkState-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## cfgTech

```TypeScript
cfgTech: RadioTechnology
```

Obtains the radio Access technology after config conversion.

**类型：** [RadioTechnology](arkts-telephony-radio-radiotechnology-e.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-cfgTech: RadioTechnology--><!--Device-NetworkState-cfgTech: RadioTechnology-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## isCaActive

```TypeScript
isCaActive: boolean
```

Obtains the status of CA.

Returns {@code true} if CA is actived; returns {@code false} otherwise.

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-isCaActive: boolean--><!--Device-NetworkState-isCaActive: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## isEmergency

```TypeScript
isEmergency: boolean
```

Checks whether this device is allowed to make emergency calls only.

Returns {@code true} if this device is allowed to make emergency calls only;returns {@code false} otherwise.

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-isEmergency: boolean--><!--Device-NetworkState-isEmergency: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## isRoaming

```TypeScript
isRoaming: boolean
```

Checks whether the device is roaming.

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-isRoaming: boolean--><!--Device-NetworkState-isRoaming: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## longOperatorName

```TypeScript
longOperatorName: string
```

Obtains the operator name in the long alphanumeric format of the registered network.

Returns the operator name in the long alphanumeric format as a string;returns an empty string if no operator name is obtained.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-longOperatorName: string--><!--Device-NetworkState-longOperatorName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## nsaState

```TypeScript
nsaState: NsaState
```

Obtains the NSA network registration status of the device.

Returns the NSA network registration status {@code NsaState}.

**类型：** [NsaState](arkts-telephony-radio-nsastate-e.md)

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-nsaState: NsaState--><!--Device-NetworkState-nsaState: NsaState-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## plmnNumeric

```TypeScript
plmnNumeric: string
```

Obtains the PLMN code of the registered network.

Returns the PLMN code as a string; returns an empty string if no operator name is obtained.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-plmnNumeric: string--><!--Device-NetworkState-plmnNumeric: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## regState

```TypeScript
regState: RegState
```

Obtains the network registration status of the device.

**类型：** [RegState](arkts-telephony-radio-regstate-e.md)

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-regState: RegState--><!--Device-NetworkState-regState: RegState-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## shortOperatorName

```TypeScript
shortOperatorName: string
```

Obtains the operator name in the short alphanumeric format of the registered network.

Returns the operator name in the short alphanumeric format as a string;returns an empty string if no operator name is obtained.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-NetworkState-shortOperatorName: string--><!--Device-NetworkState-shortOperatorName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

