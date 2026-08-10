# HuksResult

调用接口返回的result。

> **说明：**
> 
> - 从API version 8开始，从API version 9开始废弃，建议使用[HuksReturnResult&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-huksreturnresult-i.md)替代。
> 
> - errorCode的具体信息，请参考[HUKS错误码](../../../reference/apis-universal-keystore-kit/errorcode-huks.md)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)

<!--Device-huks-export interface HuksResult--><!--Device-huks-export interface HuksResult-End-->

**System capability:** SystemCapability.Security.Huks.Extension

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## certChains

```TypeScript
certChains?: Array<string>
```

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**Type:** Array&lt;string&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-HuksResult-certChains?: Array<string>--><!--Device-HuksResult-certChains?: Array<string>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

## errorCode

```TypeScript
errorCode: number
```

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-HuksResult-errorCode: number--><!--Device-HuksResult-errorCode: number-End-->

**System capability:** SystemCapability.Security.Huks.Extension

## outData

```TypeScript
outData?: Uint8Array
```

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**Type:** Uint8Array

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-HuksResult-outData?: Uint8Array--><!--Device-HuksResult-outData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Extension

## properties

```TypeScript
properties?: Array<HuksParam>
```

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**Type:** Array&lt;HuksParam&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-HuksResult-properties?: Array<HuksParam>--><!--Device-HuksResult-properties?: Array<HuksParam>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

