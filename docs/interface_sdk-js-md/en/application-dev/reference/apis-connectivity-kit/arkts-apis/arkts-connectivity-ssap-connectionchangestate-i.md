# ConnectionChangeState

Describes SSAP connection state.

**Since:** 26.0.0

<!--Device-ssap-interface ConnectionChangeState--><!--Device-ssap-interface ConnectionChangeState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Indicates the device address.The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionChangeState-address: string--><!--Device-ConnectionChangeState-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: ConnectionState
```

Connection state.

**Type:** ConnectionState

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionChangeState-state: ConnectionState--><!--Device-ConnectionChangeState-state: ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

