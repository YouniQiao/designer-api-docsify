# HuksCryptoExtensionCertInfo

[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresultcode-e.md)中的certs数组中的元素。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-export interface HuksCryptoExtensionCertInfo--><!--Device-unnamed-export interface HuksCryptoExtensionCertInfo-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

## Modules to Import

```TypeScript
import { HuksCryptoExtensionCertInfo, HuksCryptoExtensionResultCode, HuksCryptoExtensionParams, HuksCryptoExtensionParam, HuksCryptoExtensionResult } from 'kits/@kit.UniversalKeystoreKit';
```

## cert

```TypeScript
cert: Uint8Array
```

证书。

**Type:** Uint8Array

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-HuksCryptoExtensionCertInfo-cert: Uint8Array--><!--Device-HuksCryptoExtensionCertInfo-cert: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

## purpose

```TypeScript
purpose: certificateManager.CertificatePurpose
```

表示证书链对应密钥的使用类型。

**Type:** certificateManager.CertificatePurpose

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-HuksCryptoExtensionCertInfo-purpose: certificateManager.CertificatePurpose--><!--Device-HuksCryptoExtensionCertInfo-purpose: certificateManager.CertificatePurpose-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

## resourceId

```TypeScript
resourceId: string
```

资源ID。JSON格式，能够映射到Ukey中的某个资源。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-HuksCryptoExtensionCertInfo-resourceId: string--><!--Device-HuksCryptoExtensionCertInfo-resourceId: string-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

