# SetPropertyRequest (System API)

提供设置属性请求的信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface SetPropertyRequest--><!--Device-osAccount-interface SetPropertyRequest-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## authType

```TypeScript
authType: AuthType
```

身份验证凭据类型。

**Type:** [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SetPropertyRequest-authType: AuthType--><!--Device-SetPropertyRequest-authType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## key

```TypeScript
key: SetPropertyType
```

指示要设置的属性类型。

**Type:** [SetPropertyType](arkts-basicservices-osaccount-setpropertytype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SetPropertyRequest-key: SetPropertyType--><!--Device-SetPropertyRequest-key: SetPropertyType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## setInfo

```TypeScript
setInfo: Uint8Array
```

指示要设置的信息。

**Type:** Uint8Array

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SetPropertyRequest-setInfo: Uint8Array--><!--Device-SetPropertyRequest-setInfo: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

