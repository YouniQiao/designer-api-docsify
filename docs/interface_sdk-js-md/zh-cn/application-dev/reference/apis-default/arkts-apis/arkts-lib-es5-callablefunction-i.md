# CallableFunction

**ArkTS模式：** 仅支持ArkTS-Dyn

## apply

```TypeScript
apply<T, R>(this: (this: T) => R, thisArg: T): R
```

Calls the function with the specified object as the this value and the elements of specified array as the arguments.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-CallableFunction-apply<T, R>(this: (this: T) => R, thisArg: T): R--><!--Device-CallableFunction-apply<T, R>(this: (this: T) => R, thisArg: T): R-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T) =&gt; R | 是 |  |
| thisArg | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| R |  |

## apply

```TypeScript
apply<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, args: A): R
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, ...args: A) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| args | A | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| R |  |

## bind

```TypeScript
bind<T>(this: T, thisArg: ThisParameterType<T>): OmitThisParameter<T>
```

For a given function, creates a bound function that has the same body as the original function.The this object of the bound function is associated with the specified object, and has the specified initial parameters.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-CallableFunction-bind<T>(this: T, thisArg: ThisParameterType<T>): OmitThisParameter<T>--><!--Device-CallableFunction-bind<T>(this: T, thisArg: ThisParameterType<T>): OmitThisParameter<T>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | T | 是 |  |
| thisArg | [ThisParameterType](arkts-thisparametertype-t.md)&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OmitThisParameter](arkts-omitthisparameter-t.md)&lt;T&gt; |  |

## bind

```TypeScript
bind<T, A0, A extends any[], R>(this: (this: T, arg0: A0, ...args: A) => R, thisArg: T, arg0: A0): (...args: A) => R
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, arg0: A0, ...args: A) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| arg0 | A0 | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (...args: A) =&gt; R |  |

## bind

```TypeScript
bind<T, A0, A1, A extends any[], R>(this: (this: T, arg0: A0, arg1: A1, ...args: A) => R, thisArg: T, arg0: A0, arg1: A1): (...args: A) => R
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, arg0: A0, arg1: A1, ...args: A) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| arg0 | A0 | 是 |  |
| arg1 | A1 | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (...args: A) =&gt; R |  |

## bind

```TypeScript
bind<T, A0, A1, A2, A extends any[], R>(this: (this: T, arg0: A0, arg1: A1, arg2: A2, ...args: A) => R, thisArg: T, arg0: A0, arg1: A1, arg2: A2): (...args: A) => R
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, arg0: A0, arg1: A1, arg2: A2, ...args: A) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| arg0 | A0 | 是 |  |
| arg1 | A1 | 是 |  |
| arg2 | A2 | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (...args: A) =&gt; R |  |

## bind

```TypeScript
bind<T, A0, A1, A2, A3, A extends any[], R>(this: (this: T, arg0: A0, arg1: A1, arg2: A2, arg3: A3, ...args: A) => R, thisArg: T, arg0: A0, arg1: A1, arg2: A2, arg3: A3): (...args: A) => R
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, arg0: A0, arg1: A1, arg2: A2, arg3: A3, ...args: A) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| arg0 | A0 | 是 |  |
| arg1 | A1 | 是 |  |
| arg2 | A2 | 是 |  |
| arg3 | A3 | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (...args: A) =&gt; R |  |

## bind

```TypeScript
bind<T, AX, R>(this: (this: T, ...args: AX[]) => R, thisArg: T, ...args: AX[]): (...args: AX[]) => R
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, ...args: AX[]) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| args | AX[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (...args: AX[]) =&gt; R |  |

## call

```TypeScript
call<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, ...args: A): R
```

Calls the function with the specified object as the this value and the specified rest arguments as the arguments.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-CallableFunction-call<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, ...args: A): R--><!--Device-CallableFunction-call<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, ...args: A): R-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | (this: T, ...args: A) =&gt; R | 是 |  |
| thisArg | T | 是 |  |
| args | A | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| R |  |

