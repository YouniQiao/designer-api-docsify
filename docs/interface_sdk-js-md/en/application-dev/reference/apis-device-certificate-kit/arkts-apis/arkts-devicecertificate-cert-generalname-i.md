# GeneralName

Represents an X.509 GeneralName as defined in RFC 5280, which can appear in Subject Alternative Name and other extensions.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-cert-interface GeneralName--><!--Device-cert-interface GeneralName-End-->

**System capability:** SystemCapability.Security.Cert

## name

```TypeScript
name?: Uint8Array
```

DER-encoded value of the GeneralName.

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

Type of the GeneralName.

**Type:** GeneralNameType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GeneralName-type: GeneralNameType--><!--Device-GeneralName-type: GeneralNameType-End-->

**System capability:** SystemCapability.Security.Cert

