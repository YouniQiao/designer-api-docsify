# ObjectConstructor

## Modules to Import

```TypeScript
```

## entries

```TypeScript
entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]
```

Returns an array of key/values of the enumerable properties of an object

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | { [s: string]: T } \| ArrayLike & lt;T & gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## entries

```TypeScript
entries(o: {}): [string, any][]
```

Returns an array of key/values of the enumerable properties of an object

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | {} | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getOwnPropertyDescriptors

```TypeScript
getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }
```

Returns an object containing all own property descriptors of an object

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## values

```TypeScript
values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]
```

Returns an array of values of the enumerable properties of an object

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | { [s: string]: T } \| ArrayLike & lt;T & gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## values

```TypeScript
values(o: {}): any[]
```

Returns an array of values of the enumerable properties of an object

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | {} | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
