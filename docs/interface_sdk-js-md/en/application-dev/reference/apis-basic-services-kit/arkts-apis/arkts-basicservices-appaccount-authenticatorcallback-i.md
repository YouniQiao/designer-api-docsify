# AuthenticatorCallback

Provides OAuth authenticator callbacks.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

Called to redirect a request.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use [onRequestRedirected](arkts-basicservices-appaccount-authcallback-i.md#onrequestredirected) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onRequestRedirected](arkts-basicservices-appaccount-authcallback-i.md#onrequestredirected)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## onResult

```TypeScript
onResult: (code: number, result: { [key: string]: any }) => void
```

Called to return the result of an authentication request.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use [onResult](arkts-basicservices-appaccount-authcallback-i.md#onresult) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onResult](arkts-basicservices-appaccount-authcallback-i.md#onresult)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| result | { [key: string]: any } | Yes |
