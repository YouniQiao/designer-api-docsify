# HuksSessionHandle

Defines the struct for a HUKS handle.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-huks-export interface HuksSessionHandle--><!--Device-huks-export interface HuksSessionHandle-End-->

**System capability:** SystemCapability.Security.Huks.Core

## challenge

```TypeScript
challenge?: Uint8Array
```

Challenge obtained after the  
[initSession]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_operation. The default value is **undefined**.

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

Handle of the unsigned integer type.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksSessionHandle-handle: number--><!--Device-HuksSessionHandle-handle: number-End-->

**System capability:** SystemCapability.Security.Huks.Core

