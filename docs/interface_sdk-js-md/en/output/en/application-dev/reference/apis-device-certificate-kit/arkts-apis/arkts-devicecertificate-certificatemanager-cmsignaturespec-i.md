# CMSignatureSpec

Represents a set of parameters used for signing or signature verification, including the key usage purpose, padding mode, and digest algorithm.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-certificateManager-export interface CMSignatureSpec--><!--Device-certificateManager-export interface CMSignatureSpec-End-->

**System capability:** SystemCapability.Security.CertificateManager

## digest

```TypeScript
digest?: CmKeyDigest
```

Digest algorithm. Default value: CM\_DIGEST\_SHA256: indicates that the SHA256 digest algorithm is used.

**Type:** CmKeyDigest

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMSignatureSpec-digest?: CmKeyDigest--><!--Device-CMSignatureSpec-digest?: CmKeyDigest-End-->

**System capability:** SystemCapability.Security.CertificateManager

## padding

```TypeScript
padding?: CmKeyPadding
```

Enumeration representing the padding mode. Default value: CM\_PADDING\_PSS: indicates that the PSS filling mode is used.

**Type:** CmKeyPadding

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMSignatureSpec-padding?: CmKeyPadding--><!--Device-CMSignatureSpec-padding?: CmKeyPadding-End-->

**System capability:** SystemCapability.Security.CertificateManager

## purpose

```TypeScript
purpose: CmKeyPurpose
```

Purpose of using the key.

**Type:** CmKeyPurpose

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMSignatureSpec-purpose: CmKeyPurpose--><!--Device-CMSignatureSpec-purpose: CmKeyPurpose-End-->

**System capability:** SystemCapability.Security.CertificateManager

