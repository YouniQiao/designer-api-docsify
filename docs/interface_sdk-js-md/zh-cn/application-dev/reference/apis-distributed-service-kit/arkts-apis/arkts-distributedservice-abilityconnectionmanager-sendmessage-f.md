# sendMessage

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## sendMessage

```TypeScript
function sendMessage(sessionId: number, msg: string): Promise<void>
```

创建协同会话成功并获得会话ID、调用connect接口建立连接成功后，设备A或设备B可向对端设备发送文本信息。 使用Promise异步回调。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| msg | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
