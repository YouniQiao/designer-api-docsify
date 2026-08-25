# AbilityDelegator

AbilityDelegator模块可以通过[AbilityMonitor](arkts-ability-abilitymonitor-i.md)实例来监听和管理 [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)生命周期的变化。例如获取UIAbility当前状态（如是否已创建/是否在前台等）、查询当前获焦的UIAbility、等待UIAbility进入 某个生命周期节点（如等待UIAbility进入onForeground）、启动指定UIAbility、设置超时机制等功能。 AbilityDelegator可以通过 [getAbilityDelegator](../../apis-test-kit/arkts-apis/arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md)方 法获取。

> **说明：**&gt;
> 本模块接口仅可在[单元测试框架](../../../application-test/unittest-guidelines.md)中使用。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## addAbilityMonitor

```TypeScript
addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void
```

添加AbilityMonitor实例。使用callback异步回调。不支持多线程并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## addAbilityMonitor

```TypeScript
addAbilityMonitor(monitor: AbilityMonitor): Promise<void>
```

添加AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## addAbilityMonitorSync

```TypeScript
addAbilityMonitorSync(monitor: AbilityMonitor): void
```

同步添加AbilityMonitor实例。不支持多线程并发调用。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## addAbilityStageMonitor

```TypeScript
addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void
```

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## addAbilityStageMonitor

```TypeScript
addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>
```

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## addAbilityStageMonitorSync

```TypeScript
addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void
```

同步添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## addInteropAbilityMonitorSync

```TypeScript
addInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void
```

新增InteropAbilityMonitor对象，用于监控此进程中指定能力的生命周期状态变化。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [InteropAbilityMonitor](arkts-ability-interopabilitymonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## doAbilityBackground

```TypeScript
doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void
```

调度指定Ability生命周期状态到Background状态。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## doAbilityBackground

```TypeScript
doAbilityBackground(ability: UIAbility): Promise<void>
```

调度指定Ability生命周期状态到Background状态。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## doAbilityForeground

```TypeScript
doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void
```

调度指定Ability生命周期状态到Foreground状态。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## doAbilityForeground

```TypeScript
doAbilityForeground(ability: UIAbility): Promise<void>
```

调度指定Ability生命周期状态到Foreground状态。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void
```

执行指定的shell命令。使用callback异步回调。 仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; | 是 |

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void
```

指定超时时间，并执行指定的shell命令。使用callback异步回调。 仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| timeoutSecs | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; | 是 |

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>
```

指定超时时间，并执行指定的shell命令。使用Promise异步回调。 仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| timeoutSecs | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; |

## finishTest

```TypeScript
finishTest(msg: string, code: number, callback: AsyncCallback<void>): void
```

结束测试并打印日志信息到单元测试终端控制台。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| code | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## finishTest

```TypeScript
finishTest(msg: string, code: number): Promise<void>
```

结束测试并打印日志信息到单元测试终端控制台。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| code | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## getAbilityState

```TypeScript
getAbilityState(ability: UIAbility): number
```

获取指定ability的生命周期状态。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getAppContext

```TypeScript
getAppContext(): Context
```

获取应用Context。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| [Context](arkts-ability-context-c.md) |

## getCurrentTopAbility

```TypeScript
getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void
```

获取当前应用顶部Ability。使用callback异步回调。不支持Worker线程调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## getCurrentTopAbility

```TypeScript
getCurrentTopAbility(): Promise<UIAbility>
```

获取当前应用顶部Ability。使用Promise异步回调。不支持Worker线程调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## print

```TypeScript
print(msg: string, callback: AsyncCallback<void>): void
```

打印日志信息到单元测试终端控制台。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## print

```TypeScript
print(msg: string): Promise<void>
```

打印日志信息到单元测试终端控制台。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## printSync

```TypeScript
printSync(msg: string): void
```

打印日志信息到单元测试终端控制台。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## removeAbilityMonitor

```TypeScript
removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void
```

删除已经添加的AbilityMonitor实例。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## removeAbilityMonitor

```TypeScript
removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>
```

删除已经添加的AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## removeAbilityMonitorSync

```TypeScript
removeAbilityMonitorSync(monitor: AbilityMonitor): void
```

同步删除已经添加的AbilityMonitor实例。不支持多线程并发调用。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## removeAbilityStageMonitor

```TypeScript
removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void
```

从应用程序内存中删除指定的AbilityStageMonitor对象。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## removeAbilityStageMonitor

```TypeScript
removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>
```

从应用程序内存中删除指定的AbilityStageMonitor对象。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## removeAbilityStageMonitorSync

```TypeScript
removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void
```

同步从应用程序内存中删除指定的AbilityStageMonitor对象。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## removeInteropAbilityMonitorSync

```TypeScript
removeInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void
```

从应用程序内存中移除指定的InteropAbilityMonitor对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [InteropAbilityMonitor](arkts-ability-interopabilitymonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## setMockList

```TypeScript
setMockList(mockList: Record<string, string>): void
```

设置模块的mock替换关系。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mockList | Record & lt;string, string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动指定Ability。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

启动指定Ability。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void
```

等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, timeout: number, callback: AsyncCallback<UIAbility>): void
```

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| timeout | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, timeout?: number): Promise<UIAbility>
```

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用Promise异步回调。不支持多线程并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void
```

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: number, callback: AsyncCallback<AbilityStage>): void
```

在指定的超时最大等待时间内，返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| timeout | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: number): Promise<AbilityStage>
```

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象，支持设置超时最大等待时间。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
