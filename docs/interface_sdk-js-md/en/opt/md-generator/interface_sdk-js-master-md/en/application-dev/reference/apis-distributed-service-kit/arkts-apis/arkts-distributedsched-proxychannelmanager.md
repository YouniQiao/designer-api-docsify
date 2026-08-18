# @ohos.distributedsched.proxyChannelManager

DSoftBus provides stable and reliable underlying channels for cross-device communication. This module is developed based on DSoftBus. It supports data exchange between phones and wearables, providing users with a seamless device interconnection experience. It also simplifies cross-device communication for developers, eliminating the need to handle underlying communication protocols and process wakeup logic. Use scenarios: During collaboration between the phone app and wearable app, if the phone app is not running in the foreground, its downlink messages are forwarded to the notification server and then sent to the wearable through the proxy module. When the wearable sends data to the phone, the proxy module can dynamically wake up the corresponding app process on the phone to receive and process the data. The core functions of this module include proxy channel management, data route management, application state awareness and wakeup, and link state monitoring. - Proxy channel management: Manages bidirectional data channels established between phones and wearables via the Bluetooth Basic Rate (BR) protocol. This ensures reliable cross-device data communication without the need to implement the underlying communication protocol. The supported data channel IDs range from 1 to 2147483647. - Data route management: Accurately forwards data of wearables based on the specified service UUID. This accurately routes data to the target service port, preventing data loss or incorrect data transmission. The UUID uniquely identifies the service listened for the peer device. The proxy module routes data to the corresponding service port based on the UUID of the peer device. - Application state awareness and wakeup: After a proxy channel is enabled and data sent by the wearable is received, the proxy module identifies the target app based on the **action** field (for example, **action.ohos.pull.listener**) configured in the **module.json5** file, and starts the corresponding app process on the phone to process the data. This allows the app to receive data without having to stay in the foreground, thereby saving system resources. - Link state monitoring: Monitors the connection status changes of the proxy channel throughout its lifecycle in real time through callbacks. This helps the phone app respond to connection exceptions in a timely manner and adjust service policies, thereby improving data transmission reliability.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace proxyChannelManager--><!--Device-unnamed-declare namespace proxyChannelManager-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md#closeproxychannel) |
| [offChannelStateChange](arkts-distributedservice-proxychannelmanager-offchannelstatechange-f.md#offchannelstatechange) |
| [offReceiveData](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md#offreceivedata) |
| [off_channelStateChange](arkts-distributedservice-proxychannelmanager-offchannelstatechange-f.md#offchannelstatechange) |
| [off_receiveData](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md#offreceivedata) |
| [onChannelStateChange](arkts-distributedservice-proxychannelmanager-onchannelstatechange-f.md#onchannelstatechange) |
| [onReceiveData](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md#onreceivedata) |
| [on_channelStateChange](arkts-distributedservice-proxychannelmanager-onchannelstatechange-f.md#onchannelstatechange) |
| [on_receiveData](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md#onreceivedata) |
| [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openproxychannel) |
| [sendData](arkts-distributedservice-proxychannelmanager-senddata-f.md#senddata) |

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
