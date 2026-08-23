# SignalInformation

Defines the signal strength.

**Since:** 23

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

Signal strength. The value range is [–140, 140]. If the value is out of range, an error is returned.

**Type:** int

**Since:** 23

<!--Device-SignalInformation-dBm: int--><!--Device-SignalInformation-dBm: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalLevel

```TypeScript
signalLevel: int
```

Signal strength level. The value range is [0, 5]. If the value is out of range, an error is returned.

**Type:** int

**Since:** 23

<!--Device-SignalInformation-signalLevel: int--><!--Device-SignalInformation-signalLevel: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalType

```TypeScript
signalType: NetworkType
```

Signal strength type.

**Type:** NetworkType

**Since:** 23

<!--Device-SignalInformation-signalType: NetworkType--><!--Device-SignalInformation-signalType: NetworkType-End-->

**System capability:** SystemCapability.Telephony.CoreService

