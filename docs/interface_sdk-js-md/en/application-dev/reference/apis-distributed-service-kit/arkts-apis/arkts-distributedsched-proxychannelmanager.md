# @ohos.distributedsched.proxyChannelManager

DSoftBus provides stable and reliable underlying channels for cross-device communication. This module is developed based on DSoftBus. It supports efficient data exchange between phones and wearables, providing users with a seamless device interconnection experience. During collaboration between the phone application and watch application, if the phone application is not running in the foreground, its downlink messages are forwarded to the notification server and then sent to the watch through the proxy module. The core functions of this module include proxy channel management, data route management, application state awareness and wakeup, and link state monitoring. - Proxy channel management: Manages bidirectional data channels established between phones and wearables via the Bluetooth Basic Rate (BR) protocol. - Data route management: Accurately forwards data of wearables based on the specified service UUID. - Application state awareness and wakeup: After a proxy channel is enabled, dynamically analyzes and wakes up the corresponding application process on the phone after receiving data sent by the wearable. - Link state monitoring: Monitors the channel connection state in real time through callback.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

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

| Name | Description |
| --- | --- |
| [closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md#closeProxyChannel) | Closes a proxy channel that has been opened. |
| [offChannelStateChange](arkts-distributedservice-proxychannelmanager-offchannelstatechange-f.md#offChannelStateChange) | Unsubscribes from channel state change events. |
| [offReceiveData](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md#offReceiveData) | Unsubscribes from data receiving events. |
| off_channelStateChange | Unsubscribes from channel state change events. |
| off_receiveData | Unsubscribes from data receiving events. |
| [onChannelStateChange](arkts-distributedservice-proxychannelmanager-onchannelstatechange-f.md#onChannelStateChange) | Subscribes to channel state change events. This API returns the result asynchronously through a callback. |
| [onReceiveData](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md#onReceiveData) | Subscribes to data receiving events. This API returns the result asynchronously through a callback. |
| on_channelStateChange | Subscribes to channel state change events. This API returns the result asynchronously through a callback. |
| on_receiveData | Subscribes to data receiving events. This API returns the result asynchronously through a callback. |
| [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openProxyChannel) | Opens a proxy channel. This API uses a promise to return the result. |
| [sendData](arkts-distributedservice-proxychannelmanager-senddata-f.md#sendData) | Sends data to the peer end. This API uses a promise to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [ChannelInfo](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) | Represents the proxy channel information, including the MAC address and service UUID of the peer device. |
| [ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md) | Represents the connection state information of the proxy channel. |
| [DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md) | Represents the received data, including the channel ID and data. |

### Enums

| Name | Description |
| --- | --- |
| [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md) | Enumerates the connection states of the proxy channel. |
| [LinkType](arkts-distributedservice-proxychannelmanager-linktype-e.md) | Enumerates the link types. |

