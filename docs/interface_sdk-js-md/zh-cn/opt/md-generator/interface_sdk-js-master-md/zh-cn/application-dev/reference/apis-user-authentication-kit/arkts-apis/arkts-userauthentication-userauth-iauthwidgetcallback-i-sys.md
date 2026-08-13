# IAuthWidgetCallback（系统接口）

身份认证组件回调接口。认证组件通过该回调接口获取用户认证框架发送的命令，并根据命令内容执行相应的认证操作。

**起始版本：** 23

**废弃版本：** -1

<!--Device-userAuth-interface IAuthWidgetCallback--><!--Device-userAuth-interface IAuthWidgetCallback-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

## sendCommand

```TypeScript
sendCommand(cmdData: string): void
```

回调函数，用于接收来自用户认证框架的命令。用户认证框架通过此回调向身份认证组件发送命令，控件需解析命令内容并执行相应操作。

**起始版本：** 10

**废弃版本：** -1

<!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void--><!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmdData | string | 是 |

## 示例

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

const userAuthWidgetMgrVersion = 1;
try {
  let userAuthWidgetMgr = userAuth.getUserAuthWidgetMgr(userAuthWidgetMgrVersion);
  console.info('get userAuthWidgetMgr instance successfully.');
  userAuthWidgetMgr.on('command', {
    sendCommand: (cmdData) => {
      console.info(`The cmdData is ${cmdData}`);
    }
  })
  console.info('subscribe authentication event successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`userAuth widgetMgr failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## sendCommand

```TypeScript
sendCommand: AuthWidgetCallbackSendCommandFunc
```

回调函数，用于用户认证框架向组件发送命令。

**类型：** [AuthWidgetCallbackSendCommandFunc](arkts-userauthentication-userauth-authwidgetcallbacksendcommandfunc-t-sys.md)

**起始版本：** 23

**废弃版本：** -1

<!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc--><!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。
