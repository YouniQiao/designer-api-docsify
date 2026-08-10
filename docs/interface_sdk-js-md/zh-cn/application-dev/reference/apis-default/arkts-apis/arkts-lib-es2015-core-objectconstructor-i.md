# ObjectConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## assign

```TypeScript
assign<T extends {}, U>(target: T, source: U): T & U
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-assign<T extends {}, U>(target: T, source: U): T & U--><!--Device-ObjectConstructor-assign<T extends {}, U>(target: T, source: U): T & U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | T | 是 |  |
| source | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T & U |  |

## assign

```TypeScript
assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V--><!--Device-ObjectConstructor-assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | T | 是 |  |
| source1 | U | 是 |  |
| source2 | V | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T & U & V |  |

## assign

```TypeScript
assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W--><!--Device-ObjectConstructor-assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | T | 是 |  |
| source1 | U | 是 |  |
| source2 | V | 是 |  |
| source3 | W | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T & U & V & W |  |

## assign

```TypeScript
assign(target: object, ...sources: any[]): any
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-assign(target: object, ...sources: any[]): any--><!--Device-ObjectConstructor-assign(target: object, ...sources: any[]): any-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | object | 是 |  |
| sources | any[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

## getOwnPropertySymbols

```TypeScript
getOwnPropertySymbols(o: any): symbol[]
```

Returns an array of all symbol properties found directly on object o.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-getOwnPropertySymbols(o: any): symbol[]--><!--Device-ObjectConstructor-getOwnPropertySymbols(o: any): symbol[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | any | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| symbol[] |  |

## is

```TypeScript
is(value1: any, value2: any): boolean
```

Returns true if the values are the same value, false otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-is(value1: any, value2: any): boolean--><!--Device-ObjectConstructor-is(value1: any, value2: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value1 | any | 是 |  |
| value2 | any | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## keys

```TypeScript
keys(o: {}): string[]
```

Returns the names of the enumerable string properties and methods of an object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-keys(o: {}): string[]--><!--Device-ObjectConstructor-keys(o: {}): string[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | {} | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] |  |

## setPrototypeOf

```TypeScript
setPrototypeOf(o: any, proto: object | null): any
```

Sets the prototype of a specified object o to object proto or null. Returns the object o.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ObjectConstructor-setPrototypeOf(o: any, proto: object | null): any--><!--Device-ObjectConstructor-setPrototypeOf(o: any, proto: object | null): any-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | any | 是 |  |
| proto | object \| null | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

