# OsAccountSubProfile (System API)

Definition of an OS account sub-profile.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-osAccount-interface OsAccountSubProfile--><!--Device-osAccount-interface OsAccountSubProfile-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## createTime

```TypeScript
createTime: long
```

Time when the sub-profile was created.Unit: milliseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfile-createTime: long--><!--Device-OsAccountSubProfile-createTime: long-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## distributedInfo

```TypeScript
distributedInfo?: distributedAccount.DistributedInfo
```

Distributed account information bound to the OS account sub-profile.

**Type:** distributedAccount.DistributedInfo

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfile-distributedInfo?: distributedAccount.DistributedInfo--><!--Device-OsAccountSubProfile-distributedInfo?: distributedAccount.DistributedInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## id

```TypeScript
id: int
```

Identifier of the OS account sub-profile.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfile-id: int--><!--Device-OsAccountSubProfile-id: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## index

```TypeScript
index: int
```

Position index of the OS account sub-profile, ranging from 0 to the number of sub-profiles minus 1.This index is unique within each OS account and is automatically assigned by the system when the sub-profile is created.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfile-index: int--><!--Device-OsAccountSubProfile-index: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## osAccountLocalId

```TypeScript
osAccountLocalId: int
```

Local ID of the OS account to which the sub-profile belongs.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfile-osAccountLocalId: int--><!--Device-OsAccountSubProfile-osAccountLocalId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

