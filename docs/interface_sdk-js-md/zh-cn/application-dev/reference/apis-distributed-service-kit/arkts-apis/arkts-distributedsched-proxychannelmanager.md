# @ohos.distributedsched.proxyChannelManager(代理通道管理)

###### 使用说明
 调用模块接口前，需要完成如下配置：
 1. 申请ohos.permission.ACCESS_BLUETOOTH权限。如何配置和申请权限，具体操作请参考[声明权限](../../../security/AccessToken/declare-permissions.md)和[向用户申请授权](../../../security/AccessToken/request-user-authorization.md)。
 2. 在module.json5文件中配置action字段"action.ohos.pull.listener"，用于需要被代理拉起的手机侧应用进程。
 典型调用流程：
 1. 调用openProxyChannel打开代理通道，获取channelId。
 2. 调用sendData发送数据，并根据业务需求订阅事件：调用on('receiveData')接收对端数据，调用on('channelStateChange')感知通道连接状态变化（断连、恢复等）。两者可同时订阅，建议在数据传输场景中同时使用，以便通道异常时及时暂停发送并处理断连恢复逻辑。
 3. 使用完毕后，调用off('receiveData')/off('channelStateChange')取消订阅。
 4. 调用closeProxyChannel关闭代理通道释放资源。


**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 导入模块

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [closeProxyChannel(代理通道管理)](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md) |
| [off(代理通道管理)](arkts-distributedservice-proxychannelmanager-off-f.md#offreceivedata) |
| [off(代理通道管理)](arkts-distributedservice-proxychannelmanager-off-f.md#offchannelstatechange) |
| [offChannelStateChange(代理通道管理)](arkts-distributedservice-proxychannelmanager-offchannelstatechange-f.md) |
| [offReceiveData(代理通道管理)](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md) |
| [on(代理通道管理)](arkts-distributedservice-proxychannelmanager-on-f.md#onreceivedata) |
| [on(代理通道管理)](arkts-distributedservice-proxychannelmanager-on-f.md#onchannelstatechange) |
| [onChannelStateChange(代理通道管理)](arkts-distributedservice-proxychannelmanager-onchannelstatechange-f.md) |
| [onReceiveData(代理通道管理)](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md) |
| [openProxyChannel(代理通道管理)](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) |
| [sendData(代理通道管理)](arkts-distributedservice-proxychannelmanager-senddata-f.md) |

### 接口

| 名称 |
| --- |
| [ChannelInfo(代理通道管理)](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) |
| [ChannelStateInfo(代理通道管理)](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md) |
| [DataInfo(代理通道管理)](arkts-distributedservice-proxychannelmanager-datainfo-i.md) |

### 枚举

| 名称 |
| --- |
| [ChannelState(代理通道管理)](arkts-distributedservice-proxychannelmanager-channelstate-e.md) |
| [LinkType(代理通道管理)](arkts-distributedservice-proxychannelmanager-linktype-e.md) |
