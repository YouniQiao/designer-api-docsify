# ChannelStateInfo

Represents the connection state information of the proxy channel.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-proxyChannelManager-interface ChannelStateInfo--><!--Device-proxyChannelManager-interface ChannelStateInfo-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## channelId

```TypeScript
channelId: int
```

Proxy channel ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelStateInfo-channelId: int--><!--Device-ChannelStateInfo-channelId: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## state

```TypeScript
state: ChannelState
```

Connection state of the proxy channel.

**Type:** [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelStateInfo-state: ChannelState--><!--Device-ChannelStateInfo-state: ChannelState-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

