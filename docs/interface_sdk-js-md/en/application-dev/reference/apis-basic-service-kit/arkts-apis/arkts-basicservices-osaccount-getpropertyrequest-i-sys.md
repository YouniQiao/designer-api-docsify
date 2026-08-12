# GetPropertyRequest (System API)

Defines the request for obtaining property information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface GetPropertyRequest--><!--Device-osAccount-interface GetPropertyRequest-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId?: int
```

OS account ID, which is **undefined** by default.

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

Authentication credential type.

**Type:** AuthType

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GetPropertyRequest-authType: AuthType--><!--Device-GetPropertyRequest-authType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## keys

```TypeScript
keys: Array<GetPropertyType>
```

An array of the types of the properties to obtain.

**Type:** Array&lt;[GetPropertyType](arkts-basicservices-osaccount-getpropertytype-e-sys.md)&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GetPropertyRequest-keys: Array<GetPropertyType>--><!--Device-GetPropertyRequest-keys: Array<GetPropertyType>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

