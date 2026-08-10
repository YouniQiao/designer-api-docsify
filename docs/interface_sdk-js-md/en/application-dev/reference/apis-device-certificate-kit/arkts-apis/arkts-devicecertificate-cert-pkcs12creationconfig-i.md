# Pkcs12CreationConfig

表示创建P12的配置。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-cert-interface Pkcs12CreationConfig--><!--Device-cert-interface Pkcs12CreationConfig-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## certEncParams

```TypeScript
certEncParams?: PbesParams
```

表示证书加密的算法参数。

**Type:** [PbesParams](arkts-devicecertificate-cert-pbesparams-i.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-certEncParams?: PbesParams--><!--Device-Pkcs12CreationConfig-certEncParams?: PbesParams-End-->

**System capability:** SystemCapability.Security.Cert

## encryptCert

```TypeScript
encryptCert?: boolean
```

表示是否加密证书。默认为true。true为加密，false为不加密。

**Type:** boolean

**Default:** true

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-encryptCert?: boolean--><!--Device-Pkcs12CreationConfig-encryptCert?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## keyEncParams

```TypeScript
keyEncParams?: PbesParams
```

表示私钥加密的算法参数。

**Type:** [PbesParams](arkts-devicecertificate-cert-pbesparams-i.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-keyEncParams?: PbesParams--><!--Device-Pkcs12CreationConfig-keyEncParams?: PbesParams-End-->

**System capability:** SystemCapability.Security.Cert

## macDigestAlgorithm

```TypeScript
macDigestAlgorithm?: Pkcs12MacDigestAlgorithm
```

表示P12的MAC摘要算法。默认为SHA256。

**Type:** [Pkcs12MacDigestAlgorithm](arkts-devicecertificate-cert-pkcs12macdigestalgorithm-e.md)

**Default:** Pkcs12MacDigestAlgorithm.SHA256

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-macDigestAlgorithm?: Pkcs12MacDigestAlgorithm--><!--Device-Pkcs12CreationConfig-macDigestAlgorithm?: Pkcs12MacDigestAlgorithm-End-->

**System capability:** SystemCapability.Security.Cert

## macIterations

```TypeScript
macIterations?: int
```

表示P12的MAC的迭代次数。默认为2048。取值应为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 2048

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-macIterations?: int--><!--Device-Pkcs12CreationConfig-macIterations?: int-End-->

**System capability:** SystemCapability.Security.Cert

## macSaltLen

```TypeScript
macSaltLen?: int
```

表示P12的MAC的盐值长度。最小值为8，默认为16。取值应为≥8的整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 16

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-macSaltLen?: int--><!--Device-Pkcs12CreationConfig-macSaltLen?: int-End-->

**System capability:** SystemCapability.Security.Cert

## password

```TypeScript
password: string
```

表示P12的密码。最小长度为4。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Pkcs12CreationConfig-password: string--><!--Device-Pkcs12CreationConfig-password: string-End-->

**System capability:** SystemCapability.Security.Cert

