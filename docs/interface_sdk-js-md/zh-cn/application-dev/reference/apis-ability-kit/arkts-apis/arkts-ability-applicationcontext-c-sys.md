# ApplicationContext

ApplicationContext作为应用上下文，继承自Context，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力。

> **说明：**&gt;
> 本模块接口仅可在Stage模型下使用。

**继承/实现关系：** ApplicationContext extends Context

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## getProcessRunningInformation

```TypeScript
getProcessRunningInformation(): Promise<Array<ProcessInformation>>
```

获取运行中的进程信息。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [getRunningProcessInformation](arkts-ability-applicationcontext-c.md#getrunningprocessinformation)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ProcessInformation & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## getProcessRunningInformation

```TypeScript
getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

获取运行中的进程信息。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [getRunningProcessInformation](arkts-ability-applicationcontext-c.md#getrunningprocessinformation)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | AsyncCallback & lt;Array & lt;ProcessInformation & gt; & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## preloadUIExtensionAbility

```TypeScript
preloadUIExtensionAbility(want: Want): Promise<void>
```

预加载指定UIExtensionAbility实例。使用Promise异步回调。被预加载的UIExtensionAbility实例会执行到UIExtensionAbility的onCreate生命周期，然后等待被当前应用正式加载。被预加载的UIExtensionAbility实例会执行到UIExtensionAbility的onCreate生命周期，然后等待被当前应用正式加载。

**起始版本：** 12

**需要权限：** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

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
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## registerAbilityLifecycleCallback

```TypeScript
registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number
```

注册监听应用内UIAbility的生命周期。使用callback异步回调。<p>**说明：**: 仅支持主线程调用。 </p>

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [on](arkts-ability-applicationcontext-c.md#onabilitylifecycle)(type: 'abilityLifecycle', callback: AbilityLifecycleCallback)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| abilityLifecycleCallback | [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## registerEnvironmentCallback

```TypeScript
registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number
```

注册对系统环境变化的监听。使用callback异步回调。<p>**说明：**: 仅支持主线程调用。 </p>

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [on](arkts-ability-applicationcontext-c.md#onenvironment)(type: 'environment', callback: EnvironmentCallback)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| environmentCallback | [EnvironmentCallback](arkts-ability-app-ability-environmentcallback-environmentcallback-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## unregisterAbilityLifecycleCallback

```TypeScript
unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void
```

取消监听应用内UIAbility的生命周期。使用callback异步回调。<p>**说明：**: 仅支持主线程调用。 </p>

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [off](arkts-ability-applicationcontext-c.md#offabilitylifecycle)(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback&lt;void&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackId | number | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

## unregisterAbilityLifecycleCallback

```TypeScript
unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>
```

取消监听应用内UIAbility的生命周期。使用Promise异步回调。<p>**说明：**: 仅支持主线程调用。 </p>

**起始版本：** 9

**废弃版本：** 10

**替代接口：** off(type: 'abilityLifecycle', callbackId: number): Promise&lt;void&gt;;

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## unregisterEnvironmentCallback

```TypeScript
unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void
```

取消对系统环境变化的监听。使用callback异步回调。<p>**说明：**: 仅支持主线程调用。 </p>

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [off](arkts-ability-applicationcontext-c.md#offenvironment)(type: 'environment', callbackId: number, callback: AsyncCallback&lt;void&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackId | number | 是 |
| envcallback | AsyncCallback & lt;void & gt; | 是 |

## unregisterEnvironmentCallback

```TypeScript
unregisterEnvironmentCallback(callbackId: number): Promise<void>
```

取消对系统环境变化的监听。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** off(type: 'environment', callbackId: number): Promise&lt;void&gt;;

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
