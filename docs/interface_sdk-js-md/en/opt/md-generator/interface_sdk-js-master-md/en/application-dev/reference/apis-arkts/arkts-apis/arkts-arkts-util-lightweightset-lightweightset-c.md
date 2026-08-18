# LightWeightSet

LightWeightSet stores a set of values, each of which must be unique.

**Since:** 23

<!--Device-unnamed-declare class LightWeightSet--><!--Device-unnamed-declare class LightWeightSet-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

returns an ES6 iterator.Each item of the iterator is a Javascript Object

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightSet-$_iterator(): IterableIterator<T>--><!--Device-LightWeightSet-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

returns an ES6 iterator.Each item of the iterator is a Javascript Object

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-[Symbol.iterator](): IterableIterator<T>--><!--Device-LightWeightSet-[Symbol.iterator](): IterableIterator<T>-End-->

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");

// Method 1:
for (let value of lightWeightSet) {
  console.info("value:", value);
}
// value: sparrow
// value: squirrel

// Method 2:
let iter = lightWeightSet[Symbol.iterator]();
let temp: IteratorResult<string> = iter.next();
while(!temp.done) {
  console.info("value:", temp.value);
  temp = iter.next();
}
// value: sparrow
// value: squirrel
```

```TypeScript
// You are not advised to use the add, remove, or removeAt APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}
```

## add

```TypeScript
add(obj: T): boolean
```

Adds an element to this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-add(obj: T): boolean--><!--Device-LightWeightSet-add(obj: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | T | Yes |

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
let lightWeightSet = new LightWeightSet<string>();
let result = lightWeightSet.add("squirrel");
console.info("result:", result);  // result: true
```

## addAll

```TypeScript
addAll(set: LightWeightSet<T>): boolean
```

Adds all elements in a LightWeightSet to this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-addAll(set: LightWeightSet<T>): boolean--><!--Device-LightWeightSet-addAll(set: LightWeightSet<T>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | Yes |

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let set = new LightWeightSet<string>();
set.add("gull");
lightWeightSet.addAll(set);
let result = lightWeightSet.has("gull");
console.info("result:", result);  // result: true
```

## clear

```TypeScript
clear(): void
```

Clears this LightWeightSet and sets its length to **0**.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-clear(): void--><!--Device-LightWeightSet-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
lightWeightSet.clear();
let result = lightWeightSet.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **LightWeightSet** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-constructor()--><!--Device-LightWeightSet-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<number | string>();
```

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

Returns an iterator that contains all the elements in this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-entries(): IterableIterator<[T, T]>--><!--Device-LightWeightSet-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;[T, T]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let iter = lightWeightSet.entries();
for (let item of iter) {
  console.info("value:", item[1])
}
// value: sparrow
// value: squirrel
```

```TypeScript
// You are not advised to use the add, remove, or removeAt APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}
```

## equal

```TypeScript
equal(obj: Object): boolean
```

Checks whether the elements of this LightWeightSet are the same as those of **obj**. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 12. There is no substitute API.

**Since:** 8

**Deprecated since:** 12

<!--Device-LightWeightSet-equal(obj: Object): boolean--><!--Device-LightWeightSet-equal(obj: Object): boolean-End-->

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let obj = ["sparrow", "squirrel"];
let result = lightWeightSet.equal(obj);
console.info("result:", result);  // result: true
```

## forEach

```TypeScript
forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse the elements in this LightWeightSet and obtain their position indexes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void--><!--Device-LightWeightSet-forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value?: T, key?: T, set?: LightWeightSet & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("sparrow");
lightWeightSet.add("gull");
lightWeightSet.forEach((value: string, key: string) => {
  console.info("value:" + value, "key:" + key);
});
// value:gull key:gull
// value:sparrow key:sparrow
```

```TypeScript
// You are not advised to use the add, remove, or removeAt APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}
```

## forEach

```TypeScript
forEach(callbackFn: LightWeightSetForEachCb<T>): void
```

Executes the given callback function once for each real key in the map. It does not perform functions on deleted keys.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightSet-forEach(callbackFn: LightWeightSetForEachCb<T>): void--><!--Device-LightWeightSet-forEach(callbackFn: LightWeightSetForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [LightWeightSetForEachCb](arkts-arkts-lightweightsetforeachcb-t.md)&lt;T&gt; | Yes |

## getIndexOf

```TypeScript
getIndexOf(key: T): number
```

Obtains the position index of the element with the specified key in this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-getIndexOf(key: T): int--><!--Device-LightWeightSet-getIndexOf(key: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | T | Yes |

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.getIndexOf("sparrow");
console.info("result:", result);  // result: 0
```

## getValueAt

```TypeScript
getValueAt(index: number): T
```

Obtains the value of the element at the specified position in this LightWeightSet.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-getValueAt(index: number): T--><!--Device-LightWeightSet-getValueAt(index: number): T-End-->

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

## getValueAt

```TypeScript
getValueAt(index: number): T | undefined
```

Obtains the object at the location identified by index in an LightWeightSet container

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightSet-getValueAt(index: int): T | undefined--><!--Device-LightWeightSet-getValueAt(index: int): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## has

```TypeScript
has(key: T): boolean
```

Checks whether this LightWeightSet has the specified key.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-has(key: T): boolean--><!--Device-LightWeightSet-has(key: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | T | Yes |

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
let lightWeightSet = new LightWeightSet<number>();
lightWeightSet.add(123);
let result = lightWeightSet.has(123);
console.info("result:", result);  // result: true
```

## hasAll

```TypeScript
hasAll(set: LightWeightSet<T>): boolean
```

Checks whether this LightWeightSet contains all elements of the specified LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-hasAll(set: LightWeightSet<T>): boolean--><!--Device-LightWeightSet-hasAll(set: LightWeightSet<T>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | Yes |

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let set = new LightWeightSet<string>();
set.add("sparrow");
let result = lightWeightSet.hasAll(set);
console.info("result:", result);  // result: true
```

## increaseCapacityTo

```TypeScript
increaseCapacityTo(minimumCapacity: number): void
```

Increases the capacity of this LightWeightSet. If the passed-in capacity is greater than or equal to the number of elements in this LightWeightSet, the capacity is changed to the new capacity. If the passed-in capacity is less than the number of elements in this LightWeightSet, the capacity is not changed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-increaseCapacityTo(minimumCapacity: int): void--><!--Device-LightWeightSet-increaseCapacityTo(minimumCapacity: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| minimumCapacity | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.increaseCapacityTo(10);
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this LightWeightSet is empty (contains no element).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-isEmpty(): boolean--><!--Device-LightWeightSet-isEmpty(): boolean-End-->

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
const lightWeightSet = new LightWeightSet<number>();
let result = lightWeightSet.isEmpty();
console.info("result:", result);  // result: true
```

## remove

```TypeScript
remove(key: T): T
```

Removes an element of the specified key from this LightWeightSet.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-remove(key: T): T--><!--Device-LightWeightSet-remove(key: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.remove("sparrow");
console.info("result:", result);  // result: sparrow
```

## remove

```TypeScript
remove(key: T): T | undefined
```

Deletes an object of a specified Object type from an LightWeightSet container

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightSet-remove(key: T): T | undefined--><!--Device-LightWeightSet-remove(key: T): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## removeAt

```TypeScript
removeAt(index: number): boolean
```

Removes the element at the specified position from this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-removeAt(index: int): boolean--><!--Device-LightWeightSet-removeAt(index: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.removeAt(1);
console.info("result:", result);  // result: true
```

## toArray

```TypeScript
toArray(): Array<T>
```

Obtains an array that contains all objects in this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-toArray(): Array<T>--><!--Device-LightWeightSet-toArray(): Array<T>-End-->

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.toArray();
```

## toString

```TypeScript
toString(): String
```

Obtains a string that contains all elements in this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-toString(): String--><!--Device-LightWeightSet-toString(): String-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| String |

**Examples**

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.toString();
console.info("result:", result);  // result: sparrow,squirrel
```

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterator that contains all the values in this LightWeightSet.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-values(): IterableIterator<T>--><!--Device-LightWeightSet-values(): IterableIterator<T>-End-->

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
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let values = lightWeightSet.values();
for (let value of values) {
  console.info("value:", value);
}
// value: sparrow
// value: squirrel
```

## length

```TypeScript
length: number
```

Number of elements in a LightWeightSet.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightSet-length: number--><!--Device-LightWeightSet-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
