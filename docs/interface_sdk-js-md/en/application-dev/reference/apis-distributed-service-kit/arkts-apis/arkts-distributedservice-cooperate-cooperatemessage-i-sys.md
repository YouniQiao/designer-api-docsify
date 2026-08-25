# CooperateMessage (System API)

Defines a screen hopping status change event.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## networkId

```TypeScript
networkId: string
```

Descriptor of the target device for screen hopping.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

## state

```TypeScript
state: CooperateState
```

Screen hopping status.

**Type:** [CooperateState](arkts-distributedservice-cooperate-cooperatestate-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.
