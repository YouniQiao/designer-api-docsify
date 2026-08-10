# IAuthWidgetCallback (System API)

身份认证组件回调接口。认证组件通过该回调接口获取用户认证框架发送的命令，并根据命令内容执行相应的认证操作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-userAuth-interface IAuthWidgetCallback--><!--Device-userAuth-interface IAuthWidgetCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## sendCommand

```TypeScript
sendCommand(cmdData: string): void
```

回调函数，用于接收来自用户认证框架的命令。用户认证框架通过此回调向身份认证组件发送命令，控件需解析命令内容并执行相应操作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void--><!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cmdData | string | Yes | 命令数据。JSON格式的字符串，包含用户认证框架向身份认证控件发送的具体命令内容。JSON结构根据不同的命令类型包含相应字段，常见字段包括：commandType（ string，命令类型）、authType（array，认证类型列表）、result（number，认证结果码）等。控件需解析此数据并根据命令类型执行相应操作。 |

## Examples

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc--><!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

