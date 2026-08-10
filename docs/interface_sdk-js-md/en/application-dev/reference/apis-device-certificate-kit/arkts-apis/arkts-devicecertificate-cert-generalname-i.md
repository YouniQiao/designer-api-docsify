# GeneralName

表示X.509 GeneralName，定义在RFC 5280中，可出现在Subject Alternative Name等扩展中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-cert-interface GeneralName--><!--Device-cert-interface GeneralName-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## name

```TypeScript
name?: Uint8Array
```

指定GeneralName的DER编码值。

**Type:** Uint8Array

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GeneralName-name?: Uint8Array--><!--Device-GeneralName-name?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## type

```TypeScript
type: GeneralNameType
```

GeneralName类型。

**Type:** [GeneralNameType](arkts-devicecertificate-cert-generalnametype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GeneralName-type: GeneralNameType--><!--Device-GeneralName-type: GeneralNameType-End-->

**System capability:** SystemCapability.Security.Cert

