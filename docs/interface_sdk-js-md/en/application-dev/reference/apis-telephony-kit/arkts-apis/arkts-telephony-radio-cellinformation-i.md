# CellInformation

Obtains current cell information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-radio-export interface CellInformation--><!--Device-radio-export interface CellInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## networkType

```TypeScript
networkType: NetworkType
```

Obtains the network type of the serving cell.

An application can call this method to determine the network type that the child class uses.

**Type:** [NetworkType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-workscheduler-networktype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-CellInformation-networkType: NetworkType--><!--Device-CellInformation-networkType: NetworkType-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalInformation

```TypeScript
signalInformation: SignalInformation
```

An abstract method of the parent class whose implementation depends on the child classes.Returned child class objects vary according to the network type.Returns child class objects specific to the network type.

**Type:** [SignalInformation](arkts-telephony-radio-signalinformation-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-CellInformation-signalInformation: SignalInformation--><!--Device-CellInformation-signalInformation: SignalInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

