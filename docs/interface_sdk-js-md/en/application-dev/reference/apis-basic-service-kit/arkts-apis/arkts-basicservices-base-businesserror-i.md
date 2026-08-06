# BusinessError

Defines an error parameter. This API inherits from the **Error** class and is used to pass standard error information, including the error code and optional additional information.

**Inheritance/Implementation:** BusinessError extends [Error](../../apis-arkts/arkts-apis/arkts-arkts-static/error-error-c.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface BusinessError<T = void> extends Error--><!--Device-unnamed-export interface BusinessError<T = void> extends Error-End-->

**System capability:** SystemCapability.Base

## code

```TypeScript
code: number
```

Error code returned when the API fails to be called. The specific error code is defined by each API. For details,see the error code description of the corresponding API.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BusinessError-code: number--><!--Device-BusinessError-code: number-End-->

**System capability:** SystemCapability.Base

## data

```TypeScript
data?: T
```

Error message returned when the API fails to be called. If this parameter is left empty, the error object does not contain additional data.

**Type:** T

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BusinessError-data?: T--><!--Device-BusinessError-data?: T-End-->

**System capability:** SystemCapability.Base

