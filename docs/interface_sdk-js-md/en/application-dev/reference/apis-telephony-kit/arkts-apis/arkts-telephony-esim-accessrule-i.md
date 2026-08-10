# AccessRule

Establishes a single UICC access rule pursuant to the GlobalPlatform Secure Element Access Control specification.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-eSIM-export interface AccessRule--><!--Device-eSIM-export interface AccessRule-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## accessType

```TypeScript
accessType: int
```

The type of access.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AccessRule-accessType: int--><!--Device-AccessRule-accessType: int-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

## certificateHashHexStr

```TypeScript
certificateHashHexStr: string
```

Certificate hash hexadecimal string.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AccessRule-certificateHashHexStr: string--><!--Device-AccessRule-certificateHashHexStr: string-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

## packageName

```TypeScript
packageName: string
```

The name of package.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AccessRule-packageName: string--><!--Device-AccessRule-packageName: string-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

