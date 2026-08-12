# createTrustAnchorsWithKeyStore

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## createTrustAnchorsWithKeyStore

```TypeScript
function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>
```

Creates a [TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md#X509TrustAnchor) object array by using the CA certificate parsed from a .p12keystore file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>--><!--Device-cert-function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keystore | Uint8Array | Yes |
| pwd | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[X509TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19030002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19030003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |
| [19030006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |
| [19030004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
