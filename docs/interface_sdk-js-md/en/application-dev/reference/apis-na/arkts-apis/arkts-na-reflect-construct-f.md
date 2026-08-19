# construct

## Modules to Import

```TypeScript
```

## construct

```TypeScript
function construct<A extends readonly any[], R>(
        target: new (...args: A) => R,
        argumentsList: Readonly<A>,
        newTarget?: new (...args: any) => any,
    ): R
```

Constructs the target with the elements of specified array as the arguments and the specified constructor as the `new.target` value.

**Since:** -1

<!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R--><!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | new (...args: A) =&gt; R | Yes |  |
| argumentsList | [Readonly](arkts-na-readonly-t.md)&lt;A&gt; | Yes |  |
| newTarget | new (...args: any) =&gt; any | No |  |

**Return value:**

| Type | Description |
| --- | --- |

## construct

```TypeScript
function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any
```

**Since:** -1

<!--Device-Reflect-function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any--><!--Device-Reflect-function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | Function | Yes |  |
| argumentsList | ArrayLike&lt;any&gt; | Yes |  |
| newTarget | Function | No |  |

**Return value:**

| Type | Description |
| --- | --- |
