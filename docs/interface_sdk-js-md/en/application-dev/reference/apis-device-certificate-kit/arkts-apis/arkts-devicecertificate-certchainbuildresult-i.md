# CertChainBuildResult

Represents the certificate chain build result.

**Since:** 12

<!--Device-cert-interface CertChainBuildResult--><!--Device-cert-interface CertChainBuildResult-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## certChain

```TypeScript
readonly certChain: X509CertChain
```

Certificate chain object created.

**Type:** X509CertChain

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainBuildResult-readonly certChain: X509CertChain--><!--Device-CertChainBuildResult-readonly certChain: X509CertChain-End-->

**System capability:** SystemCapability.Security.Cert

## validationResult

```TypeScript
readonly validationResult: CertChainValidationResult
```

Result of the certificate chain validation.

**Type:** CertChainValidationResult

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainBuildResult-readonly validationResult: CertChainValidationResult--><!--Device-CertChainBuildResult-readonly validationResult: CertChainValidationResult-End-->

**System capability:** SystemCapability.Security.Cert

