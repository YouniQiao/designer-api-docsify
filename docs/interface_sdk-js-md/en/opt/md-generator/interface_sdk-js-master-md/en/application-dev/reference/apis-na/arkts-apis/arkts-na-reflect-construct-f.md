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

**Since:** -1

**Deprecated since:** -1

<!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R--><!--Device-Reflect-function construct<A extends readonly any[], R>(        target: new (...args: A) => R,        argumentsList: Readonly<A>,        newTarget?: new (...args: any) => any,    ): R-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | new (...args: A) = & gt; R | Yes |
| argumentsList | [Readonly](arkts-na-readonly-t.md)&lt;A&gt; | Yes |
| newTarget | new (...args: any) = & gt; any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| R |


## construct

```TypeScript
function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Reflect-function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any--><!--Device-Reflect-function construct(target: Function, argumentsList: ArrayLike<any>, newTarget?: Function): any-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | Function | Yes |
| argumentsList | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;any&gt; | Yes |
| newTarget | Function | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |
