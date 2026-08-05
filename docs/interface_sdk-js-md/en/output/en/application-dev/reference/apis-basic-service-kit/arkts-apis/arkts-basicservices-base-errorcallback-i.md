# ErrorCallback

Defines a common callback that carries an error parameter, which is used to return error information when the API call fails. The specific error code is defined by each API. For details, please refer to the error code description of the corresponding API. The information returned by the callback is an error parameter of the [BusinessError]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ type.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface ErrorCallback<T extends Error = BusinessError>--><!--Device-unnamed-export interface ErrorCallback<T extends Error = BusinessError>-End-->

**System capability:** SystemCapability.Base

## constructor

```TypeScript
(err: T): void
```

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorCallback-(err: T): void--><!--Device-ErrorCallback-(err: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | T | Yes | Common error message returned when the API fails to be called. |

