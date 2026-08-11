# AuthOptions (System API)

Represents a set of optional parameters for  
[auth](arkts-basicservices-osaccount-userauth-c-sys.md#auth).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface AuthOptions--><!--Device-osAccount-interface AuthOptions-End-->

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

OS account ID, which is **undefined** by default.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AuthOptions-accountId?: int--><!--Device-AuthOptions-accountId?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## additionalInfo

```TypeScript
additionalInfo?: string
```

Indicates the additional information about the authentication options.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthOptions-additionalInfo?: string--><!--Device-AuthOptions-additionalInfo?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authIntent

```TypeScript
authIntent?: AuthIntent
```

Authentication intent, which is **undefined** by default.

**Type:** [AuthIntent](arkts-basicservices-osaccount-authintent-e-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AuthOptions-authIntent?: AuthIntent--><!--Device-AuthOptions-authIntent?: AuthIntent-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## remoteAuthOptions

```TypeScript
remoteAuthOptions?: RemoteAuthOptions
```

Remote authentication options, which is **undefined** by default.

**Type:** [RemoteAuthOptions](arkts-basicservices-osaccount-remoteauthoptions-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AuthOptions-remoteAuthOptions?: RemoteAuthOptions--><!--Device-AuthOptions-remoteAuthOptions?: RemoteAuthOptions-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

