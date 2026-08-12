# CallableFunction

## apply

```TypeScript
apply<T, R>(this: (this: T) => R, thisArg: T): R
```

Calls the function with the specified object as the this value and the elements of specified array as the arguments.

<!--Device-CallableFunction-apply<T, R>(this: (this: T) => R, thisArg: T): R--><!--Device-CallableFunction-apply<T, R>(this: (this: T) => R, thisArg: T): R-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T) = & gt; R | Yes |
| thisArg | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| R |

## apply

```TypeScript
apply<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, args: A): R
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, ...args: A) = & gt; R | Yes |
| thisArg | T | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| R |

## bind

```TypeScript
bind<T>(this: T, thisArg: ThisParameterType<T>): OmitThisParameter<T>
```

For a given function, creates a bound function that has the same body as the original function.The this object of the bound function is associated with the specified object, and has the specified initial parameters.

<!--Device-CallableFunction-bind<T>(this: T, thisArg: ThisParameterType<T>): OmitThisParameter<T>--><!--Device-CallableFunction-bind<T>(this: T, thisArg: ThisParameterType<T>): OmitThisParameter<T>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | T | Yes |
| thisArg | [ThisParameterType](arkts-thisparametertype-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OmitThisParameter](arkts-omitthisparameter-t.md)&lt;T&gt; |

## bind

```TypeScript
bind<T, A0, A extends any[], R>(this: (this: T, arg0: A0, ...args: A) => R, thisArg: T, arg0: A0): (...args: A) => R
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, arg0: A0, ...args: A) = & gt; R | Yes |
| thisArg | T | Yes |
| arg0 | A0 | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| (...args: A) = & gt; R |

## bind

```TypeScript
bind<T, A0, A1, A extends any[], R>(this: (this: T, arg0: A0, arg1: A1, ...args: A) => R, thisArg: T, arg0: A0, arg1: A1): (...args: A) => R
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, arg0: A0, arg1: A1, ...args: A) = & gt; R | Yes |
| thisArg | T | Yes |
| arg0 | A0 | Yes |
| arg1 | A1 | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| (...args: A) = & gt; R |

## bind

```TypeScript
bind<T, A0, A1, A2, A extends any[], R>(this: (this: T, arg0: A0, arg1: A1, arg2: A2, ...args: A) => R, thisArg: T, arg0: A0, arg1: A1, arg2: A2): (...args: A) => R
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, arg0: A0, arg1: A1, arg2: A2, ...args: A) = & gt; R | Yes |
| thisArg | T | Yes |
| arg0 | A0 | Yes |
| arg1 | A1 | Yes |
| arg2 | A2 | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| (...args: A) = & gt; R |

## bind

```TypeScript
bind<T, A0, A1, A2, A3, A extends any[], R>(this: (this: T, arg0: A0, arg1: A1, arg2: A2, arg3: A3, ...args: A) => R, thisArg: T, arg0: A0, arg1: A1, arg2: A2, arg3: A3): (...args: A) => R
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, arg0: A0, arg1: A1, arg2: A2, arg3: A3, ...args: A) = & gt; R | Yes |
| thisArg | T | Yes |
| arg0 | A0 | Yes |
| arg1 | A1 | Yes |
| arg2 | A2 | Yes |
| arg3 | A3 | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| (...args: A) = & gt; R |

## bind

```TypeScript
bind<T, AX, R>(this: (this: T, ...args: AX[]) => R, thisArg: T, ...args: AX[]): (...args: AX[]) => R
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, ...args: AX[]) = & gt; R | Yes |
| thisArg | T | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | AX[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| (...args: AX[]) = & gt; R |

## call

```TypeScript
call<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, ...args: A): R
```

Calls the function with the specified object as the this value and the specified rest arguments as the arguments.

<!--Device-CallableFunction-call<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, ...args: A): R--><!--Device-CallableFunction-call<T, A extends any[], R>(this: (this: T, ...args: A) => R, thisArg: T, ...args: A): R-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | (this: T, ...args: A) = & gt; R | Yes |
| thisArg | T | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| R |
