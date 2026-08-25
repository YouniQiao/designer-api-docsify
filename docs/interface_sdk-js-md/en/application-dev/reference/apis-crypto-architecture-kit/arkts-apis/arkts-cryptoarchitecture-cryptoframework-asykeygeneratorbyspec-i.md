# AsyKeyGeneratorBySpec

Asymmetric key generator interface with specified key specifications, defining methods for generating asymmetric keys based on specified key specifications. Before use, you must create an **AsyKeyGeneratorBySpec** instance by using [createAsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md).

**Since:** 10

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## generateKeyPair

```TypeScript
generateKeyPair(callback: AsyncCallback<KeyPair>): void
```

Generates a key pair using this asymmetric key generator. This API uses an asynchronous callback to return the result.

If a key parameter of the [COMMON_PARAMS_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, a key pair will be randomly generated. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain a key pair that is consistent with the specified key parameters.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateKeyPair

```TypeScript
generateKeyPair(): Promise<KeyPair>
```

Generates a key pair using this asymmetric key generator. This API uses a promise to return the result.

If a key parameter of the [COMMON_PARAMS_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, a key pair will be randomly generated. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain a key pair that is consistent with the specified key parameters.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateKeyPairSync

```TypeScript
generateKeyPairSync(): KeyPair
```

Generates a key pair using this asymmetric key generator. This API returns the result synchronously.

If a key parameter of the [COMMON_PARAMS_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, a key pair will be randomly generated. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain a key pair that is consistent with the specified key parameters.

**NOTE：**It is recommended to prioritize the use of asynchronous API, generateKeyPair. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generatePriKey

```TypeScript
generatePriKey(callback: AsyncCallback<PriKey>): void
```

Generates a private key using this asymmetric key generator. This API uses an asynchronous callback to return the result.

If [PRIVATE_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) is used to create a key generator, the key generator generates the specified private key. If [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) is used to create a key generator, you can obtain the specified private key from the key pair generated.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generatePriKey

```TypeScript
generatePriKey(): Promise<PriKey>
```

Generates a private key using this asymmetric key generator. This API uses a promise to return the result.

If a key parameter of the [PRIVATE_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, a private key can be obtained. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain the private key from the key pair generated.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generatePriKeySync

```TypeScript
generatePriKeySync(): PriKey
```

Generates a private key using this asymmetric key generator. This API returns the result synchronously.

If a key parameter of the [PRIVATE_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, a private key can be obtained. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain the private key from the key pair generated.

**NOTE：**It is recommended to prioritize the use of asynchronous API, [generatePriKey](#generateprikey). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generatePubKey

```TypeScript
generatePubKey(callback: AsyncCallback<PubKey>): void
```

Generates a public key using this asymmetric key generator. This API uses an asynchronous callback to return the result.

If a key parameter of the [PUBLIC_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, the specified public key can be obtained. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain the specified public key from the key pair generated.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generatePubKey

```TypeScript
generatePubKey(): Promise<PubKey>
```

Generates a public key using this asymmetric key generator. This API uses a promise to return the result.

If a key parameter of the [PUBLIC_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, the specified public key can be obtained. If a key parameter of the [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) type is used to create the key generator, you can obtain the specified public key from the key pair generated.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generatePubKeySync

```TypeScript
generatePubKeySync(): PubKey
```

Generates a public key using this asymmetric key generator. This API returns the result synchronously.

If [PUBLIC_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) is used to create a key generator, the key generator generates the specified public key. If [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) is used to create a key generator, you can obtain the specified public key from the key pair generated.

**NOTE：**It is recommended to prioritize the use of asynchronous API, [generatePubKey](#generatepubkey). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name of the generator.

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework
