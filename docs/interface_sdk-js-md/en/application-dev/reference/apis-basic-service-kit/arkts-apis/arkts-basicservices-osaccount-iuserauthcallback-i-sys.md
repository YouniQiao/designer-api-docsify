# IUserAuthCallback (System API)

Provides callbacks for user authentication.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-osAccount-interface IUserAuthCallback--><!--Device-osAccount-interface IUserAuthCallback-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'osAccount';
```

## onAcquireInfo

```TypeScript
onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void
```

Called to acquire identity authentication information.

**Type:** (module: int, acquire: int, extraInfo: Uint8Array) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-IUserAuthCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void--><!--Device-IUserAuthCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## onResult

```TypeScript
onResult: (result: int, extraInfo: AuthResult) => void
```

Called to return the result code and authentication result.

**Type:** (result: int, extraInfo: AuthResult) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-IUserAuthCallback-onResult: (result: int, extraInfo: AuthResult) => void--><!--Device-IUserAuthCallback-onResult: (result: int, extraInfo: AuthResult) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

