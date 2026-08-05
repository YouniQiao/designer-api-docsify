# IAuthWidgetCallback (System API)

Defines the callback of the authentication widget. The authentication widget uses this callback to obtain commands sent by the user authentication framework and perform corresponding authentication operations based on the command content.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-userAuth-interface IAuthWidgetCallback--><!--Device-userAuth-interface IAuthWidgetCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## sendCommand

```TypeScript
sendCommand(cmdData: string): void
```

Triggered to receive commands from the user authentication framework. The user authentication framework uses this callback to send commands to the identity authentication widget. The widget needs to parse the command content and perform corresponding operations.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void--><!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cmdData | string | Yes | Command data, which is a JSON string containing the command content sent by the user authentication framework to the authentication widget. The JSON structure includes corresponding fields based on different command types. Common fields include: **commandType** (string, command type), **authType** (array, list of authentication types), **result** (number, authentication result code), etc. The widget must parse this data and perform corresponding operations based on the command type. |

**Example**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

const userAuthWidgetMgrVersion = 1;
try {
  let userAuthWidgetMgr = userAuth.getUserAuthWidgetMgr(userAuthWidgetMgrVersion);
  console.info('get userAuthWidgetMgr instance success');
  userAuthWidgetMgr.on('command', {
    sendCommand(cmdData) {
      console.info(`The cmdData is ${cmdData}`);
    }
  })
  console.info('subscribe authentication event success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`userAuth widgetMgr catch error: Code is ${err?.code}, message is ${err?.message}`);
}
```

## sendCommand

```TypeScript
sendCommand: AuthWidgetCallbackSendCommandFunc
```

Called to return the command sent from the user authentication framework to the user authentication widget.

**Type:** AuthWidgetCallbackSendCommandFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc--><!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

