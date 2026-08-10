# GetPropertyRequest (System API)

提供获取属性请求的信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface GetPropertyRequest--><!--Device-osAccount-interface GetPropertyRequest-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId?: int
```

系统账号标识，默认为undefined。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GetPropertyRequest-accountId?: int--><!--Device-GetPropertyRequest-accountId?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authType

```TypeScript
authType: AuthType
```

身份验证凭据类型。

**Type:** [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GetPropertyRequest-authType: AuthType--><!--Device-GetPropertyRequest-authType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## keys

```TypeScript
keys: Array<GetPropertyType>
```

指示要获取的属性类型数组。

**Type:** Array&lt;GetPropertyType&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GetPropertyRequest-keys: Array<GetPropertyType>--><!--Device-GetPropertyRequest-keys: Array<GetPropertyType>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

