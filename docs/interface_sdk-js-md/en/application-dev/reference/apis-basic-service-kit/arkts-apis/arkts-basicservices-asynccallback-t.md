# AsyncCallback

```TypeScript
export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void
```

Defines a common callback that carries an error parameter and asynchronous return value.The error parameter is of the [BusinessError](arkts-basicservices-base-businesserror-i.md#BusinessError) type. The type of the asynchronous return value is defined by the developer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void--><!--Device-unnamed-export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | [BusinessError](arkts-basicservices-base-businesserror-i.md)&lt;E&gt; \| null | Yes | Common error information about the API invoking failure. |
| data | T \| undefined | Yes | Common callback information. |

