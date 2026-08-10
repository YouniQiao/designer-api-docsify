# BusinessError

错误参数，继承自Error类，用于在接口调用失败时传递标准化的错误信息，包含错误码和可选的附加信息。

**Inheritance/Implementation:** BusinessError extends [Error](../../apis-arkts/arkts-apis/arkts-arkts-error-c.md/arkts-arkts-error-c.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface BusinessError<T = void> extends Error--><!--Device-unnamed-export interface BusinessError<T = void> extends Error-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from 'kits/@kit.BasicServicesKit';
```

## code

```TypeScript
code: number
```

接口调用失败返回的错误码信息。具体错误码值由各接口定义，请参考对应接口的错误码说明。

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

接口调用失败时返回的附加错误信息。如果不填，则错误对象不包含附加数据。

**Type:** T

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BusinessError-data?: T--><!--Device-BusinessError-data?: T-End-->

**System capability:** SystemCapability.Base

