# CellInformation

Obtains current cell information.

**Since:** 8

<!--Device-radio-export interface CellInformation--><!--Device-radio-export interface CellInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## networkType

```TypeScript
networkType: NetworkType
```

Obtains the network type of the serving cell.

An application can call this method to determine the network type that the child class uses.

**Type:** NetworkType

**Since:** 8

<!--Device-CellInformation-networkType: NetworkType--><!--Device-CellInformation-networkType: NetworkType-End-->

**System capability:** SystemCapability.Telephony.CoreService

## signalInformation

```TypeScript
signalInformation: SignalInformation
```

An abstract method of the parent class whose implementation depends on the child classes.Returned child class objects vary according to the network type.Returns child class objects specific to the network type.

**Type:** SignalInformation

**Since:** 8

<!--Device-CellInformation-signalInformation: SignalInformation--><!--Device-CellInformation-signalInformation: SignalInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

