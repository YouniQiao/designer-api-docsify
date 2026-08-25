# IUserAuthCallback (System API)

Provides callbacks for user authentication.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| module | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| acquire | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| extraInfo | Uint8Array | Yes |

**Examples**

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

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| extraInfo | [AuthResult](arkts-basicservices-appaccount-authresult-i.md) | Yes |

**Examples**

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

```TypeScript
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: number, extraInfo: osAccount.RequestResult) => {
    console.info('callback result = ' + result)
    console.info('callback extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```
