# IUserAuthCallback

Provides callbacks to return the authentication result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [AuthEvent](arkts-userauthentication-userauth-authevent-i.md)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## onAcquireInfo

```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: any) => void
```

Called to acquire authentication tip information. This API is optional.  
- **module**: ID of the module that sends the tip information.  
- **acquire**: Authentication tip information.  
- **extraInfo**: Reserved field.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [callback](arkts-userauthentication-userauth-authevent-i.md#callback)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| module | number | Yes |
| acquire | number | Yes |
| extraInfo | any | Yes |

## onResult

```TypeScript
onResult: (result: number, extraInfo: AuthResult) => void
```

Called to return the authentication result.  
- **result**: Authentication result. For details, see [ResultCode](arkts-userauthentication-userauth-resultcode-e.md).  
- **extraInfo**: Extended information, which varies depending on the authentication result. If the authentication  
is successful, the user authentication token will be returned in **extraInfo**. If the authentication fails, the remaining number of authentication times will be returned in **extraInfo**. If the authentication executor is locked, the freeze time will be returned in **extraInfo**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [callback](arkts-userauthentication-userauth-authevent-i.md#callback)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | number | Yes |
| extraInfo | [AuthResult](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-appaccount-authresult-i.md) | Yes |
