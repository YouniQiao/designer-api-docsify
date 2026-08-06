# PbesParams

Represents PBES algorithm parameters. Currently, only PBES2 is supported.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-cert-interface PbesParams--><!--Device-cert-interface PbesParams-End-->

**System capability:** SystemCapability.Security.Cert

## encryptionAlgorithm

```TypeScript
encryptionAlgorithm?: PbesEncryptionAlgorithm
```

PBES algorithm type. The default value is **AES\_256\_CBC**.

**Type:** PbesEncryptionAlgorithm

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

Number of iterations. The default value is **2048**.The value must be a positive integer.

**Type:** int

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

Length of the salt value. The default value is **16**, and the minimum value is **8**.The value must be an integer greater than or equal to 8.

**Type:** int

**Default:** 16

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PbesParams-saltLen?: int--><!--Device-PbesParams-saltLen?: int-End-->

**System capability:** SystemCapability.Security.Cert

