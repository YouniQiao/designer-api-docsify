# createLocalWantAgent（系统接口）

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## createLocalWantAgent

```TypeScript
function createLocalWantAgent(info: LocalWantAgentInfo): WantAgent
```

创建本地WantAgent实例。

> **说明：**
> 本接口创建的本地WantAgent实例仅存储于WantAgent客户端，不受WantAgent服务端管理。使用该本地实例时，需要校验实例，以保证安全性。
> 本地WantAgent实例创建后，触发方法参见[wantAgent.triggerAsync](arkts-ability-wantagent-triggerasync-f-sys.md)接口说明。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [LocalWantAgentInfo](arkts-ability-wantagent-localwantagentinfo-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [WantAgent](arkts-ability-wantagent-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
