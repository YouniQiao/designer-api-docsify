# SubscribeInfo (System API)

Represents the subscription information.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface SubscribeInfo--><!--Device-cloudExtension-export interface SubscribeInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from '@kit.ArkData';
```

## expirationTime

```TypeScript
expirationTime: long
```

Subscription expiration time, in ms.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SubscribeInfo-expirationTime: long--><!--Device-SubscribeInfo-expirationTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## subscribe

```TypeScript
subscribe: Record<string, Array<SubscribeId>>
```

Subscription information.

**Type:** Record&lt;string, Array&lt;[SubscribeId](arkts-arkdata-cloudextension-subscribeid-i-sys.md)&gt;&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SubscribeInfo-subscribe: Record<string, Array<SubscribeId>>--><!--Device-SubscribeInfo-subscribe: Record<string, Array<SubscribeId>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

