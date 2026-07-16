# ChannelInfo

Represents the proxy channel information, including the MAC address and service UUID of the peer device.

**Since:** 20

<!--Device-proxyChannelManager-interface ChannelInfo--><!--Device-proxyChannelManager-interface ChannelInfo-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## linkType

```TypeScript
linkType: LinkType
```

Link type of the proxy channel.

**Type:** LinkType

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelInfo-linkType: LinkType--><!--Device-ChannelInfo-linkType: LinkType-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## peerDevAddr

```TypeScript
peerDevAddr: string
```

MAC address of the peer device.

**Type:** string

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelInfo-peerDevAddr: string--><!--Device-ChannelInfo-peerDevAddr: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## peerUuid

```TypeScript
peerUuid: string
```

Service UUID of the peer device.

**Type:** string

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelInfo-peerUuid: string--><!--Device-ChannelInfo-peerUuid: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

