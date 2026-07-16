# NetworkAccessPolicy (System API)

Network policies that limit the specified UID of application to access the network.

**Since:** 12

<!--Device-policy-export interface NetworkAccessPolicy--><!--Device-policy-export interface NetworkAccessPolicy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## allowCellular

```TypeScript
allowCellular?: boolean
```

Indicate whether the application can be allowed to access the network by cellular.

**Type:** boolean

**Since:** 12

<!--Device-NetworkAccessPolicy-allowCellular?: boolean--><!--Device-NetworkAccessPolicy-allowCellular?: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## allowWiFi

```TypeScript
allowWiFi?: boolean
```

Indicate whether the application can be allowed to access the network by wifi.

**Type:** boolean

**Since:** 12

<!--Device-NetworkAccessPolicy-allowWiFi?: boolean--><!--Device-NetworkAccessPolicy-allowWiFi?: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## alwaysAllowCellular

```TypeScript
alwaysAllowCellular?: boolean
```

Indicate whether the application can be always allowed to access the network by cellular and users cannot set it.

**Type:** boolean

**Since:** 18

<!--Device-NetworkAccessPolicy-alwaysAllowCellular?: boolean--><!--Device-NetworkAccessPolicy-alwaysAllowCellular?: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## alwaysAllowWiFi

```TypeScript
alwaysAllowWiFi?: boolean
```

Indicate whether the application can be always allowed to access the network by wifi and users cannot set it.

**Type:** boolean

**Since:** 18

<!--Device-NetworkAccessPolicy-alwaysAllowWiFi?: boolean--><!--Device-NetworkAccessPolicy-alwaysAllowWiFi?: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

