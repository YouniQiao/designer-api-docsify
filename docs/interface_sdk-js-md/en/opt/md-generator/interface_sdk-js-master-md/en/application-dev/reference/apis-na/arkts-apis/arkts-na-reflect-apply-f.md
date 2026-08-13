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

**Since:** -1

**Deprecated since:** -1

<!--Device-Reflect-function apply<T, A extends readonly any[], R>(        target: (this: T, ...args: A) => R,        thisArgument: T,        argumentsList: Readonly<A>,    ): R--><!--Device-Reflect-function apply<T, A extends readonly any[], R>(        target: (this: T, ...args: A) => R,        thisArgument: T,        argumentsList: Readonly<A>,    ): R-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | (this: T, ...args: A) = & gt; R | Yes |
| thisArgument | T | Yes |
| argumentsList | [Readonly](arkts-na-readonly-t.md)&lt;A&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| R |


## apply

```TypeScript
function apply(target: Function, thisArgument: any, argumentsList: ArrayLike<any>): any
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Reflect-function apply(target: Function, thisArgument: any, argumentsList: ArrayLike<any>): any--><!--Device-Reflect-function apply(target: Function, thisArgument: any, argumentsList: ArrayLike<any>): any-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | Function | Yes |
| thisArgument | any | Yes |
| argumentsList | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;any&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |
