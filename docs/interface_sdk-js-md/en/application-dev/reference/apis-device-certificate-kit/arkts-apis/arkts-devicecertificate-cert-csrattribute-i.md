# CsrAttribute

定义CSR属性表示。

&lt;br&gt;CSR属性字段，当前仅支持字符串类型的属性字段，属性值添加到CSR中编码为utf-8。常见的type为challengePassword。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cert-interface CsrAttribute--><!--Device-cert-interface CsrAttribute-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## type

```TypeScript
type: string
```

PKCS #9指定的扩展类型。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CsrAttribute-type: string--><!--Device-CsrAttribute-type: string-End-->

**System capability:** SystemCapability.Security.Cert

## value

```TypeScript
value: string
```

属性值。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CsrAttribute-value: string--><!--Device-CsrAttribute-value: string-End-->

**System capability:** SystemCapability.Security.Cert

