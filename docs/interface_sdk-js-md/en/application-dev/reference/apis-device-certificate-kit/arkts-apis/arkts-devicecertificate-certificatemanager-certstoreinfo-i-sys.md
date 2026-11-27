# CertStoreInfo (System API)

```TypeScript
export interface CertStoreInfo
```

Represents the certificate store information.

**Since:** 26.1.0

<!--Device-certificateManager-export interface CertStoreInfo--><!--Device-certificateManager-export interface CertStoreInfo-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## certStoreVersion

```TypeScript
certStoreVersion: string
```

Version number of the international algorithm system certificate store.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertStoreInfo-certStoreVersion: string--><!--Device-CertStoreInfo-certStoreVersion: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

## smCertStoreVersion

```TypeScript
smCertStoreVersion?: string
```

Version number of the SM (commercial cryptographic) algorithm system certificate store.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertStoreInfo-smCertStoreVersion?: string--><!--Device-CertStoreInfo-smCertStoreVersion?: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.
