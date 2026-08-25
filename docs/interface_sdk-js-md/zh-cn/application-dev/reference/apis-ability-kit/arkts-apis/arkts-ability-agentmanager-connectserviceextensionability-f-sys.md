# connectServiceExtensionAbility（系统接口）

## 导入模块

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## connectServiceExtensionAbility

```TypeScript
function connectServiceExtensionAbility(context: AgentExtensionContext, want: Want, callback: ConnectOptions): long
```

将AgentExtensionAbility连接到ServiceExtensionAbility。若目标ServiceExtensionAbility可见，可直接连接；若不可见，需申请 `ohos.permission.START_INVISIBLE_ABILITY`权限；若目标ServiceExtensionAbility位于远程设备上，需申请 `ohos.permission.DISTRIBUTED_DATASYNC`权限。

> **说明：**&gt;
> 该接口不支持在多线程和子进程中调用。在多线程中调用将引发CppCrash；在子进程中调用将返回16000050错误码。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [AgentExtensionContext](arkts-ability-agentextensioncontext-c.md) | 是 |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
