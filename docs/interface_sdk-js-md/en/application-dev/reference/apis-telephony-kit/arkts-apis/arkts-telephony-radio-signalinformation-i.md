# SignalInformation

Returns child class objects specific to the network type.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-radio-export interface SignalInformation--><!--Device-radio-export interface SignalInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## dBm

```TypeScript
dBm: int
```

rsrp for LTE and NR; dbm for CDMA and EVDO; rscp for WCDMA; rssi for GSM.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SignalInformation-dBm: int--><!--Device-SignalInformation-dBm: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalLevel

```TypeScript
signalLevel: int
```

Obtains the signal level of the current network.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-SignalInformation-signalLevel: int--><!--Device-SignalInformation-signalLevel: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalType

```TypeScript
signalType: NetworkType
```

Obtains the network type corresponding to the signal.

**Type:** NetworkType

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-SignalInformation-signalType: NetworkType--><!--Device-SignalInformation-signalType: NetworkType-End-->

**System capability:** SystemCapability.Telephony.CoreService

