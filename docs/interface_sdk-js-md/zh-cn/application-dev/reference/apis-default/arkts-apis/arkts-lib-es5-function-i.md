# Function

Creates a new function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface Function--><!--Device-unnamed-interface Function-End-->

## apply

```TypeScript
apply(this: Function, thisArg: any, argArray?: any): any
```

Calls the function, substituting the specified object for the this value of the function, and the specified array for the arguments of the function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Function-apply(this: Function, thisArg: any, argArray?: any): any--><!--Device-Function-apply(this: Function, thisArg: any, argArray?: any): any-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | Function | 是 |  |
| thisArg | any | 是 |  |
| argArray | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

## bind

```TypeScript
bind(this: Function, thisArg: any, ...argArray: any[]): any
```

For a given function, creates a bound function that has the same body as the original function.The this object of the bound function is associated with the specified object, and has the specified initial parameters.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Function-bind(this: Function, thisArg: any, ...argArray: any[]): any--><!--Device-Function-bind(this: Function, thisArg: any, ...argArray: any[]): any-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | Function | 是 |  |
| thisArg | any | 是 |  |
| argArray | any[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

## call

```TypeScript
call(this: Function, thisArg: any, ...argArray: any[]): any
```

Calls a method of an object, substituting another object for the current object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Function-call(this: Function, thisArg: any, ...argArray: any[]): any--><!--Device-Function-call(this: Function, thisArg: any, ...argArray: any[]): any-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | Function | 是 |  |
| thisArg | any | 是 |  |
| argArray | any[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

## toString

```TypeScript
toString(): string
```

Returns a string representation of a function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Function-toString(): string--><!--Device-Function-toString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## arguments

```TypeScript
arguments: any
```

**类型：** any

**ArkTS模式：** 仅支持ArkTS-Dyn

## caller

```TypeScript
caller: Function
```

**类型：** Function

**ArkTS模式：** 仅支持ArkTS-Dyn

## length

```TypeScript
readonly length: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

## prototype

```TypeScript
prototype: any
```

**类型：** any

**ArkTS模式：** 仅支持ArkTS-Dyn

