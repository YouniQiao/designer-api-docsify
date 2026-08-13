# Queue

Queue follows the principle of First In First Out (FIFO). It supports insertion of elements at the end and removal from the front of the queue. Queue is implemented based on the queue data structure.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class Queue--><!--Device-unnamed-declare class Queue-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Queue } from '@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

returns an iterator. Each item of the iterator is a ArkTS Object

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Queue-$_iterator(): IterableIterator<T>--><!--Device-Queue-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

returns an iterator.Each item of the iterator is a Javascript Object

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-[Symbol.iterator](): IterableIterator<T>--><!--Device-Queue-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(4);

// Method 1:
for (let value of queue) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// Method 2:
let iter = queue[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next().value;
while(temp != undefined) {
  console.info("value: " + temp);
  temp = iter.next().value;
}
// value: 2
// value: 4
// value: 5
// value: 4
```

## add

```TypeScript
add(element: T): boolean
```

Adds an element at the end of this Queue.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-add(element: T): boolean--><!--Device-Queue-add(element: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}
let queue = new Queue<number | string | C1 | number[]>();
let result = queue.add("a");
let result1 = queue.add(1);
let b = [1, 2, 3];
let result2 = queue.add(b);
let c : C1 = {name : "Dylan", age : "13"};
let result3 = queue.add(c);
console.info("result:", queue.length);  // result: 4
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Queue** instance.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-constructor()--><!--Device-Queue-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## Examples

```TypeScript
let queue = new Queue<number | string | Object>();
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, Queue?: Queue<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse each element in the **Queue** instance.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-forEach(callbackFn: (value: T, index?: number, Queue?: Queue<T>) => void, thisArg?: Object): void--><!--Device-Queue-forEach(callbackFn: (value: T, index?: number, Queue?: Queue<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, Queue?: Queue & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(4);
queue.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

## forEach

```TypeScript
forEach(callbackFn: QueueForEachCb<T>): void
```

Executes a provided function once for each value in the queue object.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Queue-forEach(callbackFn: QueueForEachCb<T>): void--><!--Device-Queue-forEach(callbackFn: QueueForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [QueueForEachCb](arkts-arkts-queueforeachcb-t.md)&lt;T&gt; | Yes |

## getFirst

```TypeScript
getFirst(): T
```

Obtains the first element of this Queue.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-getFirst(): T--><!--Device-Queue-getFirst(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200010](../errorcode-utils.md#10200010-empty-container) |

## Examples

```TypeScript
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(2);
let result = queue.getFirst();
console.info("result:", result);  // result: 2
```

## pop

```TypeScript
pop(): T
```

Removes the first element from this Queue.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-pop(): T--><!--Device-Queue-pop(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200010](../errorcode-utils.md#10200010-empty-container) |

## Examples

```TypeScript
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(2);
queue.add(4);
let result = queue.pop();
console.info("result:", result);  // result: 2
```

## length

```TypeScript
length: number
```

Number of elements in a Queue.

**Type:** number

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Queue-length: number--><!--Device-Queue-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
