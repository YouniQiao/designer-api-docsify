# SignalInformation

Returns child class objects specific to the network type.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-radio-export interface SignalInformation--><!--Device-radio-export interface SignalInformation-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## dBm

```TypeScript
dBm: int
```

rsrp for LTE and NR; dbm for CDMA and EVDO; rscp for WCDMA; rssi for GSM.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SignalInformation-dBm: int--><!--Device-SignalInformation-dBm: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## signalLevel

```TypeScript
signalLevel: int
```

Obtains the signal level of the current network.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SignalInformation-signalLevel: int--><!--Device-SignalInformation-signalLevel: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## signalType

```TypeScript
signalType: NetworkType
```

Obtains the network type corresponding to the signal.

**类型：** [NetworkType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-workscheduler-networktype-e.md)

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SignalInformation-signalType: NetworkType--><!--Device-SignalInformation-signalType: NetworkType-End-->

**系统能力：** SystemCapability.Telephony.CoreService

