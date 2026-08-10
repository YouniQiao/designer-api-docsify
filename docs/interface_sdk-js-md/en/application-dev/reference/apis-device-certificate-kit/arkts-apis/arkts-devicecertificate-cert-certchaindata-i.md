# CertChainData

证书链数据，在证书链校验时，作为入参传入。

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

传入的数据中，包含的证书数量。

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

证书数据。

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

编码格式。

**Type:** [EncodingFormat](arkts-devicecertificate-cert-encodingformat-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainData-encodingFormat: EncodingFormat--><!--Device-CertChainData-encodingFormat: EncodingFormat-End-->

**System capability:** SystemCapability.Security.Cert

