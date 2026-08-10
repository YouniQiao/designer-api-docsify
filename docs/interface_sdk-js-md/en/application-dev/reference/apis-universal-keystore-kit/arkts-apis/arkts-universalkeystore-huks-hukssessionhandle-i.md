# HuksSessionHandle

HUKS handle结构体。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-huks-export interface HuksSessionHandle--><!--Device-huks-export interface HuksSessionHandle-End-->

**System capability:** SystemCapability.Security.Huks.Core

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## challenge

```TypeScript
challenge?: Uint8Array
```

表示  
[initSession](arkts-universalkeystore-huks-initsession-f.md#initsession)操作之后获取到的challenge信息。默认为undefined。

**Type:** Uint8Array

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksSessionHandle-challenge?: Uint8Array--><!--Device-HuksSessionHandle-challenge?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Core

## handle

```TypeScript
handle: number
```

表示无符号整数类型的handle值。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksSessionHandle-handle: number--><!--Device-HuksSessionHandle-handle: number-End-->

**System capability:** SystemCapability.Security.Huks.Core

