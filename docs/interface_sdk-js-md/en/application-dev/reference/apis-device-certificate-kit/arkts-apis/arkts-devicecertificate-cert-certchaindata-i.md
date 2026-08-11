# CertChainData

Defines the certificate chain data, which is passed in as input parameters during certificate chain verification.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cert-interface CertChainData--><!--Device-cert-interface CertChainData-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## count

```TypeScript
count: int
```

Number of certificates contained in the input data.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainData-count: int--><!--Device-CertChainData-count: int-End-->

**System capability:** SystemCapability.Security.Cert

## data

```TypeScript
data: Uint8Array
```

Certificate data.

**Type:** Uint8Array

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainData-data: Uint8Array--><!--Device-CertChainData-data: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## encodingFormat

```TypeScript
encodingFormat: EncodingFormat
```

Certificate encoding format.

**Type:** [EncodingFormat](arkts-devicecertificate-cert-encodingformat-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainData-encodingFormat: EncodingFormat--><!--Device-CertChainData-encodingFormat: EncodingFormat-End-->

**System capability:** SystemCapability.Security.Cert

