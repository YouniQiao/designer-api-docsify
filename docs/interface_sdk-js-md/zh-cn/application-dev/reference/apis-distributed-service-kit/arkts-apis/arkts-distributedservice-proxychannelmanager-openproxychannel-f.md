# openProxyChannel

## 导入模块

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## openProxyChannel

```TypeScript
function openProxyChannel(channelInfo: ChannelInfo): Promise<number>
```

打开代理通道，使用Promise异步回调。基于ChannelInfo中配置的链路类型和对端设备信息，通过蓝牙BR协议与对端设备协商建立双向数据通道，并返回唯一标识该通道的channelId。适用于手机侧应用需要与穿戴设备侧应用建立 双向数据通道的场景，例如消息通知转发等。调用此方法后，必须在不再使用代理通道时调用[closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md)关闭通道以释放资源。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| channelInfo | [ChannelInfo](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [32390001](../errorcode-proxyChannelManager.md#32390001-蓝牙已关闭) |
| [32390002](../errorcode-proxyChannelManager.md#32390002-设备未配对) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-参数错误) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-内部异常) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-调用受限) |
| [32390102](../errorcode-proxyChannelManager.md#32390102-操作失败或者连接超时) |
