# sendDialogResult（系统接口）

## 导入模块

```TypeScript
import { dialogSession } from '@kit.AbilityKit';
```

## sendDialogResult

```TypeScript
function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean): Promise<void>
```

发送用户请求。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dialogSessionId | string | 是 |
| targetWant | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| isAllowed | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

```TypeScript
import { dialogSession, Want, UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want由系统内部指定，dialogSessionId为内置参数
    let dialogSessionId: string | undefined = want.parameters?.['dialogSessionId'] as string;

    // 查询DialogSessionInfo
    let dialogSessionInfo: dialogSession.DialogSessionInfo | null = dialogSession.getDialogSessionInfo(dialogSessionId);

    let isAllow: boolean = true;

    let targetWant: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      dialogSession.sendDialogResult(dialogSessionId, targetWant, isAllow, (err, data) => {
        if (err) {
          console.error(`sendDialogResult error, errorCode: ${err.code}`);
        } else {
          console.info(`sendDialogResult success`);
        }
      });
    } catch (err) {
      console.error(`sendDialogResult error, errorCode: ${(err as BusinessError).code}`);
    }
  }
}
```

```TypeScript
import { dialogSession, Want, UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want由系统内部指定，dialogSessionId为内置参数
    let dialogSessionId: string | undefined = want.parameters?.['dialogSessionId'] as string;

    // 查询DialogSessionInfo
    let dialogSessionInfo: dialogSession.DialogSessionInfo | null = dialogSession.getDialogSessionInfo(dialogSessionId);

    let isAllow: boolean = true;

    let targetWant: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      dialogSession.sendDialogResult(dialogSessionId, targetWant, isAllow)
        .then((data) => {
          console.info(`sendDialogResult success`);
        }, (error: Error) => {
          let err = error as BusinessError;
          console.error(`sendDialogResult error, errorCode: ${err.code}`);
        });
    } catch (err) {
      console.error(`sendDialogResult error, errorCode: ${(err as BusinessError).code}`);
    }
  }
}
```


## sendDialogResult

```TypeScript
function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean, callback: AsyncCallback<void>): void
```

发送用户请求。使用callback异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dialogSessionId | string | 是 |
| targetWant | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| isAllowed | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

参见 [sendDialogResult](#senddialogresult)
