# ScryptSpec

密钥派生函数参数[KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md)的子类，作为SCRYPT密钥派生函数进行密钥派生时的输入。

> **说明：**
> 
> passphrase指的是原始密码，如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型，同时需要确保该
> 字符串为utf-8编码，否则派生结果会有差异。

**Inheritance/Implementation:** ScryptSpec extends [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface ScryptSpec extends KdfSpec--><!--Device-cryptoFramework-interface ScryptSpec extends KdfSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## keySize

```TypeScript
keySize: int
```

派生得到的密钥字节长度，需要为正整数，单位为bytes。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-keySize: int--><!--Device-ScryptSpec-keySize: int-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## maxMemory

```TypeScript
maxMemory: long
```

最大内存限制参数，需要为正整数，单位为bytes。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-maxMemory: long--><!--Device-ScryptSpec-maxMemory: long-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## n

```TypeScript
n: long
```

CPU/内存开销参数，需要为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-n: long--><!--Device-ScryptSpec-n: long-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## p

```TypeScript
p: long
```

并行化参数，需要为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-p: long--><!--Device-ScryptSpec-p: long-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## passphrase

```TypeScript
passphrase: string | Uint8Array
```

用户输入的原始密码。

**Type:** string \| Uint8Array

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-passphrase: string | Uint8Array--><!--Device-ScryptSpec-passphrase: string | Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## r

```TypeScript
r: long
```

块大小参数，需要为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-r: long--><!--Device-ScryptSpec-r: long-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## salt

```TypeScript
salt: Uint8Array
```

盐值。

**Type:** Uint8Array

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScryptSpec-salt: Uint8Array--><!--Device-ScryptSpec-salt: Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

