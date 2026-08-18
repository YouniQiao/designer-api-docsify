# LinkedList

LinkedList is implemented based on the doubly linked list. Each node of the doubly linked list has references pointing to the previous element and the next element. When querying an element, the system traverses the list from the beginning or end.

**Since:** 23

<!--Device-unnamed-declare class LinkedList--><!--Device-unnamed-declare class LinkedList-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

returns an iterator. Each item of the iterator is a ArkTS Object

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LinkedList-$_iterator(): IterableIterator<T>--><!--Device-LinkedList-$_iterator(): IterableIterator<T>-End-->

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

<!--Device-LinkedList-[Symbol.iterator](): IterableIterator<T>--><!--Device-LinkedList-[Symbol.iterator](): IterableIterator<T>-End-->

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
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);

// Method 1:
for (let item of linkedList) {
  console.info("value:", item);
}
// value: 2
// value: 4
// value: 5
// value: 4

// Method 2:
let iter = linkedList[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value:", temp.value);
  temp = iter.next();
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

Adds an element at the end of this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-add(element: T): boolean--><!--Device-LinkedList-add(element: T): boolean-End-->

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
let linkedList = new LinkedList<string | number | boolean | object>();
let result = linkedList.add("a");
let result1 = linkedList.add(1);
let b = [1, 2, 3];
let result2 = linkedList.add(b);
class C {
  name: string = ''
  age: string = ''
}
let c: C = {name : "Dylan", age : "13"};
let result3 = linkedList.add(c);
let result4 = linkedList.add(false);
console.info("result = ", result4) // result =  true
```

## addFirst

```TypeScript
addFirst(element: T): void
```

Adds an element at the top of this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-addFirst(element: T): void--><!--Device-LinkedList-addFirst(element: T): void-End-->

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
let linkedList = new LinkedList<string | number | boolean | object>();
linkedList.addFirst("a");
linkedList.addFirst(1);
let b = [1, 2, 3];
linkedList.addFirst(b);
class C {
  name: string = ''
  age: string = ''
}
let c: C = {name : "Dylan", age : "13"};
linkedList.addFirst(c);
linkedList.addFirst(false);
let result = linkedList.get(2);
console.info("result:", result);  // result: 1,2,3
```

## clear

```TypeScript
clear(): void
```

Clears this LinkedList and sets its length to **0**.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-clear(): void--><!--Device-LinkedList-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
linkedList.clear();
let result = linkedList.has(2);
console.info("result:", result);  // result: false
```

## clone

```TypeScript
clone(): LinkedList<T>
```

Clones an instance identical to this **LinkedList** and returns it. The modification to the copy does not affect the original instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-clone(): LinkedList<T>--><!--Device-LinkedList-clone(): LinkedList<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [LinkedList](arkts-arkts-util-linkedlist-linkedlist-c.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.clone();
console.info("result:", result.has(4));  // result: true
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **LinkedList** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-constructor()--><!--Device-LinkedList-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

**Examples**

```TypeScript
let linkedList = new LinkedList<string | number | boolean | object>();
```

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

Converts this LinkedList into an array and returns the array.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-convertToArray(): Array<T>--><!--Device-LinkedList-convertToArray(): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.convertToArray();
console.info("result:", result);  // result: 2,4,5,4
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, LinkedList?: LinkedList<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse the elements in this LinkedList and obtain their indexes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-forEach(callbackFn: (value: T, index?: number, LinkedList?: LinkedList<T>) => void, thisArg?: Object): void--><!--Device-LinkedList-forEach(callbackFn: (value: T, index?: number, LinkedList?: LinkedList<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, LinkedList?: LinkedList & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
linkedList.forEach((value: number, index: number) => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

## forEach

```TypeScript
forEach(callbackFn: LinkedListForEachCb<T>): void
```

Replaces each element of this linkedList with the result of applying the operator to that element.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LinkedList-forEach(callbackFn: LinkedListForEachCb<T>): void--><!--Device-LinkedList-forEach(callbackFn: LinkedListForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [LinkedListForEachCb](arkts-arkts-linkedlistforeachcb-t.md)&lt;T&gt; | Yes |

## get

```TypeScript
get(index: number): T
```

Obtains an element at the specified position in this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-get(index: int): T--><!--Device-LinkedList-get(index: int): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(1);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.get(2);
console.info("result:", result);  // result: 5
```

## getFirst

```TypeScript
getFirst(): T
```

Obtains the first element in this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-getFirst(): T--><!--Device-LinkedList-getFirst(): T-End-->

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
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.getFirst();
console.info("result:", result);  // result: 2
```

## getIndexOf

```TypeScript
getIndexOf(element: T): number
```

Obtains the index of the first occurrence of the specified element in this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-getIndexOf(element: T): int--><!--Device-LinkedList-getIndexOf(element: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(1);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.getIndexOf(2);
console.info("result:", result);  // result: 0
```

## getLast

```TypeScript
getLast(): T
```

Obtains the last element in this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-getLast(): T--><!--Device-LinkedList-getLast(): T-End-->

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
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.getLast();
console.info("result:", result);  // result: 4
```

## getLastIndexOf

```TypeScript
getLastIndexOf(element: T): number
```

Obtains the index of the last occurrence of the specified element in this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-getLastIndexOf(element: T): int--><!--Device-LinkedList-getLastIndexOf(element: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(1);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.getLastIndexOf(2);
console.info("result:", result);  // result: 5
```

## has

```TypeScript
has(element: T): boolean
```

Checks whether this LinkedList has the specified element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-has(element: T): boolean--><!--Device-LinkedList-has(element: T): boolean-End-->

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
let linkedList = new LinkedList<string>();
linkedList.add("squirrel");
let result = linkedList.has("squirrel");
console.info("result:", result);  // result: true
```

## insert

```TypeScript
insert(index: number, element: T): void
```

Inserts an element at the specified position in this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-insert(index: int, element: T): void--><!--Device-LinkedList-insert(index: int, element: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| element | T | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let linkedList = new LinkedList<string | number | boolean | object>();
linkedList.insert(0, "A");
linkedList.insert(1, 0);
linkedList.insert(2, true);
let result = linkedList.get(1);
console.info("result:", result);  // result: 0
```

## remove

```TypeScript
remove(element: T): boolean
```

Removes the first occurrence of the specified element from this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-remove(element: T): boolean--><!--Device-LinkedList-remove(element: T): boolean-End-->

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
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.remove(2);
console.info("result:", result);  // result: true
```

## removeByIndex

```TypeScript
removeByIndex(index: number): T
```

Searches for an element based on its index and then removes it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-removeByIndex(index: number): T--><!--Device-LinkedList-removeByIndex(index: number): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.removeByIndex(2);
console.info("result:", result);  // result: 5
```

## removeByIndex

```TypeScript
removeByIndex(index: number): T | undefined
```

Removes and returns the element at the specified index in this linkedlist.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LinkedList-removeByIndex(index: int): T | undefined--><!--Device-LinkedList-removeByIndex(index: int): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200010](../errorcode-utils.md#10200010-empty-container) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## removeFirst

```TypeScript
removeFirst(): T
```

Removes the first element from this LinkedList.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-removeFirst(): T--><!--Device-LinkedList-removeFirst(): T-End-->

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
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.removeFirst();
console.info("result:", result);  // result: 2
```

## removeFirst

```TypeScript
removeFirst(): T | undefined
```

Retrieves and removes the head (first element) of this linkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LinkedList-removeFirst(): T | undefined--><!--Device-LinkedList-removeFirst(): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200010](../errorcode-utils.md#10200010-empty-container) |

## removeFirstFound

```TypeScript
removeFirstFound(element: T): boolean
```

Removes the first occurrence of the specified element from this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-removeFirstFound(element: T): boolean--><!--Device-LinkedList-removeFirstFound(element: T): boolean-End-->

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
| [10200010](../errorcode-utils.md#10200010-empty-container) |
| [10200017](../errorcode-utils.md#10200017-failed-to-delete-an-element-that-does-not-exist) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.removeFirstFound(4);
console.info("result:", result);  // result: true
```

## removeLast

```TypeScript
removeLast(): T
```

Removes the last element from this LinkedList.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-removeLast(): T--><!--Device-LinkedList-removeLast(): T-End-->

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
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.removeLast();
console.info("result:", result);  // result: 4
```

## removeLast

```TypeScript
removeLast(): T | undefined
```

Removes and returns the last element from this linkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LinkedList-removeLast(): T | undefined--><!--Device-LinkedList-removeLast(): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200010](../errorcode-utils.md#10200010-empty-container) |

## removeLastFound

```TypeScript
removeLastFound(element: T): boolean
```

Removes the last occurrence of the specified element from this LinkedList.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-removeLastFound(element: T): boolean--><!--Device-LinkedList-removeLastFound(element: T): boolean-End-->

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
| [10200010](../errorcode-utils.md#10200010-empty-container) |
| [10200017](../errorcode-utils.md#10200017-failed-to-delete-an-element-that-does-not-exist) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.removeLastFound(4);
console.info("result:", result);  // result: true
```

## set

```TypeScript
set(index: number, element: T): T
```

Replaces an element at the specified position in this LinkedList with a given element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-set(index: int, element: T): T--><!--Device-LinkedList-set(index: int, element: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200010](../errorcode-utils.md#10200010-empty-container) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let linkedList = new LinkedList<number | string>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.set(2, "b");
console.info("result:", result);  // result: b
```

## length

```TypeScript
length: number
```

Number of elements in a LinkedList.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinkedList-length: number--><!--Device-LinkedList-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
