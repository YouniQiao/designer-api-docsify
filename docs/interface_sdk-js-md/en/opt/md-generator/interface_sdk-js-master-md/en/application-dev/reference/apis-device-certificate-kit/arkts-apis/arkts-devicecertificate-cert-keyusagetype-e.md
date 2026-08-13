# KeyUsageType

Enumerates the purposes for which the key in the certificate is used.

**Since:** 23

**Deprecated since:** -1

<!--Device-cert-enum KeyUsageType--><!--Device-cert-enum KeyUsageType-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_DIGITAL_SIGNATURE

```TypeScript
KEYUSAGE_DIGITAL_SIGNATURE = 0
```

The certificate holder can use the private key contained in the certificate to generate a digital signature.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_DIGITAL_SIGNATURE = 0--><!--Device-KeyUsageType-KEYUSAGE_DIGITAL_SIGNATURE = 0-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_NON_REPUDIATION

```TypeScript
KEYUSAGE_NON_REPUDIATION = 1
```

The certificate holder can use the key to create a digital signature as part of a non-repudiation service.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_NON_REPUDIATION = 1--><!--Device-KeyUsageType-KEYUSAGE_NON_REPUDIATION = 1-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_KEY_ENCIPHERMENT

```TypeScript
KEYUSAGE_KEY_ENCIPHERMENT = 2
```

The certificate holder can use the public key contained in the certificate for key encryption.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_KEY_ENCIPHERMENT = 2--><!--Device-KeyUsageType-KEYUSAGE_KEY_ENCIPHERMENT = 2-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_DATA_ENCIPHERMENT

```TypeScript
KEYUSAGE_DATA_ENCIPHERMENT = 3
```

The certificate holder can use the public key contained in the certificate for data encryption.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_DATA_ENCIPHERMENT = 3--><!--Device-KeyUsageType-KEYUSAGE_DATA_ENCIPHERMENT = 3-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_KEY_AGREEMENT

```TypeScript
KEYUSAGE_KEY_AGREEMENT = 4
```

The certificate holder can use the private key contained in the certificate to perform key agreement operations.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_KEY_AGREEMENT = 4--><!--Device-KeyUsageType-KEYUSAGE_KEY_AGREEMENT = 4-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_KEY_CERT_SIGN

```TypeScript
KEYUSAGE_KEY_CERT_SIGN = 5
```

The certificate holder can use the private key contained in the certificate to sign other certificates.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_KEY_CERT_SIGN = 5--><!--Device-KeyUsageType-KEYUSAGE_KEY_CERT_SIGN = 5-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_CRL_SIGN

```TypeScript
KEYUSAGE_CRL_SIGN = 6
```

The certificate holder can use the private key contained in the certificate to sign CRLs.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_CRL_SIGN = 6--><!--Device-KeyUsageType-KEYUSAGE_CRL_SIGN = 6-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_ENCIPHER_ONLY

```TypeScript
KEYUSAGE_ENCIPHER_ONLY = 7
```

The certificate holder can use the key to perform encryption operations only.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_ENCIPHER_ONLY = 7--><!--Device-KeyUsageType-KEYUSAGE_ENCIPHER_ONLY = 7-End-->

**System capability:** SystemCapability.Security.Cert

## KEYUSAGE_DECIPHER_ONLY

```TypeScript
KEYUSAGE_DECIPHER_ONLY = 8
```

The certificate holder can use the key to perform decryption operations only.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyUsageType-KEYUSAGE_DECIPHER_ONLY = 8--><!--Device-KeyUsageType-KEYUSAGE_DECIPHER_ONLY = 8-End-->

**System capability:** SystemCapability.Security.Cert
