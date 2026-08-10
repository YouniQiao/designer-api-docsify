# CMResult

表示接口的返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-certificateManager-export interface CMResult--><!--Device-certificateManager-export interface CMResult-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## appUidList

```TypeScript
appUidList?: Array<string>
```

表示授权应用列表。

**Type:** Array&lt;string&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-appUidList?: Array<string>--><!--Device-CMResult-appUidList?: Array<string>-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certInfo

```TypeScript
certInfo?: CertInfo
```

表示证书详情。

**Type:** [CertInfo](arkts-devicecertificate-certificatemanager-certinfo-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-certInfo?: CertInfo--><!--Device-CMResult-certInfo?: CertInfo-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certList

```TypeScript
certList?: Array<CertAbstract>
```

表示证书简要信息的列表。

**Type:** Array&lt;CertAbstract&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-certList?: Array<CertAbstract>--><!--Device-CMResult-certList?: Array<CertAbstract>-End-->

**System capability:** SystemCapability.Security.CertificateManager

## credential

```TypeScript
credential?: Credential
```

表示凭据详情。

**Type:** [Credential](arkts-devicecertificate-certificatemanager-credential-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-credential?: Credential--><!--Device-CMResult-credential?: Credential-End-->

**System capability:** SystemCapability.Security.CertificateManager

## credentialDetailList

```TypeScript
credentialDetailList?: Array<Credential>
```

表示凭据详细信息。

**Type:** Array&lt;Credential&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-CMResult-credentialDetailList?: Array<Credential>--><!--Device-CMResult-credentialDetailList?: Array<Credential>-End-->

**System capability:** SystemCapability.Security.CertificateManager

## credentialList

```TypeScript
credentialList?: Array<CredentialAbstract>
```

表示凭据简要信息的列表。

**Type:** Array&lt;CredentialAbstract&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-credentialList?: Array<CredentialAbstract>--><!--Device-CMResult-credentialList?: Array<CredentialAbstract>-End-->

**System capability:** SystemCapability.Security.CertificateManager

## outData

```TypeScript
outData?: Uint8Array
```

表示签名结果。

**Type:** Uint8Array

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-outData?: Uint8Array--><!--Device-CMResult-outData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.CertificateManager

## uri

```TypeScript
uri?: string
```

表示证书或凭据的唯一标识符，最大长度为256字节。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CMResult-uri?: string--><!--Device-CMResult-uri?: string-End-->

**System capability:** SystemCapability.Security.CertificateManager

## uriList

```TypeScript
uriList?: Array<string>
```

表示证书URI列表。26.0.0

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CMResult-uriList?: Array<string>--><!--Device-CMResult-uriList?: Array<string>-End-->

**System capability:** SystemCapability.Security.CertificateManager

