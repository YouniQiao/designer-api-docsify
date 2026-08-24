# KeyAgreement

Key agreement interface, defining methods for generating shared secrets based on asymmetric key pairs. Before use, you must create a **KeyAgreement** instance by using [createKeyAgreement(algName: string): KeyAgreement](arkts-cryptoarchitecture-cryptoframework-createkeyagreement-f.md).

**Since:** 23

<!--Device-cryptoFramework-interface KeyAgreement--><!--Device-cryptoFramework-interface KeyAgreement-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.KeyAgreement
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## generateSecret

```TypeScript
generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void
```

Generates a shared secret based on the given private key and public key. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void--><!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.KeyAgreement
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for key agreement. |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes | Public key used for key agreement. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the shared secret obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

PBKDF2

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.PBKDF2Spec = {
  algName: 'PBKDF2',
  password: '123456',
  salt: new Uint8Array(16),
  iterations: 10000,
  keySize: 32
};
let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
kdf.generateSecret(spec, (err, secret) => {
  if (err) {
    console.error('key derivation result: fail.');
    return;
  }
  console.info('key derivation output = ' + secret.data);
});
```

HKDF

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.HKDFSpec = {
  algName: 'HKDF',
  key: '123456',
  salt: new Uint8Array(16),
  info: new Uint8Array(16),
  keySize: 32
};
let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND');
kdf.generateSecret(spec, (err, secret) => {
  if (err) {
    console.error('key derivation result: fail.');
    return;
  }
  console.info('key derivation output = ' + secret.data);
});
```

PBKDF2

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let spec: cryptoFramework.PBKDF2Spec = {
  algName: 'PBKDF2',
  password: '123456',
  salt: new Uint8Array(16),
  iterations: 10000,
  keySize: 32
};
let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
let kdfPromise = kdf.generateSecret(spec);
kdfPromise.then(secret => {
  console.info('key derivation output = ' + secret.data);
}).catch((error: BusinessError) => {
  console.error(`key derivation failed: errCode: ${error.code}, errMsg: ${error.message}`);
});
```

HKDF

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let spec: cryptoFramework.HKDFSpec = {
  algName: 'HKDF',
  key: '123456',
  salt: new Uint8Array(16),
  info: new Uint8Array(16),
  keySize: 32
};
let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND');
let kdfPromise = kdf.generateSecret(spec);
kdfPromise.then(secret => {
  console.info('key derivation output = ' + secret.data);
}).catch((error: BusinessError) => {
  console.error(`key derivation failed: errCode: ${error.code}, errMsg: ${error.message}`);
});
```

## generateSecret

```TypeScript
generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>
```

Generates a shared secret based on the given private key and public key. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>--><!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.KeyAgreement
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for key agreement. |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes | Public key used for key agreement. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the shared secret of key agreement. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

See [generateSecret](#generatesecret)

## generateSecretSync

```TypeScript
generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob
```

Generates a shared secret based on the given private key and public key. This API returns the shared secret generated synchronously.<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, generateSecret. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyAgreement-generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob--><!--Device-KeyAgreement-generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.KeyAgreement

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for key agreement. |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes | Public key used for key agreement. |

**Return value:**

| Type | Description |
| --- | --- |
| DataBlob | Returns the shared secret generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

PBKDF2

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.PBKDF2Spec = {
  algName: 'PBKDF2',
  password: '123456',
  salt: new Uint8Array(16),
  iterations: 10000,
  keySize: 32
};
let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
let secret = kdf.generateSecretSync(spec);
console.info('[Sync]key derivation output = ' + secret.data);
```

HKDF

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.HKDFSpec = {
  algName: 'HKDF',
  key: '123456',
  salt: new Uint8Array(16),
  info: new Uint8Array(16),
  keySize: 32
};
let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND');
let secret = kdf.generateSecretSync(spec);
console.info('[Sync]key derivation output = ' + secret.data);
```

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyAgreement-readonly algName: string--><!--Device-KeyAgreement-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.KeyAgreement
- API version 9 to 11: SystemCapability.Security.CryptoFramework

