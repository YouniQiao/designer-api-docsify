# List

List is implemented based on the singly linked list. Each node has a reference pointing to the next element. When querying an element, the system traverses the list from the beginning.

**Since:** 23

<!--Device-unnamed-declare class List--><!--Device-unnamed-declare class List-End-->

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

<!--Device-List-$_iterator(): IterableIterator<T>--><!--Device-List-$_iterator(): IterableIterator<T>-End-->

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

<!--Device-List-[Symbol.iterator](): IterableIterator<T>--><!--Device-List-[Symbol.iterator](): IterableIterator<T>-End-->

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
let list = new List<number>();
list.add(2);
list.add(4);
list.add(5);
list.add(4);

// Method 1:
for (let item of list) {
  console.info("value: " + item);
}
// value: 2
// value: 4
// value: 5
// value: 4

// Method 2:
let iter = list[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value: " + temp.value);
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

Adds an element at the end of this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-add(element: T): boolean--><!--Device-List-add(element: T): boolean-End-->

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
let list = new List<string | number | boolean | object>();
let result1 = list.add("a");
let result2 = list.add(1);
let b = [1, 2, 3];
let result3 = list.add(b);
class C {
  name: string = ''
  age: string = ''
}
let c: C = {name : "Dylan", age : "13"};
let result4 = list.add(c);
let result5 = list.add(false);
console.info("result = ", result5) // result =  true
```

## clear

```TypeScript
clear(): void
```

Clears this List and sets its length to **0**.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-clear(): void--><!--Device-List-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
list.clear();
let result = list.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **List** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-constructor()--><!--Device-List-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

**Examples**

```TypeScript
let list = new List<string | number | boolean | object>();
```

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

Converts this List into an array and returns the array.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-convertToArray(): Array<T>--><!--Device-List-convertToArray(): Array<T>-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
let result = list.convertToArray();
console.info("result:", result);  // result: 2,4,5,4
```

## equal

```TypeScript
equal(obj: Object): boolean
```

Compares whether a specified object is equal to this List.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-equal(obj: Object): boolean--><!--Device-List-equal(obj: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Object | Yes |

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
let obj = new List<number>();
obj.add(2);
obj.add(4);
obj.add(5);
let result = list.equal(obj);
console.info("result:", result);  // result: true
```

## equal

```TypeScript
equal(obj: RecordData): boolean
```

Compares the specified object with this list for equality.if the object are the same as this list return true, otherwise return false.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-equal(obj: RecordData): boolean--><!--Device-List-equal(obj: RecordData): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse each element in the **List** instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void--><!--Device-List-forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, List?: List & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
list.forEach((value: number, index: number) => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

## forEach

```TypeScript
forEach(callbackFn: ListForEachCb<T>): void
```

Replaces each element of this list with the result of applying the operator to that element.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-forEach(callbackFn: ListForEachCb<T>): void--><!--Device-List-forEach(callbackFn: ListForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [ListForEachCb](arkts-arkts-listforeachcb-t.md)&lt;T&gt; | Yes |

## get

```TypeScript
get(index: number): T
```

Obtains the element at the specified position in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-get(index: int): T--><!--Device-List-get(index: int): T-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(2);
list.add(1);
list.add(2);
list.add(4);
let result = list.get(2);
console.info("result:", result);  // result: 5
```

## getFirst

```TypeScript
getFirst(): T
```

Obtains the first element in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getFirst(): T--><!--Device-List-getFirst(): T-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
let result = list.getFirst();
console.info("result:", result);  // result: 2
```

## getIndexOf

```TypeScript
getIndexOf(element: T): number
```

Obtains the index of the first occurrence of the specified element in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getIndexOf(element: T): int--><!--Device-List-getIndexOf(element: T): int-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(2);
list.add(1);
list.add(2);
list.add(4);
let result = list.getIndexOf(2);
console.info("result:", result); // result: 0
```

## getLast

```TypeScript
getLast(): T
```

Obtains the last element in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getLast(): T--><!--Device-List-getLast(): T-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
let result = list.getLast();
console.info("result:", result);  // result: 4
```

## getLastIndexOf

```TypeScript
getLastIndexOf(element: T): number
```

Obtains the index of the last occurrence of the specified element in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getLastIndexOf(element: T): int--><!--Device-List-getLastIndexOf(element: T): int-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(2);
list.add(1);
list.add(2);
list.add(4);
let result = list.getLastIndexOf(2);
console.info("result:", result); // result: 5
```

## getSubList

```TypeScript
getSubList(fromIndex: number, toIndex: number): List<T>
```

Obtains elements within a range in this List, including the element at the start position but not that at the end position, and returns these elements as a new **List** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getSubList(fromIndex: int, toIndex: int): List<T>--><!--Device-List-getSubList(fromIndex: int, toIndex: int): List<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let list = new List<number>()
list.add(2);
list.add(4);
list.add(6);
list.add(8);
let result = list.getSubList(1, 3);
console.info("result:", result.convertToArray());  // result: 4,6
```

## has

```TypeScript
has(element: T): boolean
```

Checks whether this List has the specified element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-has(element: T): boolean--><!--Device-List-has(element: T): boolean-End-->

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
let list = new List<string>();
list.add("squirrel");
let result = list.has("squirrel");
console.info("result:", result);  // result: true
```

## insert

```TypeScript
insert(element: T, index: number): void
```

Inserts an element at the specified position in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-insert(element: T, index: int): void--><!--Device-List-insert(element: T, index: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |
| index | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let list = new List<string | number | boolean>();
list.insert("A", 0);
list.insert(0, 1);
list.insert(true, 2);
console.info("result:", list.get(1));  // result: 0
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this List is empty (contains no element).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-isEmpty(): boolean--><!--Device-List-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
let result = list.isEmpty();
console.info("result:", result);  // result: false
```

## remove

```TypeScript
remove(element: T): boolean
```

Removes the first occurrence of the specified element from this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-remove(element: T): boolean--><!--Device-List-remove(element: T): boolean-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
let result = list.remove(2);
console.info("result:", result);  // result: true
```

## removeByIndex

```TypeScript
removeByIndex(index: number): T
```

Searches for an element based on its index and then removes it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-removeByIndex(index: number): T--><!--Device-List-removeByIndex(index: number): T-End-->

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
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(2);
list.add(4);
let result = list.removeByIndex(2);
console.info("result:", result);  // result: 5
```

## removeByIndex

```TypeScript
removeByIndex(index: number): T | undefined
```

Find the corresponding element according to the index.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-removeByIndex(index: int): T | undefined--><!--Device-List-removeByIndex(index: int): T | undefined-End-->

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
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void
```

Replaces all elements in this List with new elements, and returns the new ones.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void--><!--Device-List-replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, list?: List & lt;T & gt;) = & gt; T | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let list = new List<number>()
list.add(2);
list.add(4);
list.add(5);
list.add(4);
list.replaceAllElements((value: number) => {
  // Add the user operation logic based on the actual scenario.
  if (value === 5) {
    return value * 2;
  }
  return value;
});

console.info("result:", list.get(2));  // result: 10
```

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: ListReplaceCb<T>): void
```

Replaces each element of this list with the result of applying the operator to that element.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-replaceAllElements(callbackFn: ListReplaceCb<T>): void--><!--Device-List-replaceAllElements(callbackFn: ListReplaceCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [ListReplaceCb](arkts-arkts-listreplacecb-t.md)&lt;T&gt; | Yes |

## set

```TypeScript
set(index: number, element: T): T
```

Replaces an element at the specified position in this List with a given element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-set(index: int, element: T): T--><!--Device-List-set(index: int, element: T): T-End-->

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
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let list = new List<number | string>();
list.add(2);
list.add(4);
list.add(5);
list.add(4);
let result = list.set(2, "b");
console.info("result:", JSON.stringify(list));  // result: {"0":2,"1":4,"2":"b","3":4}
```

## sort

```TypeScript
sort(comparator: ListComparatorFn<T>): void
```

Sorts elements in this List.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-sort(comparator: ListComparatorFn<T>): void--><!--Device-List-sort(comparator: ListComparatorFn<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| comparator | [ListComparatorFn](arkts-arkts-listcomparatorfn-t.md)&lt;T&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let list = new List<number>()
list.add(2);
list.add(1);
list.add(3);
list.add(4);
list.sort((a: number, b: number) => a - b);  // The elements are sorted in ascending order.
console.info("result:", list.convertToArray());  // result: 1,2,3,4

list.sort((a: number, b: number) => b - a);  // The elements are sorted in descending order.
console.info("result:", list.convertToArray());  // result: 4,3,2,1
```

## length

```TypeScript
length: number
```

Number of elements in a List.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-length: number--><!--Device-List-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
