# X509CRLMatchParameters

用于匹配证书吊销列表的过滤参数。如果参数中任一项都未指定，则匹配所有证书吊销列表。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface X509CRLMatchParameters--><!--Device-cert-interface X509CRLMatchParameters-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## issuer

```TypeScript
issuer?: Array<Uint8Array>
```

指定CRL颁发者，为DER编码格式。

**Type:** Array&lt;Uint8Array&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-issuer?: Array<Uint8Array>--><!--Device-X509CRLMatchParameters-issuer?: Array<Uint8Array>-End-->

**System capability:** SystemCapability.Security.Cert

## maxCRL

```TypeScript
maxCRL?: bigint
```

指定CRL编号（CRL number）的最大值。

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-maxCRL?: bigint--><!--Device-X509CRLMatchParameters-maxCRL?: bigint-End-->

**System capability:** SystemCapability.Security.Cert

## minCRL

```TypeScript
minCRL?: bigint
```

指定CRL编号（CRL number）的最小值。

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-minCRL?: bigint--><!--Device-X509CRLMatchParameters-minCRL?: bigint-End-->

**System capability:** SystemCapability.Security.Cert

## updateDateTime

```TypeScript
updateDateTime?: string
```

指定CRL更新时间。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-updateDateTime?: string--><!--Device-X509CRLMatchParameters-updateDateTime?: string-End-->

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

<!--Device-X509CRLMatchParameters-x509Cert?: X509Cert--><!--Device-X509CRLMatchParameters-x509Cert?: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

