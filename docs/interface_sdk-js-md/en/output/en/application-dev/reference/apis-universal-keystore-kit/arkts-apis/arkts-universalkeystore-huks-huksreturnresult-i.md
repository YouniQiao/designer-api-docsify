# HuksReturnResult

Represents the result returned.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-huks-export interface HuksReturnResult--><!--Device-huks-export interface HuksReturnResult-End-->

**System capability:** SystemCapability.Security.Huks.Core

## certChains

```TypeScript
certChains?: Array<string>
```

Certificate chain information. The default value is **undefined**.

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HuksReturnResult-certChains?: Array<string>--><!--Device-HuksReturnResult-certChains?: Array<string>-End-->

**System capability:** SystemCapability.Security.Huks.Core

## outData

```TypeScript
outData?: Uint8Array
```

Challenge obtained after the [initSession]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ operation. The default value is **undefined**.

**Type:** Uint8Array

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksReturnResult-outData?: Uint8Array--><!--Device-HuksReturnResult-outData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Core

## properties

```TypeScript
properties?: Array<HuksParam>
```

Challenge obtained after the [initSession]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ operation. The default value is **undefined**.

**Type:** Array&lt;HuksParam&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksReturnResult-properties?: Array<HuksParam>--><!--Device-HuksReturnResult-properties?: Array<HuksParam>-End-->

**System capability:** SystemCapability.Security.Huks.Core

## sharedSecret

```TypeScript
sharedSecret?: Uint8Array
```

Shared key.

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HuksReturnResult-sharedSecret?: Uint8Array--><!--Device-HuksReturnResult-sharedSecret?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Core

