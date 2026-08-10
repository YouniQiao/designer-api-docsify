# PromiseConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## [[Construct]]

```TypeScript
new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>
```

Creates a new Promise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>--><!--Device-PromiseConstructor-new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void): Promise<T>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| executor | (resolve: (value: T \| PromiseLike&lt;T&gt;) =&gt; void, reject: (reason?: any) =&gt; void) =&gt; void | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; |  |

## all

```TypeScript
all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>--><!--Device-PromiseConstructor-all<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: Awaited<T[P]> }>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;{ -readonly [P in keyof T]: Awaited&lt;T[P]&gt; }&gt; |  |

## race

```TypeScript
race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>
```

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>--><!--Device-PromiseConstructor-race<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T[number]&gt;&gt; |  |

## reject

```TypeScript
reject<T = never>(reason?: any): Promise<T>
```

Creates a new rejected promise for the provided reason.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-reject<T = never>(reason?: any): Promise<T>--><!--Device-PromiseConstructor-reject<T = never>(reason?: any): Promise<T>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; |  |

## resolve

```TypeScript
resolve(): Promise<void>
```

Creates a new resolved promise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-resolve(): Promise<void>--><!--Device-PromiseConstructor-resolve(): Promise<void>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; |  |

## resolve

```TypeScript
resolve<T>(value: T): Promise<Awaited<T>>
```

Creates a new resolved promise for the provided value.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-resolve<T>(value: T): Promise<Awaited<T>>--><!--Device-PromiseConstructor-resolve<T>(value: T): Promise<Awaited<T>>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;&gt; |  |

## resolve

```TypeScript
resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>
```

Creates a new resolved promise for the provided value.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-resolve<T>(value: T | PromiseLike<T>): Promise<Awaited<T>>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T \| PromiseLike&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;&gt; |  |

## prototype

```TypeScript
readonly prototype: Promise<any>
```

A reference to the prototype.

**类型：** Promise&lt;any&gt;

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-readonly prototype: Promise<any>--><!--Device-PromiseConstructor-readonly prototype: Promise<any>-End-->

