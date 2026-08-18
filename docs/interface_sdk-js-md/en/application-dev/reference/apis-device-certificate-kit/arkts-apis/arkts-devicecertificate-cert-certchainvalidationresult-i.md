# CertChainValidationResult

Represents the return value of certificate chain validation.

**Since:** 23

<!--Device-cert-interface CertChainValidationResult--><!--Device-cert-interface CertChainValidationResult-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

## entityCert

```TypeScript
readonly entityCert: X509Cert
```

Entity certificate.

**Type:** X509Cert

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationResult-readonly entityCert: X509Cert--><!--Device-CertChainValidationResult-readonly entityCert: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

## trustAnchor

```TypeScript
readonly trustAnchor: X509TrustAnchor
```

Trust anchor.

**Type:** [X509TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationResult-readonly trustAnchor: X509TrustAnchor--><!--Device-CertChainValidationResult-readonly trustAnchor: X509TrustAnchor-End-->

**System capability:** SystemCapability.Security.Cert

