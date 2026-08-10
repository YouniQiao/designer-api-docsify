# HashSet

HashSet是一种非线性容器，用于存储不重复的元素集合，支持高效的元素增删和存在性判断。HashSet基于HashMap实现，仅操作元素的值对象，不涉及键的概念。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class HashSet<T>--><!--Device-unnamed-declare class HashSet<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { HashSet } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，迭代器的每一项为HashSet中的元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashSet-$_iterator(): IterableIterator<T>--><!--Device-HashSet-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回一个迭代器。 |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器的每一项为HashSet中的元素。  
> **说明：**
> 
> 不建议在Symbol.iterator中使用add、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-[Symbol.iterator](): IterableIterator<T>--><!--Device-HashSet-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回包含此HashSet中所有元素的迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");

// Method 1:
for (let item of hashSet) {
  console.info("value: " + item);
}
// value: squirrel
// value: sparrow

// Method 2:
let iter = hashSet[Symbol.iterator]();
let temp: IteratorResult<string> = iter.next();
while(!temp.done) {
  console.info("value: " + temp.value);
  temp = iter.next();
}
// value: squirrel
// value: sparrow
```

```TypeScript
// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashSet = new HashSet<string>();
for(let i = 0;i < 10;i++) {
  hashSet.add("sparrow" + i);
}
for(let i = 0;i < 10;i++) {
  hashSet.remove("sparrow" + i);
}
```

## add

```TypeScript
add(value: T): boolean
```

向HashSet添加元素。成功添加后HashSet的length增加1；若待添加元素已存在则不会重复添加，返回false且length不变。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-add(value: T): boolean--><!--Device-HashSet-add(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 要添加的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 成功添加元素返回true，若元素已存在则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The add method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
let result = hashSet.add("squirrel");
console.info("result:", result);  // result: true
```

## clear

```TypeScript
clear(): void
```

清除HashSet中的所有元素，并将length置为0。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-clear(): void--><!--Device-HashSet-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
hashSet.clear();
let result = hashSet.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

HashSet的构造函数，用于创建一个空的HashSet实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-constructor()--><!--Device-HashSet-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The HashSet's constructor cannot be directly invoked. |

## Examples

```TypeScript
let hashSet = new HashSet<number>();
```

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

返回包含此HashSet中所有元素的新迭代器对象，每个元素以[value, value]形式返回。  
> **说明：**
> 
> 不建议在entries迭代过程中使用add、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-entries(): IterableIterator<[T, T]>--><!--Device-HashSet-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[T, T]&gt; | 返回包含此HashSet中所有元素的迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
let iter = hashSet.entries();
let temp: IteratorResult<[string, string]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value[0]);
  console.info("value:" + temp.value[1]);
  temp = iter.next();
}
// key:squirrel
// value:squirrel
// key:sparrow
// value:sparrow
```

```TypeScript
// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashSet = new HashSet<string>();
for(let i = 0; i < 10; i++) {
  hashSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  hashSet.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void
```

在遍历过程中对每个元素调用一次回调函数。不建议在forEach回调中使用add、remove方法修改HashSet，因其可能导致迭代过程中的状态异常。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void--><!--Device-HashSet-forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value?: T, key?: T, set?: HashSet&lt;T&gt;) =&gt; void | Yes | 回调函数，在遍历过程中对每个元素调用一次。回调参数包括value、key和set，详见callbackFn的参数说明。 |
| thisArg | Object | No | callbackFn被调用时用作this值。当需要改变回调函数内this指向时传入此参数，不传入时默认值为当前实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("sparrow");
hashSet.add("squirrel");
hashSet.forEach((value: string, key: string): void => {
  console.info("value:" + value, "key:" + key);
});
// value:squirrel key:squirrel
// value:sparrow key:sparrow
```

```TypeScript
// You are not advised to use the add and remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashSet = new HashSet<string>();
for(let i = 0; i < 10; i++) {
  hashSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  hashSet.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: HashSetCbFn<T>): void
```

遍历HashSet中的所有元素，并对每个元素执行回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashSet-forEach(callbackFn: HashSetCbFn<T>): void--><!--Device-HashSet-forEach(callbackFn: HashSetCbFn<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [HashSetCbFn](arkts-arkts-hashsetcbfn-t.md)&lt;T&gt; | Yes | 对每个元素执行的回调函数。 |

## has

```TypeScript
has(value: T): boolean
```

判断HashSet是否包含指定元素，基于哈希值进行查找，具有O(1)的时间复杂度。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-has(value: T): boolean--><!--Device-HashSet-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 指定要查找的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定元素返回true，不包含指定元素返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The has method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
let result = hashSet.has("squirrel");
console.info("result:", result);  // result: true
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断HashSet是否为空。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-isEmpty(): boolean--><!--Device-HashSet-isEmpty(): boolean-End-->

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
const hashSet = new HashSet<number>();
let result = hashSet.isEmpty();
console.info("result:", result);  // result: true
```

## remove

```TypeScript
remove(value: T): boolean
```

从HashSet中删除指定的元素。成功删除后HashSet的length减少1；若指定元素不存在则集合不变，返回false。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-remove(value: T): boolean--><!--Device-HashSet-remove(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 指定要删除的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 成功删除指定元素返回true，若指定元素不存在则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
let result = hashSet.remove("sparrow");
console.info("result:", result);  // result: true
```

## values

```TypeScript
values(): IterableIterator<T>
```

返回包含此HashSet中所有值的新迭代器对象。  
> **说明：**
> 
> 不建议在values迭代过程中使用add、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-values(): IterableIterator<T>--><!--Device-HashSet-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回包含此HashSet中所有值的迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound. |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
let values = hashSet.values();
for (let value of values) {
  console.info("value:", value);
}
// value: squirrel
// value: sparrow
```

## length

```TypeScript
length: number
```

HashSet的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-length: number--><!--Device-HashSet-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

