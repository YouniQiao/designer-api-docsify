# unregisterConversationListener（系统接口）

## 导入模块

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## unregisterConversationListener

```TypeScript
function unregisterConversationListener(bundleName: string, abilityName: string): void
```

注销指定Bundle名和Ability名的会话监听。需与注册监听器 [registerConversationListener](arkts-distributedservice-conversation-registerconversationlistener-f-sys.md)配对使用，用于注销已注册的会话监听器。 在不再需要接收消息时应调用注销监听器以释放资源，未注销会导致资源持续占用。同一Bundle名和Ability名只能注册一个监听器， 重复注册会覆盖之前的监听器，注销后将移除当前生效的监听器。调用此接口后，应用将不再接收对应Bundle名和Ability名的会话数据。 如果之前未注册过指定Bundle名和Ability名的监听器，此接口同样返回成功。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.SoftBus.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| abilityName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2000001](../errorcode-conversation.md#2000001-内部错误) |
