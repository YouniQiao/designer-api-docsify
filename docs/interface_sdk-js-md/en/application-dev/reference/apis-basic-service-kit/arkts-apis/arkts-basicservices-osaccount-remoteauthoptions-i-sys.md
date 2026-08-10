# RemoteAuthOptions (System API)

表示远程认证的可选参数集合。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface RemoteAuthOptions--><!--Device-osAccount-interface RemoteAuthOptions-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## collectorNetworkId

```TypeScript
collectorNetworkId?: string
```

凭据收集者的网络标识，默认为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RemoteAuthOptions-collectorNetworkId?: string--><!--Device-RemoteAuthOptions-collectorNetworkId?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## collectorTokenId

```TypeScript
collectorTokenId?: int
```

凭据收集者的令牌标识，默认为undefined。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RemoteAuthOptions-collectorTokenId?: int--><!--Device-RemoteAuthOptions-collectorTokenId?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## verifierNetworkId

```TypeScript
verifierNetworkId?: string
```

凭据验证者的网络标识，默认为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RemoteAuthOptions-verifierNetworkId?: string--><!--Device-RemoteAuthOptions-verifierNetworkId?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

