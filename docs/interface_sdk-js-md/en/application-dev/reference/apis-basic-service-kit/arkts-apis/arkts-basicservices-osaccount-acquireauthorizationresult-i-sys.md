# AcquireAuthorizationResult (System API)

表示获取授权的结果。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-osAccount-interface AcquireAuthorizationResult--><!--Device-osAccount-interface AcquireAuthorizationResult-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## isReused

```TypeScript
isReused?: boolean
```

是否为复用的授权结果，默认为undefined。

true：表示是复用的授权结果。false：表示不是复用的授权结果。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcquireAuthorizationResult-isReused?: boolean--><!--Device-AcquireAuthorizationResult-isReused?: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## privilege

```TypeScript
privilege: string
```

与授权关联的权限。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcquireAuthorizationResult-privilege: string--><!--Device-AcquireAuthorizationResult-privilege: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## resultCode

```TypeScript
resultCode: AuthorizationResultCode
```

授权结果码。

**Type:** [AuthorizationResultCode](arkts-basicservices-osaccount-authorizationresultcode-e-sys.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcquireAuthorizationResult-resultCode: AuthorizationResultCode--><!--Device-AcquireAuthorizationResult-resultCode: AuthorizationResultCode-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## token

```TypeScript
token?: Uint8Array
```

授权令牌，默认为undefined。

**Type:** Uint8Array

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcquireAuthorizationResult-token?: Uint8Array--><!--Device-AcquireAuthorizationResult-token?: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## validityPeriod

```TypeScript
validityPeriod?: int
```

授权的有效期，默认值为300，单位为s。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcquireAuthorizationResult-validityPeriod?: int--><!--Device-AcquireAuthorizationResult-validityPeriod?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

