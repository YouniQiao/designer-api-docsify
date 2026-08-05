# BusinessError

Defines the error parameter.

**Inheritance/Implementation:** BusinessError extends [Error](../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-error-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BusinessError<T = void> extends Error--><!--Device-unnamed-export declare class BusinessError<T = void> extends Error-End-->

**System capability:** SystemCapability.Base

## constructor

```TypeScript
constructor()
```

Defines a constructor used to create a BusinessError object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor()--><!--Device-BusinessError-constructor()-End-->

**System capability:** SystemCapability.Base

## constructor

```TypeScript
constructor(code: int, error: Error)
```

Defines a constructor used to create a **BusinessError** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor(code: int, error: Error)--><!--Device-BusinessError-constructor(code: int, error: Error)-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Common error information about the API invoking failure. |
| error | Error | Yes | Defines the error parameter. |

## constructor

```TypeScript
constructor(code: int, data: T, error: Error)
```

Defines a constructor used to create a **BusinessError** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor(code: int, data: T, error: Error)--><!--Device-BusinessError-constructor(code: int, data: T, error: Error)-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Common error information about the API invoking failure. |
| data | T | Yes | Common callback information. |
| error | Error | Yes | Defines the error parameter. |

## constructor

```TypeScript
constructor(code: int, message: string, data?: T)
```

Defines a constructor used to create a **BusinessError** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-constructor(code: int, message: string, data?: T)--><!--Device-BusinessError-constructor(code: int, message: string, data?: T)-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Common error information about the API invoking failure. |
| message | string | Yes | Error message returned when the API call fails. |
| data | T | No | Common callback information. |

## data

```TypeScript
public data?: T
```

Common callback information. If this parameter is left empty, no related information is returned.

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BusinessError-public data?: T--><!--Device-BusinessError-public data?: T-End-->

**System capability:** SystemCapability.Base

