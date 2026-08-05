# construct

## construct

```TypeScript
function construct<A extends readonly any[], R>(
        target: new (...args: A) => R,
        argumentsList: Readonly<A>,
        newTarget?: new (...args: any) => any,
    ): R
```

Constructs the target with the elements of specified array as the arguments and the specified constructor as the \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ value.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R--><!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | new (...args: A) =&gt; R | Yes |  |
| argumentsList | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;A&gt; | Yes |  |
| newTarget | new (...args: any) =&gt; any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| R |  |


## construct

```TypeScript
function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any--><!--Device-Reflect-function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | Function | Yes |  |
| argumentsList | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;any&gt; | Yes |  |
| newTarget | Function | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| any |  |

