# X509CertMatchParameters

用于匹配证书的过滤参数。如果参数中任一项都未指定，则匹配所有证书。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface X509CertMatchParameters--><!--Device-cert-interface X509CertMatchParameters-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## authorityKeyIdentifier

```TypeScript
authorityKeyIdentifier?: Uint8Array
```

指定证书颁发机构密钥。

**Type:** Uint8Array

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-authorityKeyIdentifier?: Uint8Array--><!--Device-X509CertMatchParameters-authorityKeyIdentifier?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## certPolicy

```TypeScript
certPolicy?: Array<string>
```

指定证书策略。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-certPolicy?: Array<string>--><!--Device-X509CertMatchParameters-certPolicy?: Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

## extendedKeyUsage

```TypeScript
extendedKeyUsage?: Array<string>
```

指定扩展密钥用途。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-extendedKeyUsage?: Array<string>--><!--Device-X509CertMatchParameters-extendedKeyUsage?: Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

## issuer

```TypeScript
issuer?: Uint8Array
```

指定证书颁发者，为DER编码格式。

**Type:** Uint8Array

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-issuer?: Uint8Array--><!--Device-X509CertMatchParameters-issuer?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## keyUsage

```TypeScript
keyUsage?: Array<boolean>
```

指定是否需要匹配密钥用途。true为需要，false为不需要。

**Type:** Array&lt;boolean&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-keyUsage?: Array<boolean>--><!--Device-X509CertMatchParameters-keyUsage?: Array<boolean>-End-->

**System capability:** SystemCapability.Security.Cert

## matchAllSubjectAltNames

```TypeScript
matchAllSubjectAltNames?: boolean
```

指定是否需要匹配证书主体备用名称。true为需要，false为不需要。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-matchAllSubjectAltNames?: boolean--><!--Device-X509CertMatchParameters-matchAllSubjectAltNames?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## minPathLenConstraint

```TypeScript
minPathLenConstraint?: int
```

指定证书CA路径长度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-minPathLenConstraint?: int--><!--Device-X509CertMatchParameters-minPathLenConstraint?: int-End-->

**System capability:** SystemCapability.Security.Cert

## nameConstraints

```TypeScript
nameConstraints?: Uint8Array
```

指定证书的使用者名称。

**Type:** Uint8Array

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-nameConstraints?: Uint8Array--><!--Device-X509CertMatchParameters-nameConstraints?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## privateKey

```TypeScript
privateKey?: string | Uint8Array
```

指定证书私钥，string表示PEM格式私钥，Uint8Array表示DER格式私钥。

**Type:** string \| Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertMatchParameters-privateKey?: string | Uint8Array--><!--Device-X509CertMatchParameters-privateKey?: string | Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## privateKeyValid

```TypeScript
privateKeyValid?: string
```

指定证书私钥有效期。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-privateKeyValid?: string--><!--Device-X509CertMatchParameters-privateKeyValid?: string-End-->

**System capability:** SystemCapability.Security.Cert

## publicKey

```TypeScript
publicKey?: DataBlob
```

指定证书公钥，DER编码格式。

**Type:** [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-publicKey?: DataBlob--><!--Device-X509CertMatchParameters-publicKey?: DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

## publicKeyAlgID

```TypeScript
publicKeyAlgID?: string
```

指定证书公钥的算法。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-publicKeyAlgID?: string--><!--Device-X509CertMatchParameters-publicKeyAlgID?: string-End-->

**System capability:** SystemCapability.Security.Cert

## serialNumber

```TypeScript
serialNumber?: bigint
```

指定证书的序列号。

**Type:** bigint

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-serialNumber?: bigint--><!--Device-X509CertMatchParameters-serialNumber?: bigint-End-->

**System capability:** SystemCapability.Security.Cert

## subject

```TypeScript
subject?: Uint8Array
```

指定证书主体名称，DER编码格式。

**Type:** Uint8Array

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-subject?: Uint8Array--><!--Device-X509CertMatchParameters-subject?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## subjectAlternativeNames

```TypeScript
subjectAlternativeNames?: Array<GeneralName>
```

指定证书主体备用名称。

**Type:** Array&lt;GeneralName&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-subjectAlternativeNames?: Array<GeneralName>--><!--Device-X509CertMatchParameters-subjectAlternativeNames?: Array<GeneralName>-End-->

**System capability:** SystemCapability.Security.Cert

## subjectKeyIdentifier

```TypeScript
subjectKeyIdentifier?: Uint8Array
```

指定证书公钥。

**Type:** Uint8Array

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-subjectKeyIdentifier?: Uint8Array--><!--Device-X509CertMatchParameters-subjectKeyIdentifier?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## validDate

```TypeScript
validDate?: string
```

指定证书有效期。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-validDate?: string--><!--Device-X509CertMatchParameters-validDate?: string-End-->

**System capability:** SystemCapability.Security.Cert

## x509Cert

```TypeScript
x509Cert?: X509Cert
```

指定具体的证书对象。

**Type:** [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertMatchParameters-x509Cert?: X509Cert--><!--Device-X509CertMatchParameters-x509Cert?: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

