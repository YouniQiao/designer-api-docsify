# getDialogSessionInfo（系统接口）

## 导入模块

```TypeScript
import { dialogSession } from '@kit.AbilityKit';
```

## getDialogSessionInfo

```TypeScript
function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo
```

通过dialogSessionId获取会话信息。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dialogSessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) |

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

const TAG: string = '[testTag] UIExtAbility';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want由系统内部指定，dialogSessionId为内置参数
    let dialogSessionId = want?.parameters?.dialogSessionId.toString();

    // 查询DialogSessionInfo
    let dialogSessionInfo: dialogSession.DialogSessionInfo = dialogSession.getDialogSessionInfo(dialogSessionId);
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { dialogSession, Want, UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

const TAG: string = '[testTag] UIExtAbility';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want由系统内部指定，dialogSessionId为内置参数
    let dialogSessionId: string | undefined = want.parameters?.['dialogSessionId'] as string;

    // 查询DialogSessionInfo
    let dialogSessionInfo: dialogSession.DialogSessionInfo | null = dialogSession.getDialogSessionInfo(dialogSessionId);
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
  }
}
```


## getDialogSessionInfo

```TypeScript
function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo | null
```

根据dialogSessionId获取会话信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dialogSessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) \| null |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

参见 [getDialogSessionInfo](#getdialogsessioninfo)
