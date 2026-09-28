# EthEapStateInfo

```TypeScript
interface EthEapStateInfo
```

Represents the 802.1X EAP authentication state information, delivered via the stateChange callback.

**Since:** 26.2.0

**System capability:** SystemCapability.Communication.NetManager.Eap

## Modules to Import

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## message

```TypeScript
message?: string
```

Supplementary message, such as the failure reason. Empty on success.

**Type:** string

**Since:** 26.2.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Eap

## retryCount

```TypeScript
retryCount: number
```

Current retry count (resets to 0 on success). The value should be an integer.

**Type:** number

**Since:** 26.2.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Eap

## state

```TypeScript
state: EthEapState
```

Current authentication state.

**Type:** [EthEapState](arkts-network-eap-etheapstate-e.md)

**Since:** 26.2.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Eap
