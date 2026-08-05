# apply

## apply

```TypeScript
function apply<T, A extends readonly any[], R>(
        target: (this: T, ...args: A) => R,
        thisArgument: T,
        argumentsList: Readonly<A>,
    ): R
```

Calls the function with the specified object as the this value and the elements of specified array as the arguments.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function apply<T, A extends readonly any[], R>(        target: (this: T, ...args: A) => R,        thisArgument: T,        argumentsList: Readonly<A>,    ): R--><!--Device-Reflect-function apply<T, A extends readonly any[], R>(        target: (this: T, ...args: A) => R,        thisArgument: T,        argumentsList: Readonly<A>,    ): R-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | (this: T, ...args: A) =&gt; R | Yes |  |
| thisArgument | T | Yes |  |
| argumentsList | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;A&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| R |  |


## apply

```TypeScript
function apply(target: Function, thisArgument: any, argumentsList: ArrayLike<any>): any
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function apply(target: Function, thisArgument: any, argumentsList: ArrayLike<any>): any--><!--Device-Reflect-function apply(target: Function, thisArgument: any, argumentsList: ArrayLike<any>): any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | Function | Yes |  |
| thisArgument | any | Yes |  |
| argumentsList | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;any&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| any |  |

