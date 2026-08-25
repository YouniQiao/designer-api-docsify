# off

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## off('applicationState')

```TypeScript
function off(type: 'applicationState', observerId: number, callback: AsyncCallback<void>): void
```

注销应用状态监听器。使用callback异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'applicationState' | 是 |
| observerId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |


## off('applicationState')

```TypeScript
function off(type: 'applicationState', observerId: number): Promise<void>
```

注销应用状态监听器。使用Promise异步回调。

**起始版本：** 14

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'applicationState' | 是 |
| observerId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
