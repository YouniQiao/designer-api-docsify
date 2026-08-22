# ErrorCallback

```TypeScript
export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void
```

Defines a common callback that carries an error parameter. The information returned by the callback is of the [BusinessError](arkts-basicservices-base-businesserror-c.md) type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void--><!--Device-unnamed-export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | T | Yes | Common error information about the API invoking failure. |

