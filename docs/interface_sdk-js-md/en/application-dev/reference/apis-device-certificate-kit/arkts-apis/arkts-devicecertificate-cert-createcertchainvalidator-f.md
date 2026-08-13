# createCertChainValidator

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## createCertChainValidator

```TypeScript
function createCertChainValidator(algorithm: string): CertChainValidator
```

Creates a **CertChainValidator** object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function createCertChainValidator(algorithm: string): CertChainValidator--><!--Device-cert-function createCertChainValidator(algorithm: string): CertChainValidator-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | string | Yes | Certificate chain validator algorithm. Currently, only **PKIX** is supported. |

**Return value:**

| Type | Description |
| --- | --- |
| [CertChainValidator](arkts-devicecertificate-cert-certchainvalidator-i.md) | CertChainValidator** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validator = cert.createCertChainValidator('PKIX');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`createCertChainValidator failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

