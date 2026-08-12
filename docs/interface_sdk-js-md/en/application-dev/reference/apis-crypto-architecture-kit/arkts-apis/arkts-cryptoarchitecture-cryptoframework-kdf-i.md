# Kdf

Key derivation function (KDF) interface, defining methods for deriving keys based on key derivation parameters.Before use, you must create a **Kdf** instance by using [createKdf](arkts-cryptoarchitecture-cryptoframework-createkdf-f.md#createKdf).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface Kdf--><!--Device-cryptoFramework-interface Kdf-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## generateSecret

```TypeScript
generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void
```

Generates a key based on the specified key derivation parameters. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Kdf-generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void--><!--Device-Kdf-generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md) | Yes | Parameters of the key derivation function. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the derived key obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: &lt;br&gt;1. Invalid key length in the params; &lt;br&gt;2. Invalid info length in the params; &lt;br&gt;3. Invalid keySize in the params.<br>**Applicable version:** 22 and later |

## Examples

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

## generateSecret

```TypeScript
generateSecret(params: KdfSpec): Promise<DataBlob>
```

Generates a key based on the specified key derivation parameters. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Kdf-generateSecret(params: KdfSpec): Promise<DataBlob>--><!--Device-Kdf-generateSecret(params: KdfSpec): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md) | Yes | Parameters of the key derivation function. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the derived key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: &lt;br&gt;1. Invalid key length in the params; &lt;br&gt;2. Invalid info length in the params; &lt;br&gt;3. Invalid keySize in the params.<br>**Applicable version:** 22 and later |

## Examples

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

## generateSecretSync

```TypeScript
generateSecretSync(params: KdfSpec): DataBlob
```

Generates a key based on the specified key derivation parameters. This API returns the result synchronously.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, [generateSecret](generateSecret). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Kdf-generateSecretSync(params: KdfSpec): DataBlob--><!--Device-Kdf-generateSecretSync(params: KdfSpec): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md) | Yes | Parameters of the key derivation function. |

**Return value:**

| Type | Description |
| --- | --- |
| DataBlob | The derived key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: &lt;br&gt;1. Invalid key length in the params; &lt;br&gt;2. Invalid info length in the params; &lt;br&gt;3. Invalid keySize in the params.<br>**Applicable version:** 22 and later |

## Examples

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

Indicates the algorithm name of the key derivation function.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Kdf-readonly algName: string--><!--Device-Kdf-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

