# restoreAllPolicies（系统接口）

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## restoreAllPolicies

```TypeScript
function restoreAllPolicies(iccid: string): Promise<void>
```

根据指定的SIM卡识别码，恢复所有网络管理相关的策略配置，如UID策略、配额策略、防火墙规则等。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iccid | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
