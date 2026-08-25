# Promise

Represents the eventual completion or failure of an asynchronous operation.

**Inheritance/Implementation:** Promise implements PromiseLike<T>

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Awaited & lt;U & gt; & gt; & gt; |

## all

```TypeScript
static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>
```

Waits for all promises to resolve from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Awaited & lt;U & gt; & gt; & gt; |

## allSettled

```TypeScript
static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):
        Promise<PromiseSettledResult<Awaited<U>>[]>
```

Waits for all promises to settle from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PromiseSettledResult](arkts-arkts-promisesettledresult-t.md)&lt;Awaited&lt;U&gt;&gt;[]&gt; |

## allSettled

```TypeScript
static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>
```

Waits for all promises to settle from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PromiseSettledResult](arkts-arkts-promisesettledresult-t.md)&lt;Awaited&lt;U&gt;&gt;[]&gt; |

## any

```TypeScript
static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

Waits for any promise to resolve from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## any

```TypeScript
static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

Waits for any promise to resolve from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## catch

```TypeScript
catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

Attaches a callback for the rejection of the Promise with no error parameter.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onRejected | () = & gt; PromiseLike & lt;U & gt; \ | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;T \ | U & gt; & gt; | Promise used to return Awaited & lt;T \ |

## catch

```TypeScript
catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

Attaches a callback for the rejection of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onRejected | (error: Error) = & gt; PromiseLike & lt;U & gt; \ | U | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;T \ | U & gt; & gt; | Promise used to return Awaited & lt;T \ |

## constructor

```TypeScript
constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,
        reject: (error: Error) => void) => void)
```

Constructs a new Promise with the given callback.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (resolve: (value: PromiseLike & lt;T & gt; \ | T) = & gt; void,         reject: (error: Error) = & gt; void) = & gt; void | Yes |

## finally

```TypeScript
finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>
```

Attaches a callback that is invoked when the Promise is settled.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onFinally | () = & gt; PromiseLike & lt;U & gt; \ | U | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;T & gt; & gt; |

## race

```TypeScript
static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

Waits for the first promise to settle from a FixedArray.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## race

```TypeScript
static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

Waits for the first promise to settle from an Iterable.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## reject

```TypeScript
static reject(): Promise<void>
```

Creates a rejected Promise with no value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## reject

```TypeScript
static reject<U = never>(error: Error): Promise<Awaited<U>>
```

Creates a rejected Promise with the given error.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| error | Error | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## resolve

```TypeScript
static resolve(): Promise<void>
```

Creates a resolved Promise with no value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## resolve

```TypeScript
static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>
```

Creates a resolved Promise with the given value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | PromiseLike & lt;U & gt; \ | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## then

```TypeScript
then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>
```

Attaches a callback for the resolution of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onFulfilled | () = & gt; PromiseLike & lt;U & gt; \ | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## then

```TypeScript
then(_onFulfilled?: undefined): Promise<Awaited<T>>
```

Attaches no callback for the resolution of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| _onFulfilled | undefined | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;T & gt; & gt; |

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onFulfilled | (value: T) = & gt; PromiseLike & lt;U & gt; \ | U | Yes |
| onRejected | (error: Error) = & gt; PromiseLike & lt;E & gt; \ | E | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Awaited & lt;U \ | E & gt; & gt; | Promise used to return Awaited & lt;U \ |
