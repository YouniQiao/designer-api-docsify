# NetAccessPolicy

Network policies that limit the specified UID of application to access the network.

**Since:** 26.0.0

<!--Device-policy-export interface NetAccessPolicy--><!--Device-policy-export interface NetAccessPolicy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## allowCellular

```TypeScript
allowCellular: boolean
```

Indicate whether the application can be allowed to access the network by cellular.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetAccessPolicy-allowCellular: boolean--><!--Device-NetAccessPolicy-allowCellular: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## allowWiFi

```TypeScript
allowWiFi: boolean
```

Indicate whether the application can be allowed to access the network by wifi.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetAccessPolicy-allowWiFi: boolean--><!--Device-NetAccessPolicy-allowWiFi: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

