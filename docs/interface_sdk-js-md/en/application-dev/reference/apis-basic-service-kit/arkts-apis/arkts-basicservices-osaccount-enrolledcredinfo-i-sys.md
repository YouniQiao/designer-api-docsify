# EnrolledCredInfo (System API)

Defines enrolled credential information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface EnrolledCredInfo--><!--Device-osAccount-interface EnrolledCredInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## authSubType

```TypeScript
authSubType: AuthSubType
```

Authentication credential subtype.

**Type:** [AuthSubType](arkts-basicservices-osaccount-authsubtype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-EnrolledCredInfo-authSubType: AuthSubType--><!--Device-EnrolledCredInfo-authSubType: AuthSubType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authType

```TypeScript
authType: AuthType
```

Authentication credential type.

**Type:** AuthType

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-EnrolledCredInfo-authType: AuthType--><!--Device-EnrolledCredInfo-authType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credentialId

```TypeScript
credentialId: Uint8Array
```

Credential ID, which is left blank by default.

**Type:** Uint8Array

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-EnrolledCredInfo-credentialId: Uint8Array--><!--Device-EnrolledCredInfo-credentialId: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## isAbandoned

```TypeScript
isAbandoned?: boolean
```

Whether the credential is abandoned. The abandoned credential may be stored as a backup credential for a period of time. The value **true** indicates that the credential is abandoned, and the value **false** indicates the opposite. The default value is **undefined**.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EnrolledCredInfo-isAbandoned?: boolean--><!--Device-EnrolledCredInfo-isAbandoned?: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## templateId

```TypeScript
templateId: Uint8Array
```

Authentication credential template ID.

**Type:** Uint8Array

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-EnrolledCredInfo-templateId: Uint8Array--><!--Device-EnrolledCredInfo-templateId: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## validityPeriod

```TypeScript
validityPeriod?: long
```

Credential validity period, in milliseconds. The default value is **undefined**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EnrolledCredInfo-validityPeriod?: long--><!--Device-EnrolledCredInfo-validityPeriod?: long-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

