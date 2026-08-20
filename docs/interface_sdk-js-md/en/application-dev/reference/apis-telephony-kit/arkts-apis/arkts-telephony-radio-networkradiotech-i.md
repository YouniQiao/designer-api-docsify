# NetworkRadioTech

Describes the radio access technology (RAT) of registered network.

@interface NetworkRadioTech

**Since:** 23

<!--Device-radio-export interface NetworkRadioTech--><!--Device-radio-export interface NetworkRadioTech-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## csRadioTech

```TypeScript
csRadioTech: RadioTechnology
```

Indicates radio access technology (RAT) of circuit service (CS) domain.

**Type:** [RadioTechnology](arkts-telephony-radio-radiotechnology-e.md)

**Since:** 23

<!--Device-NetworkRadioTech-csRadioTech: RadioTechnology--><!--Device-NetworkRadioTech-csRadioTech: RadioTechnology-End-->

**System capability:** SystemCapability.Telephony.CoreService

## psRadioTech

```TypeScript
psRadioTech: RadioTechnology
```

Indicates radio access technology (RAT) of packet service (PS) domain.

**Type:** [RadioTechnology](arkts-telephony-radio-radiotechnology-e.md)

**Since:** 23

<!--Device-NetworkRadioTech-psRadioTech: RadioTechnology--><!--Device-NetworkRadioTech-psRadioTech: RadioTechnology-End-->

**System capability:** SystemCapability.Telephony.CoreService

