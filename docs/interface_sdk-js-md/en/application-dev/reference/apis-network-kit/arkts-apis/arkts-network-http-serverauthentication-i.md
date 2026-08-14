# ServerAuthentication

HTTP server authentication.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-http-export interface ServerAuthentication--><!--Device-http-export interface ServerAuthentication-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from 'http';
```

## authenticationType

```TypeScript
authenticationType?: AuthenticationType
```

Authentication type of server. If not set, negotiate with the server.

**Type:** [AuthenticationType](arkts-network-http-authenticationtype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ServerAuthentication-authenticationType?: AuthenticationType--><!--Device-ServerAuthentication-authenticationType?: AuthenticationType-End-->

**System capability:** SystemCapability.Communication.NetStack

## credential

```TypeScript
credential: Credential
```

Credential of server.

**Type:** Credential

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ServerAuthentication-credential: Credential--><!--Device-ServerAuthentication-credential: Credential-End-->

**System capability:** SystemCapability.Communication.NetStack

