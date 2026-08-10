# ChannelStateInfo

当代理通道状态变化时，用于表示代理通道的连接状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-proxyChannelManager-interface ChannelStateInfo--><!--Device-proxyChannelManager-interface ChannelStateInfo-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## channelId

```TypeScript
channelId: int
```

代理通道的channelId。

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

通道的连接状态。

**Type:** [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelStateInfo-state: ChannelState--><!--Device-ChannelStateInfo-state: ChannelState-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

