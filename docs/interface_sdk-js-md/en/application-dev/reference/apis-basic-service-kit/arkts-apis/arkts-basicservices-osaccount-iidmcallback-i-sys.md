# IIdmCallback (System API)

Provides callbacks for IDM.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface IIdmCallback--><!--Device-osAccount-interface IIdmCallback-End-->

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

Called to acquire IDM information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-IIdmCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void--><!--Device-IIdmCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void-End-->

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
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: number, extraInfo: Object) => {
    console.info('callback result = ' + result)
    console.info('callback onResult = ' + JSON.stringify(extraInfo));
  },
  onAcquireInfo: (module: number, acquire: number, extraInfo: Uint8Array) => {
    console.info('callback module = ' + module);
    console.info('callback acquire = ' + acquire);
    console.info('callback onacquireinfo = ' + JSON.stringify(extraInfo));
  }
};
```

## onResult

ArkTS-Dyn:
```TypeScript
onResult: (result: number, extraInfo: RequestResult) => void
```

ArkTS-Sta:
```TypeScript
onResult: (result: int, extraInfo: RequestResult) => void
```

Called to return the result code and request result information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-IIdmCallback-onResult: (result: int, extraInfo: RequestResult) => void--><!--Device-IIdmCallback-onResult: (result: int, extraInfo: RequestResult) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| extraInfo | [RequestResult](arkts-basicservices-osaccount-requestresult-i-sys.md) | Yes |  |

## Examples

```TypeScript
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: number, extraInfo: osAccount.RequestResult) => {
    console.info('callback result = ' + result)
    console.info('callback extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

