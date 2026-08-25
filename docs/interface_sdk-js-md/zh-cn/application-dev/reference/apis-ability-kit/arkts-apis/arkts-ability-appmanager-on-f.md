# on

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## on('applicationState')

```TypeScript
function on(type: 'applicationState', observer: ApplicationStateObserver): number
```

注册所有应用程序的状态监听器。

**起始版本：** 14

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'applicationState' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |


## on('applicationState')

```TypeScript
function on(type: 'applicationState', observer: ApplicationStateObserver, bundleNameList: Array<string>): number
```

注册指定应用程序的状态监听器。

**起始版本：** 14

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'applicationState' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | 是 |
| bundleNameList | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
