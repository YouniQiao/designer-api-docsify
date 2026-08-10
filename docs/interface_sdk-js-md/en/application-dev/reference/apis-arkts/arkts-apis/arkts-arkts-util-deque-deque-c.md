# Deque

Deque（double-ended queue）基于循环队列的数据结构实现，支持两端元素的插入和删除。Deque同时具备先进先出以及先进后出的特点，可根据操作端的不同同时作为队列和栈使用。当现有容量不足以容纳新插入的元素时，Deque会动态调整容量，每次扩容两倍，无需手动预设容量。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class Deque<T>--><!--Device-unnamed-declare class Deque<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Deque } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，每一项都是一个ArkTS对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Deque-$_iterator(): IterableIterator<T>--><!--Device-Deque-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，按插入顺序遍历Deque中的元素，迭代器每项为T类型的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-[Symbol.iterator](): IterableIterator<T>--><!--Device-Deque-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回一个迭代器，用于遍历Deque实例中的所有元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## Examples

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

Deque的构造函数，用于创建一个基于循环队列数据结构的空Deque实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-constructor()--><!--Device-Deque-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The Deque's constructor cannot be directly invoked. |

## Examples

```TypeScript
let deque = new Deque<string | number | boolean | Object>();
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void
```

通过回调函数遍历Deque实例中的每个元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void--><!--Device-Deque-forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: T, index?: number, deque?: Deque&lt;T&gt;) =&gt; void | Yes | 遍历每个元素时执行的回调函数，执行时的this值可通过thisArg参数指定。在回调函数执行过程中，不建议修改Deque（如插入或删除元素），否则可能导致遍历行为异常。 |
| thisArg | Object | No | callbackFn被调用时用作this值。当需要改变回调函数中的this指向时传入此参数；不传入时默认值为当前实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

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

通过回调函数遍历Deque实例中的每个元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Deque-forEach(callbackFn: DequeForEachCb<T>): void--><!--Device-Deque-forEach(callbackFn: DequeForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [DequeForEachCb](arkts-arkts-dequeforeachcb-t.md)&lt;T&gt; | Yes | 回调函数。 |

## getFirst

```TypeScript
getFirst(): T
```

获取Deque实例的头元素，不删除该元素。调用后，Deque的内容和长度不变。如需删除并返回首元素，请使用popFirst。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-getFirst(): T--><!--Device-Deque-getFirst(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回Deque实例的头元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

获取Deque实例的尾元素，不删除该元素。调用后，Deque的内容和长度不变。如需删除并返回尾元素，请使用popLast。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-getLast(): T--><!--Device-Deque-getLast(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回Deque实例的尾元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLast method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

判断此Deque中是否包含指定元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-has(element: T): boolean--><!--Device-Deque-has(element: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 指定的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果包含指定元素返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The has method cannot be bound. |

## Examples

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

在Deque尾部插入元素。插入成功后Deque的元素个数增加1。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-insertEnd(element: T): void--><!--Device-Deque-insertEnd(element: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 在尾部插入的元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The insertEnd method cannot be bound. |

## Examples

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

在Deque头部插入元素。插入成功后Deque的元素个数增加1。Deque在头部插入元素的效率高于ArrayList。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-insertFront(element: T): void--><!--Device-Deque-insertFront(element: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 在头部插入的元素，类型需与Deque实例化时指定的泛型类型T一致。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The insertFront method cannot be bound. |

## Examples

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

删除并返回Deque的首元素。删除成功后Deque的元素个数减少1。Deque在头部删除元素的效率高于ArrayList。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-popFirst(): T--><!--Device-Deque-popFirst(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回被删除的首元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The popFirst method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

删除并返回Deque的尾元素。删除成功后Deque的元素个数减少1。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-popLast(): T--><!--Device-Deque-popLast(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回被删除的尾元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The popLast method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

## [index: int]

```TypeScript
[index: int]: T
```

获取指定索引值对应位置的元素。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Deque-[index: int]: T--><!--Device-Deque-[index: int]: T-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Deque的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Deque-length: number--><!--Device-Deque-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

