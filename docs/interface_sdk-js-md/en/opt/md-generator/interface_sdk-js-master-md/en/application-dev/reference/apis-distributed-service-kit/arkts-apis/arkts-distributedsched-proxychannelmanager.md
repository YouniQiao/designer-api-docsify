# @ohos.distributedsched.proxyChannelManager

DSoftBus provides stable and reliable underlying channels for cross-device communication. This module is developed based on DSoftBus. It supports efficient data exchange between phones and wearables, providing users with a seamless device interconnection experience. During collaboration between the phone application and watch application, if the phone application is not running in the foreground, its downlink messages are forwarded to the notification server and then sent to the watch through the proxy module. The core functions of this module include proxy channel management, data route management, application state awareness and wakeup, and link state monitoring. - Proxy channel management: Manages bidirectional data channels established between phones and wearables via the Bluetooth Basic Rate (BR) protocol. - Data route management: Accurately forwards data of wearables based on the specified service UUID. - Application state awareness and wakeup: After a proxy channel is enabled, dynamically analyzes and wakes up the corresponding application process on the phone after receiving data sent by the wearable. - Link state monitoring: Monitors the channel connection state in real time through callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace proxyChannelManager--><!--Device-unnamed-declare namespace proxyChannelManager-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md#closeProxyChannel) |
| [offChannelStateChange](arkts-distributedservice-proxychannelmanager-offchannelstatechange-f.md#offChannelStateChange) |
| [offReceiveData](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md#offReceiveData) |
| [off_channelStateChange](arkts-distributedservice-proxychannelmanager-offchannelstatechange-f.md) |
| off_receiveData |
| [onChannelStateChange](arkts-distributedservice-proxychannelmanager-onchannelstatechange-f.md#onChannelStateChange) |
| [onReceiveData](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md#onReceiveData) |
| [on_channelStateChange](arkts-distributedservice-proxychannelmanager-onchannelstatechange-f.md) |
| on_receiveData |
| [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openProxyChannel) |
| [sendData](arkts-distributedservice-proxychannelmanager-senddata-f.md#sendData) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ChannelInfo](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) |
| [ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md) |
| [DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md) |
| [LinkType](arkts-distributedservice-proxychannelmanager-linktype-e.md) |
