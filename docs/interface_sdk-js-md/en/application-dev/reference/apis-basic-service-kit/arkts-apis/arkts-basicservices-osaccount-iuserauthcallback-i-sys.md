# IUserAuthCallback (System API)

Provides callbacks for user authentication.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface IUserAuthCallback--><!--Device-osAccount-interface IUserAuthCallback-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## onAcquireInfo

ArkTS-Dyn:
```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: Uint8Array) => void
```

ArkTS-Sta:
```TypeScript
onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void
```

Called to acquire identity authentication information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-IUserAuthCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void--><!--Device-IUserAuthCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| module | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| acquire | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| extraInfo | Uint8Array | Yes |  |

## Examples

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result)
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  },
  onAcquireInfo: (module: number, acquire: number, extraInfo: Uint8Array) => {
    console.info('auth module = ' + module);
    console.info('auth acquire = ' + acquire);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

## onResult

ArkTS-Dyn:
```TypeScript
onResult: (result: number, extraInfo: AuthResult) => void
```

ArkTS-Sta:
```TypeScript
onResult: (result: int, extraInfo: AuthResult) => void
```

Called to return the result code and authentication result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-IUserAuthCallback-onResult: (result: int, extraInfo: AuthResult) => void--><!--Device-IUserAuthCallback-onResult: (result: int, extraInfo: AuthResult) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| extraInfo | [AuthResult](arkts-basicservices-appaccount-authresult-i.md) | Yes |  |

## Examples

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

