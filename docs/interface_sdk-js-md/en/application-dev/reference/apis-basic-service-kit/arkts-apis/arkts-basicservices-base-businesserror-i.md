# BusinessError

Defines the error parameter.

**Inheritance/Implementation:** BusinessError extends [Error](../../apis-na/arkts-apis/arkts-na-lib-es2022-error-error-i.md)

**Since:** 6

<!--Device-unnamed-export interface BusinessError<T = void> extends Error--><!--Device-unnamed-export interface BusinessError<T = void> extends Error-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from '@kit.BasicServicesKit';
```

## code

```TypeScript
code: number
```

Error code returned when the API fails to be called.

**Type:** number

**Since:** 6

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

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BusinessError-data?: T--><!--Device-BusinessError-data?: T-End-->

**System capability:** SystemCapability.Base

