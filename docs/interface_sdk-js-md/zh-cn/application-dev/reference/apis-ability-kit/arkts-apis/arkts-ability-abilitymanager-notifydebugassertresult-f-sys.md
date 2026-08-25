# notifyDebugAssertResult（系统接口）

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## notifyDebugAssertResult

```TypeScript
function notifyDebugAssertResult(sessionId: string, status: UserStatus): Promise<void>
```

将断言调试结果通知应用程序。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.NOTIFY_DEBUG_ASSERT_RESULT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| status | [UserStatus](arkts-ability-abilitymanager-userstatus-e-sys.md) | 是 |

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
| [16000050](../errorcode-ability.md#16000050-内部错误) |
