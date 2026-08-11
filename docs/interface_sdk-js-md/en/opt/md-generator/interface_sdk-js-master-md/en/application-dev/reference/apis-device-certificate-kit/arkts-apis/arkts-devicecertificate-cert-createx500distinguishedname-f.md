# createX500DistinguishedName

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createX500DistinguishedName

```TypeScript
function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>
```

Creates an **X500DistinguishedName** object with a name in the form of a string. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>--><!--Device-cert-function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nameStr | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;X500DistinguishedName&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Convert the string into a Uint8Array.
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
async function createX500DistinguishedName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```


## createX500DistinguishedName

```TypeScript
function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>
```

Creates an **X500DistinguishedName** object with a name in DER format. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>--><!--Device-cert-function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nameDer | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;X500DistinguishedName&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameDer =
  new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
    101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

async function createX500DistinguishedName() {
  try {
    cert.createX500DistinguishedName(nameDer)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```
