# ObjectConstructor

## Modules to Import

```TypeScript
```

## assign

```TypeScript
assign<T extends {}, U>(target: T, source: U): T & U
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| source | U | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## assign

```TypeScript
assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| source1 | U | Yes |  |
| source2 | V | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## assign

```TypeScript
assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| source1 | U | Yes |  |
| source2 | V | Yes |  |
| source3 | W | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## assign

```TypeScript
assign(target: object, ...sources: any[]): any
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes |  |
| sources | any[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getOwnPropertySymbols

```TypeScript
getOwnPropertySymbols(o: any): symbol[]
```

Returns an array of all symbol properties found directly on object o.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## is

```TypeScript
is(value1: any, value2: any): boolean
```

Returns true if the values are the same value, false otherwise.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value1 | any | Yes |  |
| value2 | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## keys

```TypeScript
keys(o: {}): string[]
```

Returns the names of the enumerable string properties and methods of an object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | {} | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setPrototypeOf

```TypeScript
setPrototypeOf(o: any, proto: object | null): any
```

Sets the prototype of a specified object o to object proto or null. Returns the object o.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |
| proto | object \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
