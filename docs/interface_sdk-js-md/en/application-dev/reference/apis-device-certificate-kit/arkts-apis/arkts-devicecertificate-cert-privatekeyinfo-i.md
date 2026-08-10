# PrivateKeyInfo

表示私钥信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cert-interface PrivateKeyInfo--><!--Device-cert-interface PrivateKeyInfo-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## key

```TypeScript
key: string | Uint8Array
```

未加密或加密的私钥，支持PEM或DER格式。

**Type:** string \| Uint8Array

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PrivateKeyInfo-key: string | Uint8Array--><!--Device-PrivateKeyInfo-key: string | Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## password

```TypeScript
password?: string
```

私钥的密码，如果私钥是加密的。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PrivateKeyInfo-password?: string--><!--Device-PrivateKeyInfo-password?: string-End-->

**System capability:** SystemCapability.Security.Cert

