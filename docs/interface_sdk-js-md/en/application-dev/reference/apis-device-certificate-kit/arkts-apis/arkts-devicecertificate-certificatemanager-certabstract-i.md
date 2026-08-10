# CertAbstract

表示证书简要信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-certificateManager-export interface CertAbstract--><!--Device-certificateManager-export interface CertAbstract-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## certAlias

```TypeScript
certAlias: string
```

表示证书的别名，最大长度为128字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CertAbstract-certAlias: string--><!--Device-CertAbstract-certAlias: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

## state

```TypeScript
state: boolean
```

表示证书的状态，true为启用状态、false为禁用状态。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CertAbstract-state: boolean--><!--Device-CertAbstract-state: boolean-End-->

**System capability:** SystemCapability.Security.CertificateManager

## subjectName

```TypeScript
subjectName: string
```

表示证书的使用者名称，最大长度为1024字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CertAbstract-subjectName: string--><!--Device-CertAbstract-subjectName: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

## uri

```TypeScript
uri: string
```

表示证书的唯一标识符，最大长度为256字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CertAbstract-uri: string--><!--Device-CertAbstract-uri: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

