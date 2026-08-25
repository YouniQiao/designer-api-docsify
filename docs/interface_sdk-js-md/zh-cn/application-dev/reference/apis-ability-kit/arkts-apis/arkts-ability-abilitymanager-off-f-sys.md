# off（系统接口）

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## off('abilityForegroundState')

```TypeScript
function off(type: 'abilityForegroundState', observer?: AbilityForegroundStateObserver): void
```

取消注册Ability启动和退出的观测器。

**起始版本：** 11

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'abilityForegroundState' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
