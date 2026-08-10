# CMSignatureSpec

表示签名、验签操作使用的参数集合，包括密钥使用目的、填充方式和摘要算法。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-certificateManager-export interface CMSignatureSpec--><!--Device-certificateManager-export interface CMSignatureSpec-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## digest

```TypeScript
digest?: CmKeyDigest
```

表示摘要算法的枚举。默认值： CM_DIGEST_SHA256，表示使用SHA256摘要算法。

**Type:** [CmKeyDigest](arkts-devicecertificate-certificatemanager-cmkeydigest-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMSignatureSpec-digest?: CmKeyDigest--><!--Device-CMSignatureSpec-digest?: CmKeyDigest-End-->

**System capability:** SystemCapability.Security.CertificateManager

## padding

```TypeScript
padding?: CmKeyPadding
```

表示填充方式的枚举默认值： CM_PADDING_PSS，表示使用PSS填充方式。

**Type:** [CmKeyPadding](arkts-devicecertificate-certificatemanager-cmkeypadding-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMSignatureSpec-padding?: CmKeyPadding--><!--Device-CMSignatureSpec-padding?: CmKeyPadding-End-->

**System capability:** SystemCapability.Security.CertificateManager

## purpose

```TypeScript
purpose: CmKeyPurpose
```

表示密钥使用目的的枚举。

**Type:** [CmKeyPurpose](arkts-devicecertificate-certificatemanager-cmkeypurpose-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMSignatureSpec-purpose: CmKeyPurpose--><!--Device-CMSignatureSpec-purpose: CmKeyPurpose-End-->

**System capability:** SystemCapability.Security.CertificateManager

