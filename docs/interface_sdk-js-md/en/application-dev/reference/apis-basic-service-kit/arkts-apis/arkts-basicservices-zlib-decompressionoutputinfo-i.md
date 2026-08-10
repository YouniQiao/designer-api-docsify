# DecompressionOutputInfo

解压缩返回信息。

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

目标缓冲区的总长度。

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

源缓冲区的长度。

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

参考[ReturnStatus枚举定义](arkts-basicservices-zlib-returnstatus-e.md)。

**Type:** [ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecompressionOutputInfo-status: ReturnStatus--><!--Device-DecompressionOutputInfo-status: ReturnStatus-End-->

**System capability:** SystemCapability.BundleManager.Zlib

