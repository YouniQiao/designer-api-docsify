# closeProxyChannel

## 导入模块

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## closeProxyChannel

```TypeScript
function closeProxyChannel(channelId: number): void
```

关闭已打开的代理通道。适用于手机侧应用不再需要与穿戴设备侧应用通信的场景，例如完成数据同步任务后主动释放通道资源等。此方法必须与 [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md)配对使用，在使用完毕后调用此方法关闭通道以释放资源。关闭通道后，已注册的receiveData和 channelStateChange回调将自动取消订阅，正在传输的数据将中断。未及时关闭代理通道可能导致通道资源泄漏。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| channelId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [32390004](../errorcode-proxyChannelManager.md#32390004-通道id非法或者不可用) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-参数错误) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-内部异常) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-调用受限) |
