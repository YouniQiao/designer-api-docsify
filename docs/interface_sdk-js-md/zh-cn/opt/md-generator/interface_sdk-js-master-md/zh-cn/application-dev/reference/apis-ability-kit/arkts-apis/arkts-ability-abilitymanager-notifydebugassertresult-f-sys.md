# notifyDebugAssertResult（系统接口）

## notifyDebugAssertResult

```TypeScript
function notifyDebugAssertResult(sessionId: string, status: UserStatus): Promise<void>
```

将断言调试结果通知应用程序。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.NOTIFY_DEBUG_ASSERT_RESULT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityManager-function notifyDebugAssertResult(sessionId: string, status: UserStatus): Promise<void>--><!--Device-abilityManager-function notifyDebugAssertResult(sessionId: string, status: UserStatus): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { abilityManager, UIExtensionAbility, wantConstant, Want, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UiExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    let sessionId: string = '';
    if (want.parameters) {
      sessionId = want.parameters[wantConstant.Params.ASSERT_FAULT_SESSION_ID] as string;
    }
    // 设置用户操作状态为终止
    let status = abilityManager.UserStatus.ASSERT_TERMINATE;
    abilityManager.notifyDebugAssertResult(sessionId, status).then(() => {
      console.info('notifyDebugAssertResult success.');
    }).catch((err: BusinessError) => {
      console.error(`notifyDebugAssertResult failed, error: ${JSON.stringify(err)}`);
    });
  }
}
```
