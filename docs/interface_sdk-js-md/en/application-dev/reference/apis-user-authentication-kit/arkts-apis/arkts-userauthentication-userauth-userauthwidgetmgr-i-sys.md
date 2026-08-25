# UserAuthWidgetMgr (System API)

Defines the authentication widget manager. It is used to register the custom authentication widget with the **UserAuthWidgetMgr** for unified management and scheduling. The custom authentication widget can receive commands from the user authentication framework and perform corresponding operations.

**Since:** 10

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## off('command')

```TypeScript
off(type: 'command', callback?: IAuthWidgetCallback): void
```

Unsubscribes from command events from the user authentication framework. The authentication widget uses this API to unsubscribe from commands from the user authentication framework.

**Since:** 10

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'command' | Yes |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## on('command')

```TypeScript
on(type: 'command', callback: IAuthWidgetCallback): void
```

Subscribes to command events from the user authentication framework. The authentication widget uses this API to subscribe to commands from the user authentication framework so that it can perform corresponding authentication operations based on the commands.

**Since:** 10

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'command' | Yes |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
