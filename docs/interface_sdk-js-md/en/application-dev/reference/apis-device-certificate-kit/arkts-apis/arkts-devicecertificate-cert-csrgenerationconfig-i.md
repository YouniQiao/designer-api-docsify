# CsrGenerationConfig

Configuration parameters for generating a CSR, including the subject name, digest algorithm, attribute, and output format. &gt; **NOTE：**&gt; &gt; - subject is an X500DistinguishedName object. &gt; &gt; - mdName indicates the digest algorithm name. Currently, SHA1, SHA256, SHA384, and SHA512 are supported. &gt; &gt; - attributes is an optional parameter that specifies the attribute types and attribute values specified in &gt; PKCS #9 to generate a CSR. For example, challengePassword. &gt; &gt; - outFormat specifies the format of the output CSR. If the format is not specified, the PEM format is used by &gt; default.

**Since:** 23

<!--Device-cert-interface CsrGenerationConfig--><!--Device-cert-interface CsrGenerationConfig-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

## attributes

```TypeScript
attributes?: Array<CsrAttribute>
```

A collection of attributes.

**Type:** Array&lt;[CsrAttribute](arkts-devicecertificate-cert-csrattribute-i.md)&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CsrGenerationConfig-attributes?: Array<CsrAttribute>--><!--Device-CsrGenerationConfig-attributes?: Array<CsrAttribute>-End-->

**System capability:** SystemCapability.Security.Cert

## mdName

```TypeScript
mdName: string
```

Message digest algorithm name.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CsrGenerationConfig-mdName: string--><!--Device-CsrGenerationConfig-mdName: string-End-->

**System capability:** SystemCapability.Security.Cert

## outFormat

```TypeScript
outFormat?: EncodingBaseFormat
```

Output format.

**Type:** [EncodingBaseFormat](arkts-devicecertificate-cert-encodingbaseformat-e.md)

**Default:** EncodingBaseFormat.PEM

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CsrGenerationConfig-outFormat?: EncodingBaseFormat--><!--Device-CsrGenerationConfig-outFormat?: EncodingBaseFormat-End-->

**System capability:** SystemCapability.Security.Cert

## subject

```TypeScript
subject: X500DistinguishedName
```

Subject name.

**Type:** [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CsrGenerationConfig-subject: X500DistinguishedName--><!--Device-CsrGenerationConfig-subject: X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

