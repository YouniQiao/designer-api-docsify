# @ohos.distributedsched.proxyChannelManager

软总线具备常驻运行能力，可为跨设备通信提供稳定可靠的底层通道。本模块基于软总线进程开发，支持手机与穿戴设备间高效的数据互通， 可为用户提供无缝的设备互联体验。使用场景：手机侧APP与手表侧APP协同时，当手机APP不在前台被使用，手机应 用的下行消息经由通知服务器，通过代理模块发送给手表侧。模块核心功能包括：代理通道管理、数据路由管理、 应用状态感知和唤醒、 链路状态监听。 - 代理通道管理：通过蓝牙 BR 协议建立手机与穿戴设备的双向数据通道，支持的数据通道 ID 范围是[1,2147483647] 。 - 数据路由管理：基于 UUID 服务识别机制，精准转发穿戴设备数据。 - 应用状态感知和唤醒：代理通道使能后，收到穿戴设备发送的数据后，动态分析和唤醒手机端对应应用进程。 - 全链路状态监控：通过回调实时感知通道连接状态。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace proxyChannelManager--><!--Device-unnamed-declare namespace proxyChannelManager-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 汇总

### 函数

| 名称 |
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

### 接口

| 名称 |
| --- |
| [ChannelInfo](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) |
| [ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md) |
| [DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md) |

### 枚举

| 名称 |
| --- |
| [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md) |
| [LinkType](arkts-distributedservice-proxychannelmanager-linktype-e.md) |
