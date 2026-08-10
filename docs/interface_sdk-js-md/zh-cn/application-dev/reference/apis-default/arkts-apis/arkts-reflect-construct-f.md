# construct

## construct

```TypeScript
function construct<A extends readonly any[], R>(
        target: new (...args: A) => R,
        argumentsList: Readonly<A>,
        newTarget?: new (...args: any) => any,
    ): R
```

Constructs the target with the elements of specified array as the arguments and the specified constructor as the `new.target` value.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R--><!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | new (...args: A) =&gt; R | 是 |  |
| argumentsList | [Readonly](arkts-readonly-t.md)&lt;A&gt; | 是 |  |
| newTarget | new (...args: any) =&gt; any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| R |  |


## construct

```TypeScript
function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | Function | 是 |  |
| argumentsList | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;any&gt; | 是 |  |
| newTarget | Function | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

