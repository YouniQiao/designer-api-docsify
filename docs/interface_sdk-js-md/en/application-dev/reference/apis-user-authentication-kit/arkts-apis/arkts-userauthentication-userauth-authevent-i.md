# AuthEvent

Provides an asynchronous callback to return the authentication event information.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## callback

```TypeScript
callback(result: EventInfo): void
```

Called to return the authentication result or authentication tip information.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [onResult](arkts-userauthentication-userauth-iauthcallback-i.md#onresult)(result: UserAuthResult)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [EventInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-update-eventinfo-i-sys.md) | Yes |
