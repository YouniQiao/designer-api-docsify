# List

List底层通过单向链表实现，每个节点有一个指向后一个元素的引用。查询元素必须从头遍历，因此查询效率低，但插入和删除效率高。List允许元素为null。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class List<T>--><!--Device-unnamed-declare class List<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { List } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，每一项都是一个ArkTS对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-$_iterator(): IterableIterator<T>--><!--Device-List-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，用于遍历List中的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-[Symbol.iterator](): IterableIterator<T>--><!--Device-List-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回一个迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## Examples

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

在List尾部插入元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-add(element: T): boolean--><!--Device-List-add(element: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 待添加的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 插入成功返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The add method cannot be bound. |

## Examples

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

清除List中的所有元素，并将length置为0。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-clear(): void--><!--Device-List-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

## Examples

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

List的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-constructor()--><!--Device-List-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The List's constructor cannot be directly invoked. |

## Examples

```TypeScript
let list = new List<string | number | boolean | object>();
```

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

把当前List实例转换成数组并返回。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-convertToArray(): Array<T>--><!--Device-List-convertToArray(): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | 返回转换后的数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The convertToArray method cannot be bound. |

## Examples

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

比较指定对象与此List是否相等。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-equal(obj: Object): boolean--><!--Device-List-equal(obj: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Object | Yes | 用来比较的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果对象与此列表相同返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The equal method cannot be bound. |

## Examples

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

判断指定对象与此list是否相同。如果对象与此list相同，返回true，否则返回false。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-equal(obj: RecordData): boolean--><!--Device-List-equal(obj: RecordData): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | Yes | 用于与此list比较的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | boolean类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The equal method cannot be bound. |

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void
```

在遍历List实例对象中每一个元素的过程中，对每个元素执行回调函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void--><!--Device-List-forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: T, index?: number, List?: List&lt;T&gt;) =&gt; void | Yes | 回调函数。 callbackFn（必填）接受最多三个参数的函数。 value 当前遍历到的元素。 index 当前遍历到的下标值，默认值为0。 List 当前调用forEach方法的实例对象，默认值为当前实例对象。 |
| thisArg | Object | No | callbackFn被调用时用作this值，默认值为当前实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

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

用对该元素应用操作符的结果替换list中的每个元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-forEach(callbackFn: ListForEachCb<T>): void--><!--Device-List-forEach(callbackFn: ListForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [ListForEachCb](arkts-arkts-listforeachcb-t.md)&lt;T&gt; | Yes | 回调函数。 |

## get

ArkTS-Dyn:
```TypeScript
get(index: number): T
```

ArkTS-Sta:
```TypeScript
get(index: int): T
```

根据下标获取List中的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-get(index: int): T--><!--Device-List-get(index: int): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要查找的下标。需要小于等于int32_max即2147483647。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 根据下标查找到的元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The get method cannot be bound. |
| 10200001 | The value of index is out of range.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

获取List实例中的第一个元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getFirst(): T--><!--Device-List-getFirst(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回实例的第一个元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

ArkTS-Dyn:
```TypeScript
getIndexOf(element: T): number
```

ArkTS-Sta:
```TypeScript
getIndexOf(element: T): int
```

查找指定元素第一次出现的下标，查找失败返回-1。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getIndexOf(element: T): int--><!--Device-List-getIndexOf(element: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 指定元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回第一次找到指定元素的下标，没有找到返回-1。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getIndexOf method cannot be bound. |

## Examples

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

获取List实例中的最后一个元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getLast(): T--><!--Device-List-getLast(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回实例的最后一个元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLast method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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

ArkTS-Dyn:
```TypeScript
getLastIndexOf(element: T): number
```

ArkTS-Sta:
```TypeScript
getLastIndexOf(element: T): int
```

查找指定元素最后一次出现的下标值，查找失败返回-1。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getLastIndexOf(element: T): int--><!--Device-List-getLastIndexOf(element: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 指定元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回指定元素最后一次出现的下标值，没有找到返回-1。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLastIndexOf method cannot be bound. |

## Examples

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

ArkTS-Dyn:
```TypeScript
getSubList(fromIndex: number, toIndex: number): List<T>
```

ArkTS-Sta:
```TypeScript
getSubList(fromIndex: int, toIndex: int): List<T>
```

根据下标截取List中的一段元素，并返回这一段List实例，包括起始值但不包括终止值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-getSubList(fromIndex: int, toIndex: int): List<T>--><!--Device-List-getSubList(fromIndex: int, toIndex: int): List<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 起始下标。 |
| toIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 终止下标。 |

**Return value:**

| Type | Description |
| --- | --- |
| [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; | 返回List对象实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getSubList method cannot be bound. |
| 10200001 | The value of fromIndex or toIndex is out of range. |

## Examples

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

判断List中是否包含指定元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-has(element: T): boolean--><!--Device-List-has(element: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 指定元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定元素返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The has method cannot be bound. |

## Examples

```TypeScript
let list = new List<string>();
list.add("squirrel");
let result = list.has("squirrel");
console.info("result:", result);  // result: true
```

## insert

ArkTS-Dyn:
```TypeScript
insert(element: T, index: number): void
```

ArkTS-Sta:
```TypeScript
insert(element: T, index: int): void
```

在长度范围内任意位置插入指定元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-insert(element: T, index: int): void--><!--Device-List-insert(element: T, index: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 待插入元素。 |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 插入的位置索引，可插入位置区间为[0, List.length]，需要小于等于int32_max即2147483647。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The insert method cannot be bound. |
| 10200001 | The value of index is out of range. |

## Examples

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

判断List是否为空。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-isEmpty(): boolean--><!--Device-List-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 为空返回true，不为空返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The isEmpty method cannot be bound. |

## Examples

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

删除查找到的第一个指定的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-remove(element: T): boolean--><!--Device-List-remove(element: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | T | Yes | 指定元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 删除成功返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

## Examples

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

根据元素的下标值查找元素，并将其删除。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-removeByIndex(index: number): T--><!--Device-List-removeByIndex(index: number): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 指定元素的下标值，取值范围[0, List.length-1]，需要小于等于int32_max即2147483647。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回被删除的元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The removeByIndex method cannot be bound. |
| 10200001 | The value of index is out of range. |

## Examples

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
removeByIndex(index: int): T | undefined
```

根据索引查找对应元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-removeByIndex(index: int): T | undefined--><!--Device-List-removeByIndex(index: int): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 待查找元素的下标。 该值为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | T类型的值，如果下标超出范围（大于等于length或小于0），抛出异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "index" is out of range. It must be >= 0 && <= \\${length - 1}. Received value is: \\${index} |

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void
```

遍历List中的元素，并用回调函数返回的新值替换原List中的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void--><!--Device-List-replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: T, index?: number, list?: List&lt;T&gt;) =&gt; T | Yes | 回调函数。 callbackFn（必填）接受最多三个参数的函数。 value 当前遍历到的元素。 index 当前遍历到的下标值，默认值为0。 list 当前调用replaceAllElements方法的实例对象，默认值为当前实例对象。 |
| thisArg | Object | No | callbackFn被调用时用作this值，默认值为当前实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The replaceAllElements method cannot be bound. |

## Examples

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

用对该元素应用操作符的结果替换list中的每个元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-replaceAllElements(callbackFn: ListReplaceCb<T>): void--><!--Device-List-replaceAllElements(callbackFn: ListReplaceCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [ListReplaceCb](arkts-arkts-listreplacecb-t.md)&lt;T&gt; | Yes | 回调函数。 |

## set

ArkTS-Dyn:
```TypeScript
set(index: number, element: T): T
```

ArkTS-Sta:
```TypeScript
set(index: int, element: T): T
```

替换List指定位置的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-set(index: int, element: T): T--><!--Device-List-set(index: int, element: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 查找的下标值。取值范围[0, List.length-1]，需要小于等于int32_max即2147483647。 |
| element | T | Yes | 用来替换的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回替换后的元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The set method cannot be bound. |
| 10200001 | The value of index is out of range. |

## Examples

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

对List中的元素进行排序。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-sort(comparator: ListComparatorFn<T>): void--><!--Device-List-sort(comparator: ListComparatorFn<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| comparator | [ListComparatorFn](arkts-arkts-listcomparatorfn-t.md)&lt;T&gt; | Yes | 回调函数。&lt;br&gt; API version 23开始发生兼容性变更，在API version 22及之前的版本其类型为：`(firstValue: T, secondValue: T) => number`。<br>**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The sort method cannot be bound. |

## Examples

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

## [index: int]

```TypeScript
[index: int]: T
```

返回指定下标的元素。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-List-[index: int]: T--><!--Device-List-[index: int]: T-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

List的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-List-length: number--><!--Device-List-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

