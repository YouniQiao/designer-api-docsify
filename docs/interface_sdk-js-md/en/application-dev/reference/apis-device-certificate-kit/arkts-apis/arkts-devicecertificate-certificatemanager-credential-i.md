# Credential

表示凭据详细信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-certificateManager-export interface Credential--><!--Device-certificateManager-export interface Credential-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## alias

```TypeScript
alias: string
```

表示凭据的别名，最大长度为128字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Credential-alias: string--><!--Device-Credential-alias: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certNum

```TypeScript
certNum: int
```

表示凭据中包含的证书个数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Credential-certNum: int--><!--Device-Credential-certNum: int-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certPurpose

```TypeScript
certPurpose?: CertificatePurpose
```

表示凭据的用途。默认值为CertificatePurpose.PURPOSE_DEFAULT。

**Type:** [CertificatePurpose](arkts-devicecertificate-certificatemanager-certificatepurpose-e.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-Credential-certPurpose?: CertificatePurpose--><!--Device-Credential-certPurpose?: CertificatePurpose-End-->

**System capability:** SystemCapability.Security.CertificateManager

## credentialData

```TypeScript
credentialData: Uint8Array
```

表示凭据二进制数据，最大长度为20480字节。

**Type:** Uint8Array

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Credential-credentialData: Uint8Array--><!--Device-Credential-credentialData: Uint8Array-End-->

**System capability:** SystemCapability.Security.CertificateManager

## keyNum

```TypeScript
keyNum: int
```

表示凭据中包含的密钥个数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Credential-keyNum: int--><!--Device-Credential-keyNum: int-End-->

**System capability:** SystemCapability.Security.CertificateManager

## keyUri

```TypeScript
keyUri: string
```

表示凭据的唯一标识符，最大长度为256字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Credential-keyUri: string--><!--Device-Credential-keyUri: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

## type

```TypeScript
type: string
```

表示凭据的类型，最大长度为8字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Credential-type: string--><!--Device-Credential-type: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

