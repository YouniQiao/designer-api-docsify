# PbesParams

表示基于密码的加密算法参数，当前仅支持PBES2。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-cert-interface PbesParams--><!--Device-cert-interface PbesParams-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## encryptionAlgorithm

```TypeScript
encryptionAlgorithm?: PbesEncryptionAlgorithm
```

表示PBES加密算法类型。默认为AES_256_CBC。

**Type:** [PbesEncryptionAlgorithm](arkts-devicecertificate-cert-pbesencryptionalgorithm-e.md)

**Default:** PbesEncryptionAlgorithm.AES_256_CBC

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PbesParams-encryptionAlgorithm?: PbesEncryptionAlgorithm--><!--Device-PbesParams-encryptionAlgorithm?: PbesEncryptionAlgorithm-End-->

**System capability:** SystemCapability.Security.Cert

## iterations

```TypeScript
iterations?: int
```

表示迭代次数。默认为2048。取值应为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 2048

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PbesParams-iterations?: int--><!--Device-PbesParams-iterations?: int-End-->

**System capability:** SystemCapability.Security.Cert

## saltLen

```TypeScript
saltLen?: int
```

表示盐值长度。默认为16，最小值为8。取值应为≥8的整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 16

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PbesParams-saltLen?: int--><!--Device-PbesParams-saltLen?: int-End-->

**System capability:** SystemCapability.Security.Cert

