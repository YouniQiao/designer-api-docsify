# reject

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## reject

```TypeScript
function reject(token: string, reason: string): void
```

在跨端应用协同过程中，在拒绝对端的连接请求后，向对端发送拒绝原因。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | string | 是 |
| reason | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
