# Callee

系统为UIAbility创建的后台通信对象，Callee UIAbility（被调用方）可以通过Callee对象接收Caller对象发送的数据。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 导入模块

```TypeScript
import { UIAbility, Callee, CalleeCallback, Caller, OnReleaseCallback, OnRemoteStateChangeCallback } from 'kits/@kit.AbilityKit';
```

## off

```TypeScript
off(method: string): void
```

解除通用组件服务端注册消息通知callback。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| method | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200005](../errorcode-ability.md#16200005-方法未注册) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## on

```TypeScript
on(method: string, callback: CalleeCallback): void
```

通用组件服务端注册消息通知callback。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| method | string | 是 |
| callback | [CalleeCallback](arkts-ability-app-ability-uiability-calleecallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200004](../errorcode-ability.md#16200004-方法已注册) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
