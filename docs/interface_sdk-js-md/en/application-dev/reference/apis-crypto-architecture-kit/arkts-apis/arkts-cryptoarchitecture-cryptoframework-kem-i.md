# Kem

Key encapsulation mechanism (KEM) interface, defining methods for key encapsulation and decapsulation based on KEM. Before use, you must create a **Kem** instance by using [createKem(algNameId: KemAlgNameId): Kem](arkts-cryptoarchitecture-cryptoframework-createkem-f.md).

**Since:** 26.0.0

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## decapsulate

```TypeScript
decapsulate(priKey: PriKey, wrappedKey: Uint8Array): Promise<Uint8Array>
```

Key decapsulation operation. Using the receiver's private key, executed by the receiver, to decapsulate the shared key from the ciphertext. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes |
| [wrappedKey](arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## decapsulateSync

```TypeScript
decapsulateSync(priKey: PriKey, wrappedKey: Uint8Array): Uint8Array
```

Key decapsulation operation. Using the receiver's private key, executed by the receiver, to decapsulate the shared key from the ciphertext.

**NOTE：**It is recommended to prioritize the use of asynchronous API, [decapsulate](#decapsulate). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes |
| [wrappedKey](arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## encapsulate

```TypeScript
encapsulate(pubKey: PubKey, ikme: Uint8Array | null): Promise<KemEncapResult>
```

Key encapsulation operation. Using the recipient's public key, executed by the sender, to generate and encapsulate a shared key. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes |
| ikme | Uint8Array \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KemEncapResult](arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## encapsulateSync

```TypeScript
encapsulateSync(pubKey: PubKey, ikme: Uint8Array | null): KemEncapResult
```

Key encapsulation operation. Using the recipient's public key, executed by the sender, to generate and encapsulate a shared key.

**NOTE：**It is recommended to prioritize the use of asynchronous API, [encapsulate](#encapsulate). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes |
| ikme | Uint8Array \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KemEncapResult](arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
