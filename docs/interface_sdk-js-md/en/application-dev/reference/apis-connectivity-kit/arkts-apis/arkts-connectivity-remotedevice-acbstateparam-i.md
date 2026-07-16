# AcbStateParam

ACB connection status parameter.

**Since:** 26.0.0

<!--Device-remoteDevice-interface AcbStateParam--><!--Device-remoteDevice-interface AcbStateParam-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Indicates the device address.The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcbStateParam-address: string--><!--Device-AcbStateParam-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: AcbState
```

ACB connection status.

**Type:** AcbState

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AcbStateParam-state: AcbState--><!--Device-AcbStateParam-state: AcbState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

