# AsyncCallback

Defines a common callback that carries an error parameter and asynchronous return value. It is used to return error information or success data when an asynchronous operation is complete. The error parameter is of the [BusinessError](arkts-basicservices-base-businesserror-i.md#BusinessError) type. The type of the asynchronous return value is defined by the developer.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

<!--Device-unnamed-export interface AsyncCallback--><!--Device-unnamed-export interface AsyncCallback-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { AsyncCallback } from 'AsyncCallback';
import { BusinessError } from 'BusinessError';
import { Callback } from 'Callback';
import { ErrorCallback } from 'ErrorCallback';
```

## constructor

```TypeScript
(err: BusinessError<E>, data: T): void
```

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-AsyncCallback-(err: BusinessError<E>, data: T): void--><!--Device-AsyncCallback-(err: BusinessError<E>, data: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | [BusinessError](arkts-basicservices-base-businesserror-i.md)&lt;E&gt; | Yes | Common error information returned when the API fails to be called, including the error code and optional additional data. If the **E** parameter is not specified, the default value **void** is used. In this case, **BusinessError** contains only the error code. If the API call succeeds, this parameter returns **null**. |
| data | T | Yes | Data returned asynchronously when the API is successfully called. The data type is defined by the developer. This parameter is unavailable when the API fails to be called. |

