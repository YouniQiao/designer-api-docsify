# @ohos.distributedsched.proxyChannelManager(Proxy Channel Management)

###### Instructions
 Before calling the APIs of this module, complete the following configurations:
 1. You have requested the **ohos.permission.ACCESS_BLUETOOTH** permission. For details about how to configure and apply for permissions, see [Declaring Permissions](../../../security/AccessToken/declare-permissions.md) and [Requesting User Authorization](../../../security/AccessToken/request-user-authorization.md).
 2. In the **module.json5** file, you have configured the **action** field **action.ohos.pull.listener** for the phone app process that needs to be started by the proxy module.
 The typical calling process is as follows:
 1. Call **openProxyChannel** to open the proxy channel and obtain the channel ID.
 2. Call **sendData** to send data, and subscribe to events based on service requirements. Call **on('receiveData')** to receive data from the peer end, and call **on('channelStateChange')** to monitor channel connection state changes (such as disconnection and recovery). You can subscribe to both events at the same time. It is recommended to use them together in data transmission scenarios so that data sending can be paused promptly and disconnection recovery logic can be handled when the channel is abnormal.
 3. After using the event, call **off('receiveData')** or **off('channelStateChange')** to unsubscribe from the event.
 4. Call **closeProxyChannel** to close the proxy channel and release resources.


**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [closeProxyChannel(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md) |
| [off(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-off-f.md#offreceivedata) |
| [off(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-off-f.md#offchannelstatechange) |
| [on(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-on-f.md#onreceivedata) |
| [on(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-on-f.md#onchannelstatechange) |
| [openProxyChannel(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) |
| [sendData(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-senddata-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ChannelInfo(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) |
| [ChannelStateInfo(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md) |
| [DataInfo(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-datainfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ChannelState(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-channelstate-e.md) |
| [LinkType(Proxy Channel Management)](arkts-distributedservice-proxychannelmanager-linktype-e.md) |
