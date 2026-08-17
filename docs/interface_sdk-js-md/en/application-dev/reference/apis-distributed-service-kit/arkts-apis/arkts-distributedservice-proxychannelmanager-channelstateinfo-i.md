# ChannelStateInfo

Represents the connection state information of the proxy channel.

**Since:** 23

<!--Device-proxyChannelManager-interface ChannelStateInfo--><!--Device-proxyChannelManager-interface ChannelStateInfo-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'proxyChannelManager';
```

## channelId

```TypeScript
channelId: int
```

Channel ID of the proxy channel. The value range is 1 to 2147483647.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelStateInfo-channelId: int--><!--Device-ChannelStateInfo-channelId: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## state

```TypeScript
state: ChannelState
```

Connection state of the channel. For the value range, see [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md#channelstate). You are advised to adjust service policies based on different state values, for example, suspending data transmission when the channel is disconnected and retrying services after the channel is restored.

**Type:** [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelStateInfo-state: ChannelState--><!--Device-ChannelStateInfo-state: ChannelState-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

