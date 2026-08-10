# BusinessError

错误参数。

**Inheritance/Implementation:** BusinessError extends [Error](../../apis-arkts/arkts-apis/arkts-arkts-error-c.md/arkts-arkts-error-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BusinessError<T = void> extends Error--><!--Device-unnamed-export declare class BusinessError<T = void> extends Error-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from 'kits/@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

BusinessError的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor()--><!--Device-BusinessError-constructor()-End-->

**System capability:** SystemCapability.Base

## constructor

```TypeScript
constructor(code: int, error: Error)
```

BusinessError的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor(code: int, error: Error)--><!--Device-BusinessError-constructor(code: int, error: Error)-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | 接口调用失败返回的错误码信息。 |
| error | Error | Yes | 错误参数。 |

## constructor

```TypeScript
constructor(code: int, data: T, error: Error)
```

BusinessError的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor(code: int, data: T, error: Error)--><!--Device-BusinessError-constructor(code: int, data: T, error: Error)-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | 接口调用失败返回的错误码信息。 |
| data | T | Yes | 接口调用时的公共回调信息。 |
| error | Error | Yes | 错误参数。 |

## constructor

```TypeScript
constructor(code: int, message: string, data?: T)
```

BusinessError的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor(code: int, message: string, data?: T)--><!--Device-BusinessError-constructor(code: int, message: string, data?: T)-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | 接口调用失败返回的错误码信息。 |
| message | string | Yes | 接口调用失败返回描述信息。 |
| data | T | No | 接口调用时的公共回调信息。 |

## data

```TypeScript
public data?: T
```

接口调用时的公共回调信息。如果不填，则回调不返回相关信息。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-public data?: T--><!--Device-BusinessError-public data?: T-End-->

**System capability:** SystemCapability.Base

