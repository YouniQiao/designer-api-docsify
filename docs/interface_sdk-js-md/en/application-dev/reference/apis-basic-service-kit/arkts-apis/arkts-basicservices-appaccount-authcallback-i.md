# AuthCallback

Implements authenticator callbacks.

**Since:** 23

<!--Device-appAccount-interface AuthCallback--><!--Device-appAccount-interface AuthCallback-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'appAccount';
```

## onRequestContinued

```TypeScript
onRequestContinued?: () => void
```

Called to continue to process the request.

**Type:** () =&gt; void

**Since:** 23

<!--Device-AuthCallback-onRequestContinued?: () => void--><!--Device-AuthCallback-onRequestContinued?: () => void-End-->

**System capability:** SystemCapability.Account.AppAccount

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

Called to redirect a request.

**Type:** (request: Want) =&gt; void

**Since:** 23

<!--Device-AuthCallback-onRequestRedirected: (request: Want) => void--><!--Device-AuthCallback-onRequestRedirected: (request: Want) => void-End-->

**System capability:** SystemCapability.Account.AppAccount

## onResult

```TypeScript
onResult: (code: int, result?: AuthResult) => void
```

Called to return the result of an authentication request.

**Type:** (code: int, result?: AuthResult) =&gt; void

**Since:** 23

<!--Device-AuthCallback-onResult: (code: int, result?: AuthResult) => void--><!--Device-AuthCallback-onResult: (code: int, result?: AuthResult) => void-End-->

**System capability:** SystemCapability.Account.AppAccount

