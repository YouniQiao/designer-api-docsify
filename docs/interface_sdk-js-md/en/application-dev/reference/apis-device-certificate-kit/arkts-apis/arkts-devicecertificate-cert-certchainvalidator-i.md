# CertChainValidator

Provides APIs for certificate chain validator operations.

**Since:** 9

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## validate

```TypeScript
validate(certChain: CertChainData, callback: AsyncCallback<void>): void
```

Validates an X.509 certificate chain. This API uses an asynchronous callback to return the result.

Because the system time on the device is untrusted, the certificate chain validator does not verify the certificate validity period. To check the validity period of a certificate, use the [checkValidityWithDate()](arkts-devicecertificate-cert-x509cert-i.md#checkvaliditywithdate) API of the **X509Cert** class. For details about certificate specifications, see [Certificate Specifications](../../../security/DeviceCertificateKit/certificate-framework-overview.md#certificate-specifications).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| certChain | [CertChainData](arkts-devicecertificate-cert-certchaindata-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |

## validate

```TypeScript
validate(certChain: CertChainData): Promise<void>
```

Validates an X.509 certificate chain. This API uses a promise to return the result.

Because the system time on the device is untrusted, the certificate chain validator does not verify the certificate validity period. To check the validity period of a certificate, use the [checkValidityWithDate()](arkts-devicecertificate-cert-x509cert-i.md#checkvaliditywithdate) API of the **X509Cert** class. For details about certificate specifications, see [Certificate Specifications](../../../security/DeviceCertificateKit/certificate-framework-overview.md#certificate-specifications).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| certChain | [CertChainData](arkts-devicecertificate-cert-certchaindata-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |

## validateCert

```TypeScript
validateCert(cert: X509Cert, params: CertValidationParams): Promise<CertValidationResult>
```

Validates a certificate by building and verifying its certificate chain. This API uses a promise to return the result.

The certificate chain construction process complies with the following rules:
1. Trusted anchor source: The trusted certificate list (trustedCerts) is always used as the trust anchor source.
The preconfigured certificate is used as the trust anchor source only when trustSystemCa is set to true.
2. Issuer search sequence: The system searches for the issuer from the trust anchor source first. If the issuer
cannot be found, the system searches for the issuer in the untrusted certificate list (untrustedCerts). The intermediate CA certificate downloaded online is an untrusted certificate.
3. Trust anchor locking: Once the issuer is found in the trust anchor source, the subsequent lookup process does
not roll back to the untrusted certificate, that is, the subsequent certificates must come from the trust anchor source.
4. Construction completion conditions:
If partialChain is false (default value), the build is complete only when the root certificate (self-signed certificate) is found. If partialChain is true, the first time the issuer is found in the trust anchor source, the build is complete.
5. Follow-up verification: After the certificate chain is constructed, perform other verification operations,
such as certificate signature verification and certificate revocation check.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes |
| params | [CertValidationParams](arkts-devicecertificate-cert-certvalidationparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CertValidationResult](arkts-devicecertificate-cert-certvalidationresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |
| [19030009](../errorcode-cert.md#19030009-untrusted-certificate) |
| [19030010](../errorcode-cert.md#19030010-certificate-revoked) |
| [19030011](../errorcode-cert.md#19030011-unsupported-key-extensions) |
| [19030012](../errorcode-cert.md#19030012-host-name-mismatch) |
| [19030013](../errorcode-cert.md#19030013-email-address-mismatch) |
| [19030014](../errorcode-cert.md#19030014-key-usage-mismatch) |
| [19030015](../errorcode-cert.md#19030015-crl-not-found) |
| [19030016](../errorcode-cert.md#19030016-invalid-crl) |
| [19030017](../errorcode-cert.md#19030017-crl-expired) |
| [19030018](../errorcode-cert.md#19030018-crl-signature-verification-failure) |
| [19030019](../errorcode-cert.md#19030019-crl-issuer-not-found) |
| [19030020](../errorcode-cert.md#19030020-ocsp-response-not-found) |
| [19030021](../errorcode-cert.md#19030021-invalid-ocsp-response) |
| [19030022](../errorcode-cert.md#19030022-ocsp-signature-verification-failure) |
| [19030023](../errorcode-cert.md#19030023-unknown-ocsp-certificate-status) |
| [19030024](../errorcode-cert.md#19030024-network-connection-timeout) |

## algorithm

```TypeScript
readonly algorithm: string
```

Algorithm used by the X.509 certificate chain validator.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert
