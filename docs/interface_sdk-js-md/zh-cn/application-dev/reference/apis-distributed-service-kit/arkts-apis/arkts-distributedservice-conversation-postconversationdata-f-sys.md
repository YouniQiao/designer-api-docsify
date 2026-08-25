# postConversationData（系统接口）

## 导入模块

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## postConversationData

```TypeScript
function postConversationData(
    deviceId: string,
    bundleName: string,
    abilityName: string,
    msg: ArrayBuffer
  ): Promise<void>
```

向目标设备发送会话数据。目标设备须为同一账号下的可信设备。以目标设备的networkId或UDID进行设备寻址，数据发送至目标设备上 与指定Bundle名和Ability名匹配的已注册监听应用。典型使用场景包括：跨设备协同指令发送。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.SoftBus.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| bundleName | string | 是 |
| abilityName | string | 是 |
| msg | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2000001](../errorcode-conversation.md#2000001-内部错误) |
| [2004001](../errorcode-conversation.md#2004001-对端设备系统版本过低) |
| [2004002](../errorcode-conversation.md#2004002-对端拉起ability失败) |
| [2004003](../errorcode-conversation.md#2004003-发送数据失败) |
| [2004004](../errorcode-conversation.md#2004004-等待对端确认超时) |
