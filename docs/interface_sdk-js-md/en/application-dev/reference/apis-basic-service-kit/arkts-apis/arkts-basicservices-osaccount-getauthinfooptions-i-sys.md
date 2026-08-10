# GetAuthInfoOptions (System API)

表示[查询认证凭据信息](arkts-basicservices-osaccount-useridentitymanager-c-sys.md#getauthinfo)的可选参数集合。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface GetAuthInfoOptions--><!--Device-osAccount-interface GetAuthInfoOptions-End-->

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

<!--Device-GetAuthInfoOptions-accountId?: int--><!--Device-GetAuthInfoOptions-accountId?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authType

```TypeScript
authType?: AuthType
```

认证类型，默认为undefined。

**Type:** [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GetAuthInfoOptions-authType?: AuthType--><!--Device-GetAuthInfoOptions-authType?: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

