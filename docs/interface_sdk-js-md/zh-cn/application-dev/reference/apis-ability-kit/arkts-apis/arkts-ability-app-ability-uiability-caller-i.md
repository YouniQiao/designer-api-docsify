# Caller

调用方Caller UIAbility通过[startAbilityByCall](arkts-ability-uiabilitycontext-c.md#startabilitybycall)接口 拉起目标Callee UIAbility，目标UIAbility启动成功后，返回一个Caller对象给调用方进行通信。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 导入模块

```TypeScript
import { UIAbility, Callee, CalleeCallback, Caller, OnReleaseCallback, OnRemoteStateChangeCallback } from 'kits/@kit.AbilityKit';
```

## call

```TypeScript
call(method: string, data: rpc.Parcelable): Promise<void>
```

Caller UIAbility向Callee UIAbility发送双方约定好的序列化的数据。使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| method | string | 是 |
| data | rpc.Parcelable | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16200002](../errorcode-ability.md#16200002-通用组件服务端callee无效) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## callWithResult

```TypeScript
callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence>
```

Caller UIAbility向Callee UIAbility发送消息，Callee UIAbility处理完成后返回结果。使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| method | string | 是 |
| data | rpc.Parcelable | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;rpc.MessageSequence & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16200002](../errorcode-ability.md#16200002-通用组件服务端callee无效) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## off('release')

```TypeScript
off(type: 'release', callback: OnReleaseCallback): void
```

取消注册Callee UIAbility断开通知的监听，与[on('release')](#onrelease)是反向操作，当前暂未支持。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'release' | 是 |
| callback | [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('release')

```TypeScript
off(type: 'release'): void
```

取消注册Callee UIAbility断开通知的监听，与[Caller.on('release')](#onrelease)是反向操作，当前暂未支持。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'release' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('release')

```TypeScript
on(type: 'release', callback: OnReleaseCallback): void
```

Caller UIAbility可使用该接口注册与Callee UIAbility连接断开通知的监听。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'release' | 是 |
| callback | [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## onRelease

```TypeScript
onRelease(callback: OnReleaseCallback): void
```

Caller UIAbility可使用该接口注册与Callee UIAbility连接断开通知的监听。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## onRemoteStateChange

```TypeScript
onRemoteStateChange(callback: OnRemoteStateChangeCallback): void
```

注册协同场景下跨设备组件状态变化监听通知。使用callback异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnRemoteStateChangeCallback](arkts-ability-app-ability-uiability-onremotestatechangecallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## release

```TypeScript
release(): void
```

Caller主动释放与Callee UIAbility的连接。调用该接口后，Caller不能再使用call或callWithResult向Callee方发送消息。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**错误码：**

| 错误码ID |
| --- |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16200002](../errorcode-ability.md#16200002-通用组件服务端callee无效) |
