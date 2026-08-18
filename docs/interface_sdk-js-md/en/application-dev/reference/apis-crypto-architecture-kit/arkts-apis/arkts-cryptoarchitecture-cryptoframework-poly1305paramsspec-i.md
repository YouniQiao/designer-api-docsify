# Poly1305ParamsSpec

Encapsulates the parameters for encryption or decryption using the ChaCha20-Poly1305 AEAD mode, which requires a nonce, AAD, and an authentication tag. It is a child class of [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) and used as a parameter in [init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init) for symmetric encryption or decryption. <br>Applicable to ChaCha20-Poly1305. > **NOTE：**> > Before passing a value to > [init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init), specify > **algName** for its parent class [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md). > > When the Poly1305 mode is used for encryption, you need to extract the last 16 bytes from the > [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) returned by > [doFinal()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinal) or > [doFinalSync()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinalsync) and use them as **authTag** in > [Poly1305ParamsSpec](#poly1305paramsspec) for > [init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init) or > [initSync()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#initsync) during decryption.

**Inheritance/Implementation:** Poly1305ParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 23

<!--Device-cryptoFramework-interface Poly1305ParamsSpec--><!--Device-cryptoFramework-interface Poly1305ParamsSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## aad

```TypeScript
aad: DataBlob
```

Additional authenticated data.

**Type:** DataBlob

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Poly1305ParamsSpec-aad: DataBlob--><!--Device-Poly1305ParamsSpec-aad: DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## authTag

```TypeScript
authTag: DataBlob
```

Authentication tag, which is of 16 bytes.

**Type:** DataBlob

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Poly1305ParamsSpec-authTag: DataBlob--><!--Device-Poly1305ParamsSpec-authTag: DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## iv

```TypeScript
iv: DataBlob
```

Nonce (passed as the **iv** field), which is of 12 bytes.

**Type:** DataBlob

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Poly1305ParamsSpec-iv: DataBlob--><!--Device-Poly1305ParamsSpec-iv: DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

