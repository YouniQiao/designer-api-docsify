# UserAuthWidgetMgr (System API)

Defines the identity authentication widget manager. It is used to register custom identity authentication widgets with the **UserAuthWidgetMgr** for unified management and scheduling. Custom authentication widgets can receive commands from the user authentication framework and execute corresponding operations.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-userAuth-interface UserAuthWidgetMgr--><!--Device-userAuth-interface UserAuthWidgetMgr-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## offCommand

```TypeScript
offCommand(callback?: IAuthWidgetCallback): void
```

Unsubscribes from commands sent from the user authentication framework.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-UserAuthWidgetMgr-offCommand(callback?: IAuthWidgetCallback): void--><!--Device-UserAuthWidgetMgr-offCommand(callback?: IAuthWidgetCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | No | Callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

## off_command

```TypeScript
off(type: 'command', callback?: IAuthWidgetCallback): void
```

Unsubscribes from command events from the user authentication framework. The authentication widget uses this API to unsubscribe from commands from the user authentication framework.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-UserAuthWidgetMgr-off(type: 'command', callback?: IAuthWidgetCallback): void--><!--Device-UserAuthWidgetMgr-off(type: 'command', callback?: IAuthWidgetCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'command' | Yes | Event type to subscribe to. The value **'command'** indicates that the event that the user authentication framework sends commands to the identity authentication widget is unsubscribed. |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | No | Callback to unregister, which must be the same as the callback passed in the **on** method. If this parameter is not passed, all registered callbacks are unregistered. Before using the **off** API, ensure that the corresponding callback has been registered through the [on](#on_command) method. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

const userAuthWidgetMgrVersion = 1;
try {
  let userAuthWidgetMgr = userAuth.getUserAuthWidgetMgr(userAuthWidgetMgrVersion);
  console.info('get userAuthWidgetMgr instance success');
  userAuthWidgetMgr.off('command', {
    sendCommand(cmdData) {
      console.info(`The cmdData is ${cmdData}`);
    }
  })
  console.info('cancel subscribe authentication event success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`userAuth widgetMgr catch error: Code is ${err?.code}, message is ${err?.message}`);
}
```

## onCommand

```TypeScript
onCommand(callback: IAuthWidgetCallback): void
```

Subscribes to commands from the user authentication framework for the user authentication widget.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-UserAuthWidgetMgr-onCommand(callback: IAuthWidgetCallback): void--><!--Device-UserAuthWidgetMgr-onCommand(callback: IAuthWidgetCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | Yes | Callback used to return the command from the user authentication framework to the user authentication widget. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

## on_command

```TypeScript
on(type: 'command', callback: IAuthWidgetCallback): void
```

Subscribes to command events from the user authentication framework. The authentication widget uses this API to subscribe to commands from the user authentication framework so that it can perform corresponding authentication operations based on the commands.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-UserAuthWidgetMgr-on(type: 'command', callback: IAuthWidgetCallback): void--><!--Device-UserAuthWidgetMgr-on(type: 'command', callback: IAuthWidgetCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'command' | Yes | Event type to subscribe to. The value **'command'** indicates that the event is used by the user authentication framework to send commands to the user authentication widget. |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | Yes | Callback function. It is used to receive commands from the user authentication framework. The authentication widget needs to parse the commands and perform corresponding operations in the callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

## Examples

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

