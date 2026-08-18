# Deque

Double-ended queue (deque) is a sequence container implemented based on the queue data structure that follows the principles of First In First Out (FIFO) and Last In First Out (LIFO). It allows insertion and removal of elements at both the ends.

**Since:** 23

<!--Device-unnamed-declare class Deque--><!--Device-unnamed-declare class Deque-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns an iterator. Each item of the iterator is a ArkTS Object

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Deque-$_iterator(): IterableIterator<T>--><!--Device-Deque-$_iterator(): IterableIterator<T>-End-->

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-[Symbol.iterator](): IterableIterator<T>--><!--Device-Deque-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);

// Method 1:
for (let item of deque) {
  console.info("value:" + item);
}
/*
Output: 4
        5
        4
        2
*/

// Method 2:
let iter = deque[Symbol.iterator]();
let temp:IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value:" + temp.value);
  temp = iter.next();
}
/*
Output: 4
        5
        4
        2
*/
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Deque** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-constructor()--><!--Device-Deque-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

**Examples**

```TypeScript
let deque = new Deque<string | number | boolean | Object>();
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse each element in the **Deque** instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void--><!--Device-Deque-forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, deque?: Deque & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(3);
deque.insertFront(1);
deque.insertEnd(4);
deque.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
/*
Output: value:1 index:0
        value:2 index:1
        value:3 index:2
        value:4 index:3
*/
```

## forEach

```TypeScript
forEach(callbackFn: DequeForEachCb<T>): void
```

Iterates over elements in a generic Deque (double-ended queue) and executes a callback function for each element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Deque-forEach(callbackFn: DequeForEachCb<T>): void--><!--Device-Deque-forEach(callbackFn: DequeForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [DequeForEachCb](arkts-arkts-dequeforeachcb-t.md)&lt;T&gt; | Yes |

## getFirst

```TypeScript
getFirst(): T
```

Obtains the first element of this Deque.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-getFirst(): T--><!--Device-Deque-getFirst(): T-End-->

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

**Examples**

```TypeScript
let deque = new Deque<number>();
deque.insertEnd(2);
deque.insertEnd(4);
deque.insertFront(5);
deque.insertFront(4);
let result = deque.getFirst();
console.info("result:", result);  // result: 4
```

## getLast

```TypeScript
getLast(): T
```

Obtains the last element of this Deque.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-getLast(): T--><!--Device-Deque-getLast(): T-End-->

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

**Examples**

```TypeScript
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);
let result = deque.getLast();
console.info("result:", result);  // result: 2
```

## has

```TypeScript
has(element: T): boolean
```

Checks whether this Deque has the specified element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-has(element: T): boolean--><!--Device-Deque-has(element: T): boolean-End-->

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

**Examples**

```TypeScript
let deque = new Deque<string>();
deque.insertFront("squirrel");
let result = deque.has("squirrel");
console.info("result:", result);  // result: true
```

## insertEnd

```TypeScript
insertEnd(element: T): void
```

Inserts an element at the end of this Deque.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-insertEnd(element: T): void--><!--Device-Deque-insertEnd(element: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}

let deque = new Deque<string | number | boolean | Array<number> | C1>();
deque.insertEnd("a");
deque.insertEnd(1);
let b = [1, 2, 3];
deque.insertEnd(b);
let c: C1 = {name : "Dylan", age : "13"};
deque.insertEnd(c);
deque.insertEnd(false);
console.info("result:", deque[0]);  // result: a
```

## insertFront

```TypeScript
insertFront(element: T): void
```

Inserts an element at the front of this Deque.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-insertFront(element: T): void--><!--Device-Deque-insertFront(element: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}

let deque = new Deque<string | number | boolean | Array<number> | C1>();
deque.insertFront("a");
deque.insertFront(1);
let b = [1, 2, 3];
deque.insertFront(b);
let c: C1 = {name : "Dylan", age : "13"};
deque.insertFront(c);
deque.insertFront(false);
console.info("result:", deque[0]);  // result: false
```

## popFirst

```TypeScript
popFirst(): T
```

Removes the first element of this Deque.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-popFirst(): T--><!--Device-Deque-popFirst(): T-End-->

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

**Examples**

```TypeScript
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertEnd(5);
deque.insertFront(2);
deque.insertFront(4);
let result = deque.popFirst();
console.info("result:", result);  // result: 4
```

## popLast

```TypeScript
popLast(): T
```

Removes the last element of this Deque.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-popLast(): T--><!--Device-Deque-popLast(): T-End-->

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

**Examples**

```TypeScript
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(6);
deque.insertFront(5);
deque.insertFront(2);
deque.insertFront(4);
let result = deque.popLast();
console.info("result:", result);  // result: 6
```

## length

```TypeScript
length: number
```

Number of elements in a Deque.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-length: number--><!--Device-Deque-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
