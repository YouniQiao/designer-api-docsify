# ProxyHandler

## Modules to Import

```TypeScript
```

## apply

```TypeScript
apply?(target: T, thisArg: any, argArray: any[]): any
```

A trap method for a function call.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| thisArg | any | Yes |  |
| argArray | any[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## construct

```TypeScript
construct?(target: T, argArray: any[], newTarget: Function): object
```

A trap for the `new` operator.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| argArray | any[] | Yes |  |
| newTarget | Function | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## defineProperty

```TypeScript
defineProperty?(target: T, property: string | symbol, attributes: PropertyDescriptor): boolean
```

A trap for `Object.defineProperty()`.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| property | string \| symbol | Yes |  |
| attributes | PropertyDescriptor | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## deleteProperty

```TypeScript
deleteProperty?(target: T, p: string | symbol): boolean
```

A trap for the `delete` operator.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## get

```TypeScript
get?(target: T, p: string | symbol, receiver: any): any
```

A trap for getting a property value.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |
| receiver | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getOwnPropertyDescriptor

```TypeScript
getOwnPropertyDescriptor?(target: T, p: string | symbol): PropertyDescriptor | undefined
```

A trap for `Object.getOwnPropertyDescriptor()`.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getPrototypeOf

```TypeScript
getPrototypeOf?(target: T): object | null
```

A trap for the `[[GetPrototypeOf]]` internal method.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## has

```TypeScript
has?(target: T, p: string | symbol): boolean
```

A trap for the `in` operator.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| p | string \| symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## isExtensible

```TypeScript
isExtensible?(target: T): boolean
```

A trap for `Object.isExtensible()`.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## ownKeys

```TypeScript
ownKeys?(target: T): ArrayLike<string | symbol>
```

A trap for `Reflect.ownKeys()`.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## preventExtensions

```TypeScript
preventExtensions?(target: T): boolean
```

A trap for `Object.preventExtensions()`.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## set

```TypeScript
set?(target: T, p: string | symbol, newValue: any, receiver: any): boolean
```

A trap for setting a property value.

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
## setPrototypeOf

```TypeScript
setPrototypeOf?(target: T, v: object | null): boolean
```

A trap for `Object.setPrototypeOf()`.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| v | object \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
