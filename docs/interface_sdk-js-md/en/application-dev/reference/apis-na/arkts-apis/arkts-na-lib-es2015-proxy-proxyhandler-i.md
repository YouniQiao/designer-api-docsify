# ProxyHandler

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface ProxyHandler--><!--Device-unnamed-interface ProxyHandler-End-->

## apply

```TypeScript
apply?(target: T, thisArg: any, argArray: any[]): any
```

A trap method for a function call.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-apply?(target: T, thisArg: any, argArray: any[]): any--><!--Device-ProxyHandler-apply?(target: T, thisArg: any, argArray: any[]): any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| thisArg | any | Yes |  |
| argArray | any[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| any |  |

## construct

```TypeScript
construct?(target: T, argArray: any[], newTarget: Function): object
```

A trap for the `new` operator.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-construct?(target: T, argArray: any[], newTarget: Function): object--><!--Device-ProxyHandler-construct?(target: T, argArray: any[], newTarget: Function): object-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| argArray | any[] | Yes |  |
| newTarget | Function | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| object |  |

## defineProperty

```TypeScript
defineProperty?(target: T, property: string | symbol, attributes: PropertyDescriptor): boolean
```

A trap for `Object.defineProperty()`.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-defineProperty?(target: T, property: string | symbol, attributes: PropertyDescriptor): boolean--><!--Device-ProxyHandler-defineProperty?(target: T, property: string | symbol, attributes: PropertyDescriptor): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| property | string \| symbol | Yes |  |
| attributes | PropertyDescriptor | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## deleteProperty

```TypeScript
deleteProperty?(target: T, p: string | symbol): boolean
```

A trap for the `delete` operator.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-deleteProperty?(target: T, p: string | symbol): boolean--><!--Device-ProxyHandler-deleteProperty?(target: T, p: string | symbol): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## get

```TypeScript
get?(target: T, p: string | symbol, receiver: any): any
```

A trap for getting a property value.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-get?(target: T, p: string | symbol, receiver: any): any--><!--Device-ProxyHandler-get?(target: T, p: string | symbol, receiver: any): any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |
| receiver | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| any |  |

## getOwnPropertyDescriptor

```TypeScript
getOwnPropertyDescriptor?(target: T, p: string | symbol): PropertyDescriptor | undefined
```

A trap for `Object.getOwnPropertyDescriptor()`.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-getOwnPropertyDescriptor?(target: T, p: string | symbol): PropertyDescriptor | undefined--><!--Device-ProxyHandler-getOwnPropertyDescriptor?(target: T, p: string | symbol): PropertyDescriptor | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| PropertyDescriptor |  |

## getPrototypeOf

```TypeScript
getPrototypeOf?(target: T): object | null
```

A trap for the `[[GetPrototypeOf]]` internal method.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-getPrototypeOf?(target: T): object | null--><!--Device-ProxyHandler-getPrototypeOf?(target: T): object | null-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| object |  |

## has

```TypeScript
has?(target: T, p: string | symbol): boolean
```

A trap for the `in` operator.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-has?(target: T, p: string | symbol): boolean--><!--Device-ProxyHandler-has?(target: T, p: string | symbol): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## isExtensible

```TypeScript
isExtensible?(target: T): boolean
```

A trap for `Object.isExtensible()`.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-isExtensible?(target: T): boolean--><!--Device-ProxyHandler-isExtensible?(target: T): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## ownKeys

```TypeScript
ownKeys?(target: T): ArrayLike<string | symbol>
```

A trap for `Reflect.ownKeys()`.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-ownKeys?(target: T): ArrayLike<string | symbol>--><!--Device-ProxyHandler-ownKeys?(target: T): ArrayLike<string | symbol>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayLike&lt;string \| symbol&gt; |  |

## preventExtensions

```TypeScript
preventExtensions?(target: T): boolean
```

A trap for `Object.preventExtensions()`.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-preventExtensions?(target: T): boolean--><!--Device-ProxyHandler-preventExtensions?(target: T): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## set

```TypeScript
set?(target: T, p: string | symbol, newValue: any, receiver: any): boolean
```

A trap for setting a property value.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-set?(target: T, p: string | symbol, newValue: any, receiver: any): boolean--><!--Device-ProxyHandler-set?(target: T, p: string | symbol, newValue: any, receiver: any): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |
| newValue | any | Yes |  |
| receiver | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## setPrototypeOf

```TypeScript
setPrototypeOf?(target: T, v: object | null): boolean
```

A trap for `Object.setPrototypeOf()`.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-ProxyHandler-setPrototypeOf?(target: T, v: object | null): boolean--><!--Device-ProxyHandler-setPrototypeOf?(target: T, v: object | null): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| v | object \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

