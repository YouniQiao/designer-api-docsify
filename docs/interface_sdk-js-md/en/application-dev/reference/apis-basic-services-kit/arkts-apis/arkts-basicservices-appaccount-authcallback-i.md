# AuthCallback

Defines authenticator callbacks.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## onRequestContinued

```TypeScript
onRequestContinued?: () => void
```

Called to continue to process the request.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

Called to redirect a request.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## onResult

```TypeScript
onResult: (code: number, result?: AuthResult) => void
```

Called to return the result of an authentication request.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| result | [AuthResult](arkts-basicservices-appaccount-authresult-i.md) | No |
