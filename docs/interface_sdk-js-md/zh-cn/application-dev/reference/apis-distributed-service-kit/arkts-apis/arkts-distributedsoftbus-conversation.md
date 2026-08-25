# @ohos.distributedSoftBus.conversation(跨设备唤醒与消息传输)

分布式软总线conversation模块为应用提供跨设备交互能力，包括获取可信设备列表、发送和接收会话数据。通过本模块， 应用可以获取同一账号下的可信设备，注册监听器以接收跨设备数据，并通过会话通道向指定设备发送数据。适用于需要跨设备协作和 多设备数据传递的场景，可降低跨设备交互的开发复杂度。

> **说明：**&gt;
> 本模块接口为系统接口，仅可在Stage模型下使用。

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.SoftBus.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getTrustedDevices(跨设备唤醒与消息传输)](arkts-distributedservice-conversation-gettrusteddevices-f-sys.md) |
| [postConversationData(跨设备唤醒与消息传输)](arkts-distributedservice-conversation-postconversationdata-f-sys.md) |
| [registerConversationListener(跨设备唤醒与消息传输)](arkts-distributedservice-conversation-registerconversationlistener-f-sys.md) |
| [unregisterConversationListener(跨设备唤醒与消息传输)](arkts-distributedservice-conversation-unregisterconversationlistener-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceNodeInfo(跨设备唤醒与消息传输)](arkts-distributedservice-conversation-devicenodeinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [DataCallback(跨设备唤醒与消息传输)](arkts-distributedservice-conversation-datacallback-t-sys.md) |
<!--DelEnd-->
