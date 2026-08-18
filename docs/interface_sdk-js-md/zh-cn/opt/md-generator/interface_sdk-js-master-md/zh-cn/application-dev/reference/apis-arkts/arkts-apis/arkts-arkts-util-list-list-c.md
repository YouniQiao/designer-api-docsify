# List

List底层通过单向链表实现，每个节点有一个指向后一个元素的引用。查询元素必须从头遍历，因此查询效率低，但插入和删除效率高。List允许元素为null。

**起始版本：** 23

<!--Device-unnamed-declare class List--><!--Device-unnamed-declare class List-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，每一项都是一个ArkTS对象。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-List-$_iterator(): IterableIterator<T>--><!--Device-List-$_iterator(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，用于遍历List中的元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-[Symbol.iterator](): IterableIterator<T>--><!--Device-List-[Symbol.iterator](): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
list.add(2);
list.add(4);
list.add(5);
list.add(4);

// 使用方法一：
for (let item of list) {
  console.info("value: " + item);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-add(element: T): boolean--><!--Device-List-add(element: T): boolean-End-->

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
// 创建支持多种类型元素的List实例
let list = new List<string | number | boolean | object>();
let result1 = list.add("a");
console.info("result = ", result1); // result =  true
let result2 = list.add(1);
console.info("result = ", result2); // result =  true
let numArray = [1, 2, 3];
let result3 = list.add(numArray);
console.info("result = ", result3); // result =  true
class PersonInfo {
  name: string = "";
  age: string = "";
}
let personInfo: PersonInfo = {name : "Dylan", age : "13"};
let result4 = list.add(personInfo);
console.info("result = ", result4); // result =  true
let result5 = list.add(false);
console.info("result = ", result5); // result =  true
```

## clear

```TypeScript
clear(): void
```

清除List中的所有元素，并将length置为0。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-clear(): void--><!--Device-List-clear(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-constructor()--><!--Device-List-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

**示例**

```TypeScript
let list = new List<string | number | boolean | object>();
```

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

把当前List实例转换成数组并返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-convertToArray(): Array<T>--><!--Device-List-convertToArray(): Array<T>-End-->

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

```TypeScript
let list = new List<number>();
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

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-equal(obj: Object): boolean--><!--Device-List-equal(obj: Object): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object | 是 |

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
let list = new List<number>();
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

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-List-equal(obj: RecordData): boolean--><!--Device-List-equal(obj: RecordData): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void
```

在遍历List实例对象中每一个元素的过程中，对每个元素执行回调函数。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void--><!--Device-List-forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, List?: List & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
list.add(2);
list.add(4);
list.add(5);
list.add(4);
// 遍历List中的每个元素并打印值和下标
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

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-List-forEach(callbackFn: ListForEachCb<T>): void--><!--Device-List-forEach(callbackFn: ListForEachCb<T>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [ListForEachCb](arkts-arkts-listforeachcb-t.md)&lt;T&gt; | 是 |

## get

```TypeScript
get(index: number): T
```

根据下标获取List中的元素。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-get(index: int): T--><!--Device-List-get(index: int): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
let list = new List<number>();
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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-getFirst(): T--><!--Device-List-getFirst(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200010](../errorcode-utils.md#10200010-容器为空) |

**示例**

```TypeScript
let list = new List<number>();
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

查找指定元素第一次出现的下标，查找失败返回-1。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-getIndexOf(element: T): int--><!--Device-List-getIndexOf(element: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-getLast(): T--><!--Device-List-getLast(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200010](../errorcode-utils.md#10200010-容器为空) |

**示例**

```TypeScript
let list = new List<number>();
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

查找指定元素最后一次出现的下标值，查找失败返回-1。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-getLastIndexOf(element: T): int--><!--Device-List-getLastIndexOf(element: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
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

根据下标截取List中的一段元素，并返回这一段List实例，包括起始值但不包括终止值。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-getSubList(fromIndex: int, toIndex: int): List<T>--><!--Device-List-getSubList(fromIndex: int, toIndex: int): List<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
let list = new List<number>();
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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-has(element: T): boolean--><!--Device-List-has(element: T): boolean-End-->

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
let list = new List<string>();
list.add("squirrel");
let result = list.has("squirrel");
console.info("result:", result);  // result: true
```

## insert

```TypeScript
insert(element: T, index: number): void
```

在长度范围内任意位置插入指定元素。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-insert(element: T, index: int): void--><!--Device-List-insert(element: T, index: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |
| index | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-isEmpty(): boolean--><!--Device-List-isEmpty(): boolean-End-->

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

```TypeScript
let list = new List<number>();
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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-remove(element: T): boolean--><!--Device-List-remove(element: T): boolean-End-->

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
let list = new List<number>();
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

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-removeByIndex(index: number): T--><!--Device-List-removeByIndex(index: number): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
let list = new List<number>();
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

根据索引查找对应元素。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-List-removeByIndex(index: int): T | undefined--><!--Device-List-removeByIndex(index: int): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void
```

遍历List中的元素，并用回调函数返回的新值替换原List中的元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void--><!--Device-List-replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, list?: List & lt;T & gt;) = & gt; T | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
list.add(2);
list.add(4);
list.add(5);
list.add(4);
list.replaceAllElements((value: number) => {
  // 用户操作逻辑根据实际场景进行添加
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

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-List-replaceAllElements(callbackFn: ListReplaceCb<T>): void--><!--Device-List-replaceAllElements(callbackFn: ListReplaceCb<T>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [ListReplaceCb](arkts-arkts-listreplacecb-t.md)&lt;T&gt; | 是 |

## set

```TypeScript
set(index: number, element: T): T
```

替换List指定位置的元素。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-set(index: int, element: T): T--><!--Device-List-set(index: int, element: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

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

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-sort(comparator: ListComparatorFn<T>): void--><!--Device-List-sort(comparator: ListComparatorFn<T>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | [ListComparatorFn](arkts-arkts-listcomparatorfn-t.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
let list = new List<number>();
list.add(2);
list.add(1);
list.add(3);
list.add(4);
list.sort((a: number, b: number) => a - b);  // 结果为升序排列
console.info("result:", list.convertToArray());  // result: 1,2,3,4

list.sort((a: number, b: number) => b - a);  // 结果为降序排列
console.info("result:", list.convertToArray());  // result: 4,3,2,1
```

## length

```TypeScript
length: number
```

List的元素个数。

**类型：** number

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-List-length: number--><!--Device-List-length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
