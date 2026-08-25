# ChannelStateInfo

Represents the connection state information of the proxy channel.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## channelId

```TypeScript
channelId: int
```

Channel ID of the proxy channel. The value range is 1 to 2147483647.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## state

```TypeScript
state: ChannelState
```

Connection state of the channel. For the value range, see [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md). You are advised to adjust service policies based on different state values, for example, suspending data transmission when the channel is disconnected and retrying services after the channel is restored.

**Type:** [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration
