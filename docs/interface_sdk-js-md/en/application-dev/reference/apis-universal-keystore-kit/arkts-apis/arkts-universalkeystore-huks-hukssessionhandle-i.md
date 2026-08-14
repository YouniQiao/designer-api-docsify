# HuksSessionHandle

Defines the struct for a HUKS handle.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-huks-export interface HuksSessionHandle--><!--Device-huks-export interface HuksSessionHandle-End-->

**System capability:** SystemCapability.Security.Huks.Core

## Modules to Import

```TypeScript
import { huks } from 'huks';
```

## challenge

```TypeScript
challenge?: Uint8Array
```

Challenge obtained after the [initSession](arkts-universalkeystore-huks-initsession-f.md#initSession) operation. The default value is **undefined**.

**Type:** Uint8Array

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksSessionHandle-challenge?: Uint8Array--><!--Device-HuksSessionHandle-challenge?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Core

## handle

```TypeScript
handle: number
```

Handle of the unsigned integer type.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksSessionHandle-handle: number--><!--Device-HuksSessionHandle-handle: number-End-->

**System capability:** SystemCapability.Security.Huks.Core

