# Pkcs12Data

P12（PKCS #12）数据，包含私钥、证书和其他证书。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cert-interface Pkcs12Data--><!--Device-cert-interface Pkcs12Data-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## cert

```TypeScript
cert?: X509Cert
```

和私钥匹配的证书。

**Type:** [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12Data-cert?: X509Cert--><!--Device-Pkcs12Data-cert?: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

## otherCerts

```TypeScript
otherCerts?: Array<X509Cert>
```

其他证书。

**Type:** Array&lt;X509Cert&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12Data-otherCerts?: Array<X509Cert>--><!--Device-Pkcs12Data-otherCerts?: Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

## privateKey

```TypeScript
privateKey?: string | Uint8Array
```

私钥。**string**对应PEM格式，**Uint8Array**对应DER格式。

**Type:** string \| Uint8Array

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12Data-privateKey?: string | Uint8Array--><!--Device-Pkcs12Data-privateKey?: string | Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

