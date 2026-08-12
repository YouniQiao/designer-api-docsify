# DeflatePendingOutputInfo

DeflatePending return value information.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface DeflatePendingOutputInfo--><!--Device-zlib-interface DeflatePendingOutputInfo-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## bits

```TypeScript
bits: int
```

Number of output bits that have been generated.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeflatePendingOutputInfo-bits: int--><!--Device-DeflatePendingOutputInfo-bits: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## pending

```TypeScript
pending: int
```

Number of output bytes that have been generated.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeflatePendingOutputInfo-pending: int--><!--Device-DeflatePendingOutputInfo-pending: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## status

```TypeScript
status: ReturnStatus
```

For details, see [ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md#ReturnStatus).

**Type:** [ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeflatePendingOutputInfo-status: ReturnStatus--><!--Device-DeflatePendingOutputInfo-status: ReturnStatus-End-->

**System capability:** SystemCapability.BundleManager.Zlib

