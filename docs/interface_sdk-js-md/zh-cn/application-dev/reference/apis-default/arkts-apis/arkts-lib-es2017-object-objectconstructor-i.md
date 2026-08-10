# ObjectConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## entries

```TypeScript
entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]
```

Returns an array of key/values of the enumerable properties of an object

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]--><!--Device-ObjectConstructor-entries<T>(o: { [s: string]: T } | ArrayLike<T>): [string, T][]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | { [s: string]: T } \| ArrayLike&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [string, T][] |  |

## entries

```TypeScript
entries(o: {}): [string, any][]
```

Returns an array of key/values of the enumerable properties of an object

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-entries(o: {}): [string, any][]--><!--Device-ObjectConstructor-entries(o: {}): [string, any][]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | {} | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [string, any][] |  |

## getOwnPropertyDescriptors

```TypeScript
getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }
```

Returns an object containing all own property descriptors of an object

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }--><!--Device-ObjectConstructor-getOwnPropertyDescriptors<T>(o: T): {[P in keyof T]: TypedPropertyDescriptor<T[P]>} & { [x: string]: PropertyDescriptor }-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| {[P in keyof T]: TypedPropertyDescriptor&lt;T[P]&gt;} & { [x: string]: PropertyDescriptor } |  |

## values

```TypeScript
values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]
```

Returns an array of values of the enumerable properties of an object

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]--><!--Device-ObjectConstructor-values<T>(o: { [s: string]: T } | ArrayLike<T>): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | { [s: string]: T } \| ArrayLike&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## values

```TypeScript
values(o: {}): any[]
```

Returns an array of values of the enumerable properties of an object

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-values(o: {}): any[]--><!--Device-ObjectConstructor-values(o: {}): any[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | {} | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any[] |  |

