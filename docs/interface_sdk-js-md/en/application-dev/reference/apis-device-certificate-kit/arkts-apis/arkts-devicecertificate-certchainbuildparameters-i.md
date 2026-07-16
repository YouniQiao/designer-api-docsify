# CertChainBuildParameters

Represents the parameters for building a certificate chain.

**Since:** 12

<!--Device-cert-interface CertChainBuildParameters--><!--Device-cert-interface CertChainBuildParameters-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## certMatchParameters

```TypeScript
certMatchParameters: X509CertMatchParameters
```

Filter criteria.

**Type:** X509CertMatchParameters

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainBuildParameters-certMatchParameters: X509CertMatchParameters--><!--Device-CertChainBuildParameters-certMatchParameters: X509CertMatchParameters-End-->

**System capability:** SystemCapability.Security.Cert

## maxLength

```TypeScript
maxLength?: number
```

Maximum number of CA certificates in the certificate chain.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainBuildParameters-maxLength?: int--><!--Device-CertChainBuildParameters-maxLength?: int-End-->

**System capability:** SystemCapability.Security.Cert

## validationParameters

```TypeScript
validationParameters: CertChainValidationParameters
```

Parameters for certificate chain validation.

**Type:** CertChainValidationParameters

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainBuildParameters-validationParameters: CertChainValidationParameters--><!--Device-CertChainBuildParameters-validationParameters: CertChainValidationParameters-End-->

**System capability:** SystemCapability.Security.Cert

