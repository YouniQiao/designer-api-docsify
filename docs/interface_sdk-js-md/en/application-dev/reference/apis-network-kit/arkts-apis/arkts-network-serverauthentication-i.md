# ServerAuthentication

HTTP server authentication.

**Since:** 18

<!--Device-http-export interface ServerAuthentication--><!--Device-http-export interface ServerAuthentication-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## authenticationType

```TypeScript
authenticationType?: AuthenticationType
```

Authentication type of server. If not set, negotiate with the server.

**Type:** AuthenticationType

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ServerAuthentication-authenticationType?: AuthenticationType--><!--Device-ServerAuthentication-authenticationType?: AuthenticationType-End-->

**System capability:** SystemCapability.Communication.NetStack

## credential

```TypeScript
credential: Credential
```

Credential of server.

**Type:** Credential

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ServerAuthentication-credential: Credential--><!--Device-ServerAuthentication-credential: Credential-End-->

**System capability:** SystemCapability.Communication.NetStack

