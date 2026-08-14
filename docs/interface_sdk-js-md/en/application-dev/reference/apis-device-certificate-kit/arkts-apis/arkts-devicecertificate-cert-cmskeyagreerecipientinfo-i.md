# CmsKeyAgreeRecipientInfo

Represents KeyAgree recipient information for CMS enveloped data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cert-interface CmsKeyAgreeRecipientInfo--><!--Device-cert-interface CmsKeyAgreeRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'cert';
```

## cert

```TypeScript
cert: X509Cert
```

EC certificate.

**Type:** X509Cert

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CmsKeyAgreeRecipientInfo-cert: X509Cert--><!--Device-CmsKeyAgreeRecipientInfo-cert: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

## digestAlgorithm

```TypeScript
digestAlgorithm?: CmsKeyAgreeRecipientDigestAlgorithm
```

KDF digest algorithm. The default value is **SHA256**.

**Type:** [CmsKeyAgreeRecipientDigestAlgorithm](arkts-devicecertificate-cert-cmskeyagreerecipientdigestalgorithm-e.md)

**Default:** CmsKeyAgreeRecipientDigestAlgorithm.SHA256

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CmsKeyAgreeRecipientInfo-digestAlgorithm?: CmsKeyAgreeRecipientDigestAlgorithm--><!--Device-CmsKeyAgreeRecipientInfo-digestAlgorithm?: CmsKeyAgreeRecipientDigestAlgorithm-End-->

**System capability:** SystemCapability.Security.Cert

