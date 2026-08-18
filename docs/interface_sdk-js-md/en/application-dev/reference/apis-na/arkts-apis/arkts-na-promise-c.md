# Promise

Represents the eventual completion or failure of an asynchronous operation.

**Inheritance/Implementation:** Promise implements PromiseLike<T>

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class Promise--><!--Device-unnamed-export class Promise-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## all

```TypeScript
static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>
```

Waits for all promises to resolve from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>--><!--Device-Promise-static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | FixedArray&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U \| undefined&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt;&gt; | Promise used to return Array&lt;Awaited<U>&gt;. |

## all

```TypeScript
static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>
```

Waits for all promises to resolve from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>--><!--Device-Promise-static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | Iterable&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt;&gt; | Promise used to return Array&lt;Awaited<U>&gt;. |

## allSettled

```TypeScript
static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):
        Promise<PromiseSettledResult<Awaited<U>>[]>
```

Waits for all promises to settle from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):        Promise<PromiseSettledResult<Awaited<U>>[]>--><!--Device-Promise-static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):        Promise<PromiseSettledResult<Awaited<U>>[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | FixedArray&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U \| undefined&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PromiseSettledResult](arkts-na-promisesettledresult-t.md)&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt;[]&gt; | Promise used to return PromiseSettledResult&lt;Awaited<U>&gt;[]. |

## allSettled

```TypeScript
static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>
```

Waits for all promises to settle from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>--><!--Device-Promise-static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | Iterable&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PromiseSettledResult](arkts-na-promisesettledresult-t.md)&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt;[]&gt; | Promise used to return PromiseSettledResult&lt;Awaited<U>&gt;[]. |

## any

```TypeScript
static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

Waits for any promise to resolve from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>--><!--Device-Promise-static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | FixedArray&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U \| undefined&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## any

```TypeScript
static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

Waits for any promise to resolve from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>--><!--Device-Promise-static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | Iterable&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## catch

```TypeScript
catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

Attaches a callback for the rejection of the Promise with no error parameter.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>--><!--Device-Promise-catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onRejected | () =&gt; PromiseLike&lt;U&gt; \| U | Yes | The callback to execute when the Promise is rejected. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T \| U&gt;&gt; | Promise used to return Awaited&lt;T \| U&gt;. |

## catch

```TypeScript
catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

Attaches a callback for the rejection of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>--><!--Device-Promise-catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onRejected | (error: Error) =&gt; PromiseLike&lt;U&gt; \| U | No | The callback to execute when the Promise is rejected. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T \| U&gt;&gt; | Promise used to return Awaited&lt;T \| U&gt;. |

## constructor

```TypeScript
constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,
        reject: (error: Error) => void) => void)
```

Constructs a new Promise with the given callback.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,        reject: (error: Error) => void) => void)--><!--Device-Promise-constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,        reject: (error: Error) => void) => void)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (resolve: (value: PromiseLike&lt;T&gt; \| T) =&gt; void,         reject: (error: Error) =&gt; void) =&gt; void | Yes | The callback to execute. |

## finally

```TypeScript
finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>
```

Attaches a callback that is invoked when the Promise is settled.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>--><!--Device-Promise-finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onFinally | () =&gt; PromiseLike&lt;U&gt; \| U | No | The callback to execute when the Promise is settled. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;&gt; | Promise used to return Awaited&lt;T&gt;. |

## race

```TypeScript
static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

Waits for the first promise to settle from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>--><!--Device-Promise-static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | FixedArray&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U \| undefined&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## race

```TypeScript
static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

Waits for the first promise to settle from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>--><!--Device-Promise-static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| promises | Iterable&lt;[PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U&gt; | Yes | The promises to wait for. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## reject

```TypeScript
static reject(): Promise<void>
```

Creates a rejected Promise with no value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static reject(): Promise<void>--><!--Device-Promise-static reject(): Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## reject

```TypeScript
static reject<U = never>(error: Error): Promise<Awaited<U>>
```

Creates a rejected Promise with the given error.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static reject<U = never>(error: Error): Promise<Awaited<U>>--><!--Device-Promise-static reject<U = never>(error: Error): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | Error | Yes | The error to reject with. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## resolve

```TypeScript
static resolve(): Promise<void>
```

Creates a resolved Promise with no value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static resolve(): Promise<void>--><!--Device-Promise-static resolve(): Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## resolve

```TypeScript
static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>
```

Creates a resolved Promise with the given value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>--><!--Device-Promise-static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PromiseLike](arkts-na-promise-promiselike-i.md)&lt;U&gt; \| U | Yes | The value to resolve with. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## then

```TypeScript
then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>
```

Attaches a callback for the resolution of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>--><!--Device-Promise-then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onFulfilled | () =&gt; PromiseLike&lt;U&gt; \| U | Yes | The callback to execute when the Promise is resolved. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## then

```TypeScript
then(_onFulfilled?: undefined): Promise<Awaited<T>>
```

Attaches no callback for the resolution of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-then(_onFulfilled?: undefined): Promise<Awaited<T>>--><!--Device-Promise-then(_onFulfilled?: undefined): Promise<Awaited<T>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| _onFulfilled | undefined | No | Undefined to skip fulfillment handling. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;&gt; | Promise used to return Awaited&lt;T&gt;. |

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Promise-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>--><!--Device-Promise-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onFulfilled | (value: T) =&gt; PromiseLike&lt;U&gt; \| U | Yes | The callback to execute when the Promise is resolved. |
| onRejected | (error: Error) =&gt; PromiseLike&lt;E&gt; \| E | No | The callback to execute when the Promise is rejected. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;U \| E&gt;&gt; | Promise used to return Awaited&lt;U \| E&gt;. |

