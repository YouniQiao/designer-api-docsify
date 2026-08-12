# PromiseConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Construct]]

```TypeScript
new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>
```

Creates a new Promise.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>--><!--Device-PromiseConstructor-new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| executor | (resolve: (value: T \| PromiseLike&lt;T&gt;) =&gt; void, reject: (reason?: any) =&gt; void) =&gt; void | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; |  |

## all

```TypeScript
all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>--><!--Device-PromiseConstructor-all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;{ -readonly [P in keyof T]: Awaited&lt;T[P]&gt; }&gt; |  |

## race

```TypeScript
race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>
```

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>--><!--Device-PromiseConstructor-race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-awaited-t.md)&lt;T[number]&gt;&gt; |  |

## reject

```TypeScript
reject<T = never>(reason?: any): Promise<T>
```

Creates a new rejected promise for the provided reason.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-reject<T = never>(reason?: any): Promise<T>--><!--Device-PromiseConstructor-reject<T = never>(reason?: any): Promise<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; |  |

## resolve

```TypeScript
resolve(): Promise<void>
```

Creates a new resolved promise.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-resolve(): Promise<void>--><!--Device-PromiseConstructor-resolve(): Promise<void>-End-->

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

## resolve

```TypeScript
resolve<T>(value: T): Promise<Awaited<T>>
```

Creates a new resolved promise for the provided value.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-resolve<T>(value: T): Promise<Awaited<T>>--><!--Device-PromiseConstructor-resolve<T>(value: T): Promise<Awaited<T>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-awaited-t.md)&lt;T&gt;&gt; |  |

## resolve

```TypeScript
resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>
```

Creates a new resolved promise for the provided value.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T \| PromiseLike&lt;T&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-awaited-t.md)&lt;T&gt;&gt; |  |

## prototype

```TypeScript
readonly prototype: Promise<any>
```

A reference to the prototype.

**Type:** Promise&lt;any&gt;

**ArkTS mode:** ArkTS-Dyn only

<!--Device-PromiseConstructor-readonly prototype: Promise<any>--><!--Device-PromiseConstructor-readonly prototype: Promise<any>-End-->

