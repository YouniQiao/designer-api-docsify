# PromiseConstructor

**Since:** -1

<!--Device-unnamed-interface PromiseConstructor--><!--Device-unnamed-interface PromiseConstructor-End-->

## Modules to Import

```TypeScript
```

## all

```TypeScript
all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

**Since:** -1

<!--Device-PromiseConstructor-all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>--><!--Device-PromiseConstructor-all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;{ -readonly [P in keyof T]: Awaited & lt;T[P] & gt; } & gt; |

## constructor

```TypeScript
new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>
```

Creates a new Promise.

**Since:** -1

<!--Device-PromiseConstructor-new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>--><!--Device-PromiseConstructor-new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| executor | (resolve: (value: T \| [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;T&gt;) =&gt; void, reject: (reason?: any) =&gt; void) =&gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

## race

```TypeScript
race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>
```

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

**Since:** -1

<!--Device-PromiseConstructor-race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>--><!--Device-PromiseConstructor-race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T[number]&gt;&gt; |

## reject

```TypeScript
reject<T = never>(reason?: any): Promise<T>
```

Creates a new rejected promise for the provided reason.

**Since:** -1

<!--Device-PromiseConstructor-reject<T = never>(reason?: any): Promise<T>--><!--Device-PromiseConstructor-reject<T = never>(reason?: any): Promise<T>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

## resolve

```TypeScript
resolve(): Promise<void>
```

Creates a new resolved promise.

**Since:** -1

<!--Device-PromiseConstructor-resolve(): Promise<void>--><!--Device-PromiseConstructor-resolve(): Promise<void>-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## resolve

```TypeScript
resolve<T>(value: T): Promise<Awaited<T>>
```

Creates a new resolved promise for the provided value.

**Since:** -1

<!--Device-PromiseConstructor-resolve<T>(value: T): Promise<Awaited<T>>--><!--Device-PromiseConstructor-resolve<T>(value: T): Promise<Awaited<T>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;&gt; |

## resolve

```TypeScript
resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>
```

Creates a new resolved promise for the provided value.

**Since:** -1

<!--Device-PromiseConstructor-resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T \| [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;&gt; |

## prototype

```TypeScript
readonly prototype: Promise<any>
```

A reference to the prototype.

**Type:** Promise&lt;any&gt;

**Since:** -1

<!--Device-PromiseConstructor-readonly prototype: Promise<any>--><!--Device-PromiseConstructor-readonly prototype: Promise<any>-End-->
