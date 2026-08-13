# IAuthWidgetCallback (System API)

Defines the callback of the authentication widget. The authentication widget uses this callback to obtain commands sent by the user authentication framework and perform corresponding authentication operations based on the command content.

**Since:** 23

**Deprecated since:** -1

<!--Device-userAuth-interface IAuthWidgetCallback--><!--Device-userAuth-interface IAuthWidgetCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## sendCommand

```TypeScript
sendCommand(cmdData: string): void
```

Triggered to receive commands from the user authentication framework. The user authentication framework uses this callback to send commands to the identity authentication widget. The widget needs to parse the command content and perform corresponding operations.

**Since:** 10

**Deprecated since:** -1

<!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void--><!--Device-IAuthWidgetCallback-sendCommand(cmdData: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cmdData | string | Yes |

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

Called to return the command sent from the user authentication framework to the user authentication widget.

**Type:** [AuthWidgetCallbackSendCommandFunc](arkts-userauthentication-userauth-authwidgetcallbacksendcommandfunc-t-sys.md)

**Since:** 23

**Deprecated since:** -1

<!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc--><!--Device-IAuthWidgetCallback-sendCommand: AuthWidgetCallbackSendCommandFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.
