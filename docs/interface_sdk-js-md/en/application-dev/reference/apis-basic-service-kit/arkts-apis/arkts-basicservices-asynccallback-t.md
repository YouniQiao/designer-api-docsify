# AsyncCallback

```TypeScript
export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void
```

Defines a common callback that carries an error parameter and asynchronous return value.The error parameter is of the [BusinessError]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ type. The type of the asynchronous return value is defined by the developer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void--><!--Device-unnamed-export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;E&gt; \| null | Yes | Common error information about the API invoking failure.  |
| data | T \| undefined | Yes | Common callback information.  |

