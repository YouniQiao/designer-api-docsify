# acceptConnect

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## acceptConnect

```TypeScript
function acceptConnect(sessionId: number, token: string): Promise<void>
```

设备B上的应用，在创建协同会话成功并获得会话ID后，调用acceptConnect()方法接受连接。 调用此接口前，需先在两端设备分别创建协同会话。必须与设备A的connect方法配合使用： 设备A调用connect会拉起设备B应用，设备B在onCollaborate生命周期中创建会话后调用acceptConnect。 使用Promise异步回调。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
