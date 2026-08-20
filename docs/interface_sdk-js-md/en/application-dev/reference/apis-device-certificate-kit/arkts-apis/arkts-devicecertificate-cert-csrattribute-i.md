# CsrAttribute

Defines the CSR attribute representation.

<br>CSR attribute field. Currently, only string-type attribute fields are supported. The attribute value added to the CSR is encoded in UTF-8 format. The common type is challengePassword.

**Since:** 23

<!--Device-cert-interface CsrAttribute--><!--Device-cert-interface CsrAttribute-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

## type

```TypeScript
type: string
```

Attribute type defined in PKCS #9.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CsrAttribute-type: string--><!--Device-CsrAttribute-type: string-End-->

**System capability:** SystemCapability.Security.Cert

## value

```TypeScript
value: string
```

Attribute value.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CsrAttribute-value: string--><!--Device-CsrAttribute-value: string-End-->

**System capability:** SystemCapability.Security.Cert

