# LteCellInformation (System API)

Obtains LTE cell information.

@interface LteCellInformation

**Since:** 23

<!--Device-radio-export interface LteCellInformation--><!--Device-radio-export interface LteCellInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## bandwidth

```TypeScript
bandwidth: int
```

Indicates the bandwidth.

**Type:** int

**Since:** 23

<!--Device-LteCellInformation-bandwidth: int--><!--Device-LteCellInformation-bandwidth: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## cgi

```TypeScript
cgi: long
```

Indicates the cell global identification.

**Type:** long

**Since:** 23

<!--Device-LteCellInformation-cgi: long--><!--Device-LteCellInformation-cgi: long-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## earfcn

```TypeScript
earfcn: int
```

Indicates the E-UTRA Absolute Radio Frequency Channel Number.

**Type:** int

**Since:** 23

<!--Device-LteCellInformation-earfcn: int--><!--Device-LteCellInformation-earfcn: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## isSupportEndc

```TypeScript
isSupportEndc: boolean
```

Support for New Radio_Dual Connectivity.

**Type:** boolean

**Since:** 23

<!--Device-LteCellInformation-isSupportEndc: boolean--><!--Device-LteCellInformation-isSupportEndc: boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## mcc

```TypeScript
mcc: string
```

Indicates the mobile country code.

**Type:** string

**Since:** 23

<!--Device-LteCellInformation-mcc: string--><!--Device-LteCellInformation-mcc: string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## mnc

```TypeScript
mnc: string
```

Indicates the mobile network code.

**Type:** string

**Since:** 23

<!--Device-LteCellInformation-mnc: string--><!--Device-LteCellInformation-mnc: string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## pci

```TypeScript
pci: int
```

Indicates the physical cell identification.

**Type:** int

**Since:** 23

<!--Device-LteCellInformation-pci: int--><!--Device-LteCellInformation-pci: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## tac

```TypeScript
tac: int
```

Indicates the tracking area code.

**Type:** int

**Since:** 23

<!--Device-LteCellInformation-tac: int--><!--Device-LteCellInformation-tac: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

