# SignalInformation

Returns child class objects specific to the network type.

**Since:** 6

<!--Device-radio-export interface SignalInformation--><!--Device-radio-export interface SignalInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## dBm

```TypeScript
dBm: number
```

rsrp for LTE and NR; dbm for CDMA and EVDO; rscp for WCDMA; rssi for GSM.

**Type:** number

**Since:** 9

<!--Device-SignalInformation-dBm: int--><!--Device-SignalInformation-dBm: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalLevel

```TypeScript
signalLevel: number
```

Obtains the signal level of the current network.

**Type:** number

**Since:** 6

<!--Device-SignalInformation-signalLevel: int--><!--Device-SignalInformation-signalLevel: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalType

```TypeScript
signalType: NetworkType
```

Obtains the network type corresponding to the signal.

**Type:** NetworkType

**Since:** 6

<!--Device-SignalInformation-signalType: NetworkType--><!--Device-SignalInformation-signalType: NetworkType-End-->

**System capability:** SystemCapability.Telephony.CoreService

