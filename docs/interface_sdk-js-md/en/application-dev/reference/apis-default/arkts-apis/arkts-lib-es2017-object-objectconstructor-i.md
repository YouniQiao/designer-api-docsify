# ObjectConstructor

**ArkTS mode:** ArkTS-Dyn only

## entries

```TypeScript
entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]
```

Returns an array of key/values of the enumerable properties of an object

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ObjectConstructor-entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]--><!--Device-ObjectConstructor-entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | { [s: string]: T } \| ArrayLike&lt;T&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [string, T][] |  |

## entries

```TypeScript
entries(o: {}): [string, any][]
```

Returns an array of key/values of the enumerable properties of an object

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ObjectConstructor-entries(o: {}): [string, any][]--><!--Device-ObjectConstructor-entries(o: {}): [string, any][]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | {} | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [string, any][] |  |

## getOwnPropertyDescriptors

```TypeScript
getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }
```

Returns an object containing all own property descriptors of an object

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ObjectConstructor-getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }--><!--Device-ObjectConstructor-getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| {[P in keyof T]: TypedPropertyDescriptor&lt;T[P]&gt;} & { [x: string]: PropertyDescriptor } |  |

## values

```TypeScript
values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]
```

Returns an array of values of the enumerable properties of an object

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ObjectConstructor-values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]--><!--Device-ObjectConstructor-values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | { [s: string]: T } \| ArrayLike&lt;T&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T[] |  |

## values

```TypeScript
values(o: {}): any[]
```

Returns an array of values of the enumerable properties of an object

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ObjectConstructor-values(o: {}): any[]--><!--Device-ObjectConstructor-values(o: {}): any[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | {} | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| any[] |  |

