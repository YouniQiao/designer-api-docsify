# ArrayList

ArrayList是一种线性数据结构，底层基于数组实现，解决了固定大小数组无法动态扩容的限制。ArrayList会根据实际需要动态调整容量，每次扩容增加50%。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { ArrayList } from '@kit.ArkTS';
import { ArrayListComparatorFn } from '@kit.ArkTS';
import { ArrayListForEachCb } from '@kit.ArkTS';
import { ArrayListReplaceCb } from '@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，迭代器按照ArrayList中元素的顺序依次返回类型为T的元素。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |

**示例**

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);

// 使用方法一：
for (let item of arrayList) {
  console.info(`value : ${item}`);
}

// 使用方法二：
let iter = arrayList.$_iterator();
let temp: IteratorResult<int> = iter.next();
while(!temp.done) {
    console.info(`value:${temp.value}`);
    temp = iter.next();
}
/**
 * value:2
 * value:4
 * value:5
 * value:4
 * */
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器按照ArrayList中元素的顺序依次返回类型为T的元素。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);

// 使用方法一：
for (let value of arrayList) {
  console.info('value:', value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
let iterator = arrayList[Symbol.iterator]();
let iteratorResult: IteratorResult<number> = iterator.next();
while (!iteratorResult.done) {
  console.info('value:', iteratorResult.value);
  iteratorResult = iterator.next();
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

在ArrayList尾部插入元素。批量添加元素时，建议先调用increaseCapacityTo方法扩充容量，避免多次自动扩容带来的性能开销。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
class Person {
  name: string = '';
  age: string = '';
}
let arrayList = new ArrayList<string | number | boolean | Array<number> | Person>();
// 添加字符串类型元素
arrayList.add('a');
// 添加数字类型元素
arrayList.add(1);
let numberArray = [1, 2, 3];
// 添加数组类型元素
arrayList.add(numberArray);
let person: Person = {name: 'Dylan', age: '13'};
// 添加自定义对象类型元素
let addPersonResult = arrayList.add(person);
// 添加布尔类型元素
let addBooleanResult = arrayList.add(false);
console.info('addPersonResult:', addPersonResult);  // addPersonResult: true
console.info('addBooleanResult:', addBooleanResult);  // addBooleanResult: true
console.info('length:', arrayList.length);  // length: 5
```

ArkTS-Sta示例：

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}
let arrayList: ArrayList<string | int | boolean | Array<int> | C1> =
  new ArrayList<string | int | boolean | Array<int> | C1>();
let result1 = arrayList.add("a");
let result2 = arrayList.add(1);
let b: Array<int> = [1, 2, 3];
let result3 = arrayList.add(b);
let c : C1 = {name: "Dylan", age: "13"}
let result4 = arrayList.add(c);
let result5 = arrayList.add(false);
```

## clear

```TypeScript
clear(): void
```

清除ArrayList中的所有元素，并把length置为0。此方法不会释放预留的容量空间，如需释放容量请调用trimToCurrentLength方法。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.clear();
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.clear();
```

## clone

```TypeScript
clone(): ArrayList<T>
```

克隆一个与ArrayList相同的实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: ArrayList<number> = arrayList.clone();
console.info('result = ', result.length); // result = 4
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result:  ArrayList<int> = arrayList.clone();
console.info("result = ", result.length); // result = 4
```

## constructor

```TypeScript
constructor()
```

ArrayList的构造函数，用于创建一个空的ArrayList实例。该构造函数需通过new关键字调用，不可作为普通函数直接调用，否则将抛出异常。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<string | number>();
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<string | int> = new ArrayList<string | int>();
```

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

把当前ArrayList实例转换成数组，并返回转换后的数组。此操作不会修改原ArrayList实例，对返回数组的修改也不会影响原实例。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: Array<number> = arrayList.convertToArray();
console.info('result = ', result); // result =  2,4,5,4
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: Array<int> = arrayList.convertToArray();
console.info("result = ", result); // result =  2,4,5,4
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => void, thisArg?: Object): void
```

在遍历ArrayList实例对象的过程中，对每个元素执行回调函数。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, arrlist?: ArrayList & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
// 遍历ArrayList中的每个元素，打印元素值和下标
arrayList.forEach((value: number, index?: number) => {
  console.info('value:' + value, 'index:' + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

```TypeScript
import { ArrayListForEachCb } from '@ohos.util.ArrayList';

let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let arrayListCb: ArrayListForEachCb<int> = (value: int, index: int, arrlist: ArrayList<int>) => {
  console.info("value: " + value, " index: " + index);
};
arrayList.forEach(arrayListCb);
```

## forEach

```TypeScript
forEach(callbackFn: ArrayListForEachCb<T>): void
```

在遍历ArrayList实例对象的过程中，对每个元素执行回调函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [ArrayListForEachCb](arkts-arkts-arraylistforeachcb-t.md)&lt;T&gt; | 是 |

**示例**

参见 [forEach](#foreach)

## getCapacity

ArkTS-Dyn:
```TypeScript
getCapacity(): number
```

ArkTS-Sta:
```TypeScript
getCapacity(): int
```

返回当前实例的容量大小。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: number = arrayList.getCapacity();
console.info('result = ', result); // result = 10
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: int = arrayList.getCapacity();
console.info("result = ", result); // result = 10
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

返回指定元素第一次出现的下标，查找失败返回-1。与getLastIndexOf的区别在于，该方法返回元素首次出现的位置，getLastIndexOf返回元素最后一次出现的位置。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.getIndexOf(2);
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: int = arrayList.getIndexOf(2);
console.info("result = ", result); // result = 0
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

返回指定元素最后一次出现的下标，查找失败返回-1。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.getLastIndexOf(2);
console.info('result = ', result); // result = 5
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: int = arrayList.getLastIndexOf(2);
console.info("result = ", result); // result = 5
```

## has

```TypeScript
has(element: T): boolean
```

判断此ArrayList中是否包含指定元素。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let arrayList = new ArrayList<string>();
arrayList.add('squirrel');
let result: boolean = arrayList.has('squirrel');
console.info('result:', result);  // result: true
```

## increaseCapacityTo

ArkTS-Dyn:
```TypeScript
increaseCapacityTo(newCapacity: number): void
```

ArkTS-Sta:
```TypeScript
increaseCapacityTo(newCapacity: int): void
```

如果传入的新容量大于或等于ArrayList中的元素个数，将容量变更为新容量；如果传入的新容量小于ArrayList中的元素个数，则容量保持不变。当需要批量添加元素时，可预先调用此方法扩充容量，避免多次自动扩容带来的性能开销。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newCapacity | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.increaseCapacityTo(2);
arrayList.increaseCapacityTo(8);
console.info('result = ', arrayList.length); // result = 4
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.increaseCapacityTo(2);
arrayList.increaseCapacityTo(8);
console.info("result = ", arrayList.length); // result = 4
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

在长度范围内指定位置index插入元素element。调用成功后，ArrayList的length增加1，index位置及之后的元素依次向后移动一位。如果index超出范围，则抛出异常。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number | string | boolean>();
// 在位置0插入字符串'A'
arrayList.insert('A', 0);
// 在位置1插入数字0
arrayList.insert(0, 1);
// 在位置2插入布尔值true
arrayList.insert(true, 2);
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int | string | boolean> = new ArrayList<int | string | boolean>();
arrayList.insert("A", 0);
arrayList.insert(0, 1);
arrayList.insert(true, 2);
console.info("length:", arrayList.length);  // length: 3
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断该ArrayList是否为空。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.isEmpty();
console.info('result = ', result); // result =  false
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.isEmpty();
console.info("result = ", result); // result =  false
```

## remove

```TypeScript
remove(element: T): boolean
```

删除查找到的第一个指定元素。删除成功后，ArrayList的length减少1，被删除元素之后的元素依次向前移动一位。如果未找到指定元素，则不执行删除操作。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.remove(2);
console.info('result = ', result); // result =  true
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.remove(2);
console.info("result = ", result); // result =  true
```

## removeByIndex

ArkTS-Dyn:
```TypeScript
removeByIndex(index: number): T
```

ArkTS-Sta:
```TypeScript
removeByIndex(index: int): T
```

根据指定下标删除元素，并返回被删除的元素。删除后，ArrayList的length减少1，被删除元素之后的元素依次向前移动一位。如果index超出范围，则抛出异常。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.removeByIndex(2);
console.info('result = ', result); // result = 5
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(4);
let result: int = arrayList.removeByIndex(2);
console.info("result = ", result); // result = 5
```

## removeByRange

ArkTS-Dyn:
```TypeScript
removeByRange(fromIndex: number, toIndex: number): void
```

ArkTS-Sta:
```TypeScript
removeByRange(fromIndex: int, toIndex: int): void
```

删除指定范围内的元素，即左闭右开区间[fromIndex, toIndex)。删除后，ArrayList的length减少对应的元素个数，toIndex之后的元素依次向前移动。如果fromIndex或toIndex超出范围， 则抛出异常。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| toIndex | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
// 删除下标2到4之间的元素（左闭右开区间，即删除下标为2和3的元素）
arrayList.removeByRange(2, 4);
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.removeByRange(2, 4);
```

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => T, thisArg?: Object): void
```

遍历ArrayList中的每个元素，对每个元素执行回调函数，用回调函数返回的值替换原元素。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, arrlist?: ArrayList & lt;T & gt;) = & gt; T | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.replaceAllElements((value: number): number => {
  // 用户操作逻辑根据实际场景进行添加。
  return value;
});
```

```TypeScript
import { ArrayListReplaceCb } from '@ohos.util.ArrayList';

let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let arrayListCb: ArrayListReplaceCb<int> = (value: int, index: int, arrlist: ArrayList<int>): int => {
  // 用户操作逻辑根据实际场景进行添加。
  return value;
};
arrayList.replaceAllElements(arrayListCb);
```

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: ArrayListReplaceCb<T>): void
```

遍历ArrayList中的每个元素，对每个元素执行回调函数，用回调函数返回的值替换原元素。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [ArrayListReplaceCb](arkts-arkts-arraylistreplacecb-t.md)&lt;T&gt; | 是 |

**示例**

参见 [replaceAllElements](#replaceallelements)

## sort

```TypeScript
sort(comparator?: ArrayListComparatorFn<T>): void
```

根据指定比较器所定义的顺序，对ArrayList中的元素进行排序。排序后，ArrayList的元素个数不变，元素位置按比较器定义的顺序重新排列。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | [ArrayListComparatorFn](arkts-arkts-arraylistcomparatorfn-t.md)&lt;T&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
// 升序排序
arrayList.sort((firstValue: number, secondValue: number) => firstValue - secondValue);
// 降序排序
arrayList.sort((firstValue: number, secondValue: number) => secondValue - firstValue);
// 默认排序（升序）
arrayList.sort();
```

ArkTS-Sta示例：

```TypeScript
import { ArrayListComparatorFn } from '@kit.ArkTS'; 

let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let arrayListCb1: ArrayListComparatorFn<int> = (a: int, b: int): double => {
  return a - b;
}
let arrayListCb2: ArrayListComparatorFn<int> = (a: int, b: int): double => {
  return b - a;
}
arrayList.sort(arrayListCb1);
arrayList.sort(arrayListCb2);
arrayList.sort();
```

## subArrayList

ArkTS-Dyn:
```TypeScript
subArrayList(fromIndex: number, toIndex: number): ArrayList<T>
```

ArkTS-Sta:
```TypeScript
subArrayList(fromIndex: int, toIndex: int): ArrayList<T>
```

根据下标截取ArrayList中的一段元素，并返回这一段ArrayList实例，即左闭右开区间[fromIndex, toIndex)。如果fromIndex或toIndex超出范围，则抛出异常。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| toIndex | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: ArrayList<number> = arrayList.subArrayList(2, 4);
console.info('result = ', result.length); // result = 2
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: ArrayList<int> = arrayList.subArrayList(2, 4);
console.info("result = ", result.length); // result = 2
```

## trimToCurrentLength

```TypeScript
trimToCurrentLength(): void
```

释放ArrayList中预留的空间，把容量调整为当前的元素个数。当ArrayList的容量远大于当前元素个数时（如经过多次删除操作后），可调用此方法释放多余空间以优化内存占用。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.trimToCurrentLength();
console.info('result = ', arrayList.length); // result = 4
```

ArkTS-Sta示例：

```TypeScript
let arrayList: ArrayList<int> = new ArrayList<int>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.trimToCurrentLength();
console.info("result = ", arrayList.length); // result = 4
```

## [index: int]

```TypeScript
[index: int]: T
```

获取指定下标对应位置的元素。如果index超出范围，则抛出异常。

**类型：** T

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

ArrayList的元素个数。

**类型：** number

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
