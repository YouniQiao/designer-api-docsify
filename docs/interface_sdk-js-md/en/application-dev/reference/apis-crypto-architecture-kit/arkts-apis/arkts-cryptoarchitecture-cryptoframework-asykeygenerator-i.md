# AsyKeyGenerator

Asymmetric key generator interface, defining methods for generating asymmetric keys. Before use, you must create an **AsyKeyGenerator** instance by using [createAsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createasykeygenerator-f.md).

**Since:** 23

<!--Device-cryptoFramework-interface AsyKeyGenerator--><!--Device-cryptoFramework-interface AsyKeyGenerator-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## convertKey

```TypeScript
convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void
```

Converts asymmetric key data to a key pair object. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void--><!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | DataBlob | Yes | The public key data blob. |
| priKey | DataBlob | Yes | The private key data blob. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the asymmetric key pair obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = [
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob, (err, symKey) => {
    console.info('Convert symKey result: success, algName: ' + symKey.algName);
  });
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = [
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob)
    .then(symKey => {
      console.info('Convert symKey result: success, algName: ' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(`Convert symKey failed, ${error.code}, ${error.message}`);
    });
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let pubKeyArray =
  new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
let priKeyArray =
  new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // Binary data of the public key.
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // Binary data of the private key.
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
  if (err) {
    console.error('convertKey result: fail.');
    return;
  }
  console.info('convertKey result: success.');
});
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let pubKeyArray =
  new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
let priKeyArray =
  new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // Binary data of the public key.
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // Binary data of the private key.
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
let keyGenPromise = asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob);
keyGenPromise.then(keyPair => {
  console.info('convertKey result: success.');
}).catch((error: BusinessError) => {
  console.error(`convertKey failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

## convertKey

```TypeScript
convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void
```

Converts data into an asymmetric key pair. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void--><!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | DataBlob \| null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| priKey | DataBlob \| null | Yes | Private key material to convert. If no private key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the key pair obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

See [convertKey](#convertkey)

## convertKey

```TypeScript
convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>
```

Converts asymmetric key data to a key pair object. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>--><!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | DataBlob | Yes | The public key data blob. |
| priKey | DataBlob | Yes | The private key data blob. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Promise used to return the asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

See [convertKey](#convertkey)

## convertKey

```TypeScript
convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>
```

Converts data into an asymmetric key pair. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>--><!--Device-AsyKeyGenerator-convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | DataBlob \| null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| priKey | DataBlob \| null | Yes | Private key material to convert. If no private key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Promise used to return the asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

See [convertKey](#convertkey)

## convertKeySync

```TypeScript
convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair
```

Converts data into an asymmetric key pair. This API returns the result synchronously.

<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, convertKey. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AsyKeyGenerator-convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair--><!--Device-AsyKeyGenerator-convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | DataBlob \| null | Yes | Public key material. If no public key needs to be converted, set this parameter to **null**. Before API version 10, only **DataBlob** is supported. Since API version 10, **null** can be passed in. |
| priKey | DataBlob \| null | Yes | Private key material. If no private key needs to be converted, set this parameter to **null**. Before API version 10, only **DataBlob** is supported. Since API version 10, **null** can be passed in. |

**Return value:**

| Type | Description |
| --- | --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | Asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function testConvertKeySync() {
  // The symmetric key length is 64 bytes (512 bits).
  let keyMessage = '87654321abcdefgh87654321abcdefgh87654321abcdefgh87654321abcdefgh';
  let keyBlob: cryptoFramework.DataBlob = {
    data : new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
  }
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  let key = symKeyGenerator.convertKeySync(keyBlob);
  let encodedKey = key.getEncoded();
  console.info('key encoded data: ' + encodedKey.data);
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let pubKeyArray =
  new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
let priKeyArray =
  new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // Binary data of the public key.
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // Binary data of the private key.
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
try {
  let keyPairData = asyKeyGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  if (keyPairData != null) {
    console.info('[Sync]: key pair result: success.');
  } else {
    console.error('[Sync]: convert key pair result: fail.');
  }
} catch (e) {
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

## convertPemKey

```TypeScript
convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>
```

Converts data into an asymmetric key pair. This API uses a promise to return the result.

> **NOTE：**
> 
> 1. When **convertPemKey()** is used to convert an external string into an asymmetric key object defined by
> the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and PEM
> encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and PEM
> encoding format.
> 2. In **convertPemKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is
> passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
> 3. When **convertPemKey** is used to convert an external string into an asymmetric key object defined by the
> Crypto framework, the system does not verify whether the specifications of the generated key object are the
> same as the key specifications specified for the asymmetric key generator.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AsyKeyGenerator-convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>--><!--Device-AsyKeyGenerator-convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | string \| null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string \| null | Yes | Private key material to convert. If no private key needs to be converted, set this parameter to **null**.<br>Note: The public key and private key materials cannot be both null or empty strings. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Promise used to return the asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n'
    + '-----END RSA PRIVATE KEY-----\n';
let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n'
    + '-----END RSA PUBLIC KEY-----\n';

async function TestConvertPemKeyByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024)
    .then(keyPair => {
      console.info('convertPemKey result: success.');
    }).catch((error: BusinessError) => {
    console.error(`convertPemKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let priKeyPkcs1EncodingStr: string =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'Proc-Type: 4,ENCRYPTED\n'
    + 'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n'
    + '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n'
    + 't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n'
    + 'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n'
    + '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n'
    + 'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n'
    + 'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n'
    + 'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n'
    + 'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n'
    + 'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n'
    + 'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n'
    + 'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n'
    + 'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n'
    + 'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n'
    + '-----END RSA PRIVATE KEY-----\n'

async function TestConvertPemKeyByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  asyKeyGenerator.convertPemKey(null, priKeyPkcs1EncodingStr, '123456')
    .then(keyPair => {
      console.info('convertPemKey result: success.');
    }).catch((error: BusinessError) => {
    console.error(`convertPemKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

## convertPemKey

```TypeScript
convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>
```

Converts data into an asymmetric key pair. Encrypted private keys are supported. The private key password is synchronously passed to decrypt the private key. This API uses a promise to return the result.

> **NOTE：**
> 
> 1. When **convertPemKey()** is used to convert an external string into an asymmetric key object defined by
> the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and PEM
> encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and PEM
> encoding format.
> 2. In **convertPemKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is
> passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
> 3. When **convertPemKey** is used to convert an external string into an asymmetric key object defined by the
> Crypto framework, the system does not verify whether the specifications of the generated key object are the
> same as the key specifications specified for the asymmetric key generator.
> 4. If **password** is passed in, it can be used to decrypt the encrypted private key.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AsyKeyGenerator-convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>--><!--Device-AsyKeyGenerator-convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | string \| null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string \| null | Yes | Private key material to convert. If no private key needs to be converted, set this parameter to **null**.<br>Note: The public key and private key materials cannot be both null or empty strings. |
| password | string | Yes | Password used to decrypt the private key. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Promise used to return the asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

See [convertPemKey](#convertpemkey)

## convertPemKeySync

```TypeScript
convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair
```

Converts data into an asymmetric key pair. This API returns the result synchronously.

> **NOTE：**
> The precautions for using **convertPemKeySync** are the same as those for **convertPemKey**. For details, see
> the description of
> [convertPemKey](#convertpemkey)
> .

<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, [convertPemKey](#convertpemkey). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AsyKeyGenerator-convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair--><!--Device-AsyKeyGenerator-convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | string \| null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string \| null | Yes | Private key material. If no private key needs to be converted, set this parameter to **null**.<br>Note: The public key and private key materials cannot be both null or empty strings. |

**Return value:**

| Type | Description |
| --- | --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | Asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n'
    + '-----END RSA PRIVATE KEY-----\n';
let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n'
    + '-----END RSA PUBLIC KEY-----\n';

function TestConvertPemKeyBySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(publicPkcs1Str1024, priKeyPkcs1Str1024);
    if (keyPairData != null) {
      console.info('[Sync]: convert pem key pair result: success.');
    } else {
      console.error('[Sync]: convert pem key pair result: fail.');
    }
  } catch (e) {
    console.error(`Sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1EncodingStr: string =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'Proc-Type: 4,ENCRYPTED\n'
    + 'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n'
    + '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n'
    + 't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n'
    + 'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n'
    + '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n'
    + 'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n'
    + 'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n'
    + 'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n'
    + 'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n'
    + 'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n'
    + 'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n'
    + 'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n'
    + 'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n'
    + 'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n'
    + '-----END RSA PRIVATE KEY-----\n'

function TestConvertPemKeyBySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(null, priKeyPkcs1EncodingStr, '123456');
    if (keyPairData != null) {
      console.info('[Sync]: convert pem key pair result: success.');
    } else {
      console.error('[Sync]: convert pem key pair result: fail.');
    }
  } catch (e) {
    console.error(`Sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

## convertPemKeySync

```TypeScript
convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair
```

Converts data into an asymmetric key pair. Encrypted private keys are supported. The private key password is synchronously passed to decrypt the private key.

> **NOTE：**
> The precautions for using **convertPemKeySync** are the same as those for
> [convertPemKey](#convertpemkey)
> .

<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, [convertPemKey](#convertpemkey). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AsyKeyGenerator-convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair--><!--Device-AsyKeyGenerator-convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | string \| null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string \| null | Yes | Private key material. If no private key needs to be converted, set this parameter to **null**. <br>Note: **pubKey** and **priKey** cannot be **null** at the same time. |
| password | string | Yes | Password used to decrypt the private key. |

**Return value:**

| Type | Description |
| --- | --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | Asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

See [convertPemKeySync](#convertpemkeysync)

## generateKeyPair

```TypeScript
generateKeyPair(callback: AsyncCallback<KeyPair>): void
```

Generates a random key pair using this asymmetric key generator. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-generateKeyPair(callback: AsyncCallback<KeyPair>): void--><!--Device-AsyKeyGenerator-generateKeyPair(callback: AsyncCallback<KeyPair>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the key pair obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: Incorrect parameter types; |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
asyKeyGenerator.generateKeyPair((err, keyPair) => {
  if (err) {
    console.error('generateKeyPair result: fail.');
    return;
  }
  console.info('generateKeyPair result: success.');
})
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
let keyGenPromise = asyKeyGenerator.generateKeyPair();
keyGenPromise.then(keyPair => {
  console.info('generateKeyPair result: success.');
}).catch((error: BusinessError) => {
  console.error('generateKeyPair result: fail.');
});
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPair() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generateKeyPair((err, keyPair) => {
    if (err) {
      console.error('generateKeyPair result: fail.');
      return;
    }
    console.info('generateKeyPair result: success.');
  })
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPair() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generateKeyPair();
  keyGenPromise.then(keyPair => {
    console.info('generateKeyPair result: success.');
  }).catch((error: BusinessError) => {
    console.error(`generateKeyPair failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

## generateKeyPair

```TypeScript
generateKeyPair(): Promise<KeyPair>
```

Generates a random key pair using this asymmetric key generator. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-generateKeyPair(): Promise<KeyPair>--><!--Device-AsyKeyGenerator-generateKeyPair(): Promise<KeyPair>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Promise used to return the asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

See [generateKeyPair](#generatekeypair)

## generateKeyPairSync

```TypeScript
generateKeyPairSync(): KeyPair
```

Generates a random key pair using this asymmetric key generator. This API returns the result synchronously.

<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, generateKeyPair. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AsyKeyGenerator-generateKeyPairSync(): KeyPair--><!--Device-AsyKeyGenerator-generateKeyPairSync(): KeyPair-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value:**

| Type | Description |
| --- | --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | Asymmetric key pair. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
try {
  let keyPairData = asyKeyGenerator.generateKeyPairSync();
  if (keyPairData != null) {
    console.info('[Sync]: key pair result: success.');
  } else {
    console.error('[Sync]: get key pair result: fail.');
  }
} catch (e) {
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPairSync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let keyPairData = asyKeyGeneratorBySpec.generateKeyPairSync();
    if (keyPairData != null) {
      console.info('[Sync]: key pair result: success.');
    } else {
      console.error('[Sync]: get key pair result: fail.');
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`sync failed: errCode: ${error.code}, errMsg: ${error.message}`);
  }
}
```

## algName

```TypeScript
readonly algName: string
```

The algName of the AsyKeyGenerator.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeyGenerator-readonly algName: string--><!--Device-AsyKeyGenerator-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

