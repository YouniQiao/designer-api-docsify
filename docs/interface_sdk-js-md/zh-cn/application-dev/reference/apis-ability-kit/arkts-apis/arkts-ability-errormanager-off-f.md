# off

## 导入模块

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## off('error')

```TypeScript
function off(type: 'error', observerId: number, callback: AsyncCallback<void>): void
```

注销错误观测器。使用callback异步返回。仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| observerId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000003](../errorcode-ability.md#16000003-指定的id不存在) |


## off('error')

```TypeScript
function off(type: 'error', observerId: number): Promise<void>
```

注销错误观测器。使用Promise异步返回。仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| observerId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000003](../errorcode-ability.md#16000003-指定的id不存在) |


## off('loopObserver')

```TypeScript
function off(type: 'loopObserver', observer?: LoopObserver): void
```

注销主线程消息处理监听器。仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'loopObserver' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |


## off('unhandledRejection')

```TypeScript
function off(type: 'unhandledRejection', observer?: UnhandledRejectionObserver): void
```

注销被拒绝promise监听器。仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'unhandledRejection' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |


## off('globalUnhandledRejectionDetected')

```TypeScript
function off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void
```

注销被拒绝promise监听器，注销后无法监听进程中的promise异常。如果传入的回调不在通过on方法注册的回调队列中，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'globalUnhandledRejectionDetected' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |


## off('freeze')

```TypeScript
function off(type: 'freeze', observer?: FreezeObserver): void
```

取消之前注册的应用主线程freeze监听。仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。如果传入的回调与通过on方法注册回调不一致，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'freeze' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |


## off('globalErrorOccurred')

```TypeScript
function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void
```

注销错误观测器，注销之前注册在同一线程的callback全局监听。如果传入的回调不在通过on方法注册的回调队列中，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'globalErrorOccurred' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |
