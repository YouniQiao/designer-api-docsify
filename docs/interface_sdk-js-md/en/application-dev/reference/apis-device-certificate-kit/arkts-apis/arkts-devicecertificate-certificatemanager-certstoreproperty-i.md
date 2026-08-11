# CertStoreProperty

Represents the storage information about a certificate, including the certificate type and location.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-certificateManager-export interface CertStoreProperty--><!--Device-certificateManager-export interface CertStoreProperty-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## certAlg

```TypeScript
certAlg?: CertAlgorithm
```

Certificate algorithm. This parameter is valid only when **certType** is set to **CA_CERT_SYSTEM**. The default value is **INTERNATIONAL**.Devices outside China do not support the SM algorithm.

**Type:** [CertAlgorithm](arkts-devicecertificate-certificatemanager-certalgorithm-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CertStoreProperty-certAlg?: CertAlgorithm--><!--Device-CertStoreProperty-certAlg?: CertAlgorithm-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certScope

```TypeScript
certScope?: CertScope
```

Scope of the certificate. This parameter is mandatory when **certType** is **CA_CERT_USER**.

**Type:** [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CertStoreProperty-certScope?: CertScope--><!--Device-CertStoreProperty-certScope?: CertScope-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certType

```TypeScript
certType: CertType
```

Type of the certificate.

**Type:** [CertType](../../apis-network-kit/arkts-apis/arkts-network-http-certtype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CertStoreProperty-certType: CertType--><!--Device-CertStoreProperty-certType: CertType-End-->

**System capability:** SystemCapability.Security.CertificateManager

