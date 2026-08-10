# CertChainValidationResult

表示证书链校验的返回值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface CertChainValidationResult--><!--Device-cert-interface CertChainValidationResult-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## entityCert

```TypeScript
readonly entityCert: X509Cert
```

表示实体证书。

**Type:** [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationResult-readonly entityCert: X509Cert--><!--Device-CertChainValidationResult-readonly entityCert: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

## trustAnchor

```TypeScript
readonly trustAnchor: X509TrustAnchor
```

表示信任锚。

**Type:** [X509TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationResult-readonly trustAnchor: X509TrustAnchor--><!--Device-CertChainValidationResult-readonly trustAnchor: X509TrustAnchor-End-->

**System capability:** SystemCapability.Security.Cert

