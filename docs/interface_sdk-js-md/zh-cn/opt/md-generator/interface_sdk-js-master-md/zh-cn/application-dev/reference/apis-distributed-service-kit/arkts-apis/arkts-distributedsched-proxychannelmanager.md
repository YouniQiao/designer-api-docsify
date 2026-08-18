# @ohos.distributedsched.proxyChannelManager

软总线具备常驻运行能力，可为跨设备通信提供稳定可靠的底层通道。本模块基于软总线进程开发，支持手机与穿戴设备间的数据互通，可为用户提供无缝的设备互联体验，同时降低开发者跨设备通信的实现复杂度，无需自行处理底层通信协议和进程唤醒逻辑。使用 场景：手机侧应用与穿戴设备侧应用协同时，当手机侧应用不在前台时，手机侧应用的下行消息经由通知服务器，通过代理模块发送给穿戴设备侧；当穿戴设备向手机发送数据时，代理模块可动态唤醒手机侧对应应用进程以接收和处理数据。模块核心功能包括：代理 通道管理、数据路由管理、应用状态感知和唤醒、全链路状态监控。 - 代理通道管理：通过蓝牙 BR 协议建立手机与穿戴设备的双向数据通道，确保跨设备间可靠的双向数据通信，无需开发者自行实现底层通信协议。支持的数据通道ID范围是1~2147483647。 - 数据路由管理：基于 UUID 服务识别机制转发穿戴设备侧应用数据，实现数据的精准路由至目标服务端口，避免数据丢失或错发。UUID用于唯一标识对端设备上监听的服务，代理模块根据对端设备的UUID将数据路由至对应服务端口。 - 应用状态感知和唤醒：代理通道使能并收到穿戴设备侧应用数据后，代理模块根据module.json5中配置的action字段（如'action.ohos.pull.listener'）识别目标应用，并代理拉起对应手机侧应用进程以处理数 据，无需应用常驻前台即可接收数据，节省系统资源。 - 全链路状态监控：通过回调实时感知代理通道全生命周期的连接状态变化，帮助手机侧应用及时响应连接异常并调整业务策略，提升数据传输可靠性。包括连接恢复、异常断连、配对关系删除等事件。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace proxyChannelManager--><!--Device-unnamed-declare namespace proxyChannelManager-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
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
