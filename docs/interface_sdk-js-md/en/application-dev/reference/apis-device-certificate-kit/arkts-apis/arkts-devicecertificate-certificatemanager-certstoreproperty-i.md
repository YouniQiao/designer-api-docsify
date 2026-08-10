# CertStoreProperty

表示获取证书存储位置的参数集合，包括证书的类型及证书的位置。

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

表示证书算法类型。仅当certType为CA_CERT_SYSTEM时有效，默认值为INTERNATIONAL。海外设备不支持SM算法。

**Type:** [CertAlgorithm](arkts-devicecertificate-certificatemanager-certalgorithm-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CertStoreProperty-certAlg?: CertAlgorithm--><!--Device-CertStoreProperty-certAlg?: CertAlgorithm-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certScope

```TypeScript
certScope?: CertScope
```

表示证书的存储位置。当证书类型为CA_CERT_USER时，此项为必选项。

**Type:** [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CertStoreProperty-certScope?: CertScope--><!--Device-CertStoreProperty-certScope?: CertScope-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certType

```TypeScript
certType: CertType
```

表示证书的类型。

**Type:** [CertType](../../apis-network-kit/arkts-apis/arkts-network-http-certtype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CertStoreProperty-certType: CertType--><!--Device-CertStoreProperty-certType: CertType-End-->

**System capability:** SystemCapability.Security.CertificateManager

