# DecompressionOutputInfo

Uncompress2 return value information.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface DecompressionOutputInfo--><!--Device-zlib-interface DecompressionOutputInfo-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## destLength

```TypeScript
destLength: long
```

Total length of the destination buffer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecompressionOutputInfo-destLength: long--><!--Device-DecompressionOutputInfo-destLength: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## sourceLength

```TypeScript
sourceLength: long
```

Length of the source buffer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecompressionOutputInfo-sourceLength: long--><!--Device-DecompressionOutputInfo-sourceLength: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## status

```TypeScript
status: ReturnStatus
```

For details, see [ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md).

**Type:** [ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecompressionOutputInfo-status: ReturnStatus--><!--Device-DecompressionOutputInfo-status: ReturnStatus-End-->

**System capability:** SystemCapability.BundleManager.Zlib

