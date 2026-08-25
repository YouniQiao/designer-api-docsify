# Deque

Deque（double-ended queue）基于循环队列的数据结构实现，支持两端元素的插入和删除。Deque同时具备先进先出以及先进后出的特点，可根据操作端的不同同时作为队列和栈使用。当现有容量不足以容纳新插入的元素时，Deque会动态调整容量，每次扩容两倍，无需手动预设容量。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { Deque } from '@kit.ArkTS';
import { DequeForEachCb } from '@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，每一项都是一个ArkTS对象。

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
let deque: Deque<int> = new Deque<int>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);

// 使用方法一：
for (let item of deque) {
  console.info("value:" + item);
}
/*
输出结果：
value:4
value:5
value:4
value:2
 */

// 使用方法二：
let iter = deque.$_iterator();
let temp:IteratorResult<int> = iter.next();
while(!temp.done) {
  console.info("value:" + temp.value);
  temp = iter.next();
}
/*
输出结果：
value:4
value:5
value:4
value:2
 */
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，按插入顺序遍历Deque中的元素，迭代器每项为T类型的元素。

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
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);

// 使用方法一：
let nums: Array<number> = Array.from(deque);
for (let item of nums) {
  console.info("value:" + item);
}

// 使用方法二：
let iter = deque[Symbol.iterator]();
let temp:IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value:" + temp.value);
  temp = iter.next();
}
```

## constructor

```TypeScript
constructor()
```

Deque的构造函数，用于创建一个基于循环队列数据结构的空Deque实例。

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
// 创建Deque实例
let deque = new Deque<string | number | boolean | Object>();
```

ArkTS-Sta示例：

```TypeScript
let deque: Deque<string | int | boolean | Object> = new Deque<string | int | boolean | Object>();
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void
```

通过回调函数遍历Deque实例中的每个元素。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, deque?: Deque & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

```TypeScript
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(3);
deque.insertFront(1);
deque.insertEnd(4);
// 使用forEach遍历Deque中每个元素并执行回调函数
deque.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
/*
输出结果：value:1 index:0
         value:2 index:1
         value:3 index:2
         value:4 index:3
 */
```

```TypeScript
import { DequeForEachCb } from '@kit.ArkTS'

let deque: Deque<int> = new Deque<int>();
deque.insertFront(2);
deque.insertEnd(4);
deque.insertFront(5);
deque.insertEnd(4);
let dequeCb: DequeForEachCb<int> = (value: int, index: int, deque: Deque<int>):void => {
  console.info("value:" + value, "index:" + index);
};

deque.forEach(dequeCb);
```

## forEach

```TypeScript
forEach(callbackFn: DequeForEachCb<T>): void
```

通过回调函数遍历Deque实例中的每个元素。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [DequeForEachCb](arkts-arkts-dequeforeachcb-t.md)&lt;T&gt; | 是 |

**示例**

参见 [forEach](#foreach)

## getFirst

```TypeScript
getFirst(): T
```

获取Deque实例的头元素，不删除该元素。调用后，Deque的内容和长度不变。如需删除并返回首元素，请使用popFirst。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

ArkTS-Dyn示例：

```TypeScript
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertEnd(2);
deque.insertEnd(4);
deque.insertFront(5);
deque.insertFront(4);
// 获取Deque的头元素
let result = deque.getFirst();
console.info("result:", result);  // result: 4
```

ArkTS-Sta示例：

```TypeScript
let deque: Deque<int> = new Deque<int>();
deque.insertEnd(2);
deque.insertEnd(4);
deque.insertFront(5);
deque.insertFront(4);
let result = deque.getFirst();
```

## getLast

```TypeScript
getLast(): T
```

获取Deque实例的尾元素，不删除该元素。调用后，Deque的内容和长度不变。如需删除并返回尾元素，请使用popLast。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

ArkTS-Dyn示例：

```TypeScript
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);
// 获取Deque的尾元素
let result = deque.getLast();
console.info("result:", result);  // result: 2
```

ArkTS-Sta示例：

```TypeScript
let deque: Deque<int> = new Deque<int>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);
let result = deque.getLast();
```

## has

```TypeScript
has(element: T): boolean
```

判断此Deque中是否包含指定元素。

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
// 创建Deque实例
let deque = new Deque<string>();
// 在头部插入元素
deque.insertFront("squirrel");
// 判断Deque中是否包含指定元素
let result = deque.has("squirrel");
console.info("result:", result);  // result: true
```

## insertEnd

```TypeScript
insertEnd(element: T): void
```

在Deque尾部插入元素。插入成功后Deque的元素个数增加1。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
class PersonInfo {
  name: string = "";
  age: string = "";
}

// 创建支持多种类型的Deque实例
let deque = new Deque<string | number | boolean | Array<number> | PersonInfo>();
// 在尾部插入字符串元素
deque.insertEnd("a");
// 在尾部插入数字元素
deque.insertEnd(1);
let numArray = [1, 2, 3];
deque.insertEnd(numArray);
let person: PersonInfo = {name : "Dylan", age : "13"};
deque.insertEnd(person);
deque.insertEnd(false);
console.info("result:", deque[0]);  // result: a
```

ArkTS-Sta示例：

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}

let deque: Deque<string | int | boolean | Array<int> | C1> =
  new Deque<string | int | boolean | Array<int> | C1>();
deque.insertEnd("a");
deque.insertEnd(1);
let b: Array<int> = [1, 2, 3];
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

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
class PersonInfo {
  name: string = "";
  age: string = "";
}

// 创建支持多种类型的Deque实例
let deque = new Deque<string | number | boolean | Array<number> | PersonInfo>();
// 在头部插入字符串元素
deque.insertFront("a");
// 在头部插入数字元素
deque.insertFront(1);
let numArray = [1, 2, 3];
deque.insertFront(numArray);
let person: PersonInfo = {name : "Dylan", age : "13"};
deque.insertFront(person);
deque.insertFront(false);
console.info("result:", deque[0]);  // result: false
```

ArkTS-Sta示例：

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}
let deque: Deque<string | int | boolean | Array<int> | C1> =
  new Deque<string | int | boolean | Array<int> | C1>();
deque.insertFront("a");
deque.insertFront(1);
let b: Array<int> = [1, 2, 3];
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

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

ArkTS-Dyn示例：

```TypeScript
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertEnd(5);
deque.insertFront(2);
deque.insertFront(4);
// 删除并返回双端队列的首元素
let result = deque.popFirst();
console.info("result:", result);  // result: 4
```

ArkTS-Sta示例：

```TypeScript
let deque: Deque<int> = new Deque<int>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertEnd(5);
deque.insertFront(2);
deque.insertFront(4);
let result = deque.popFirst();
console.info("result = ", result) // result =  4
```

## popLast

```TypeScript
popLast(): T
```

删除并返回Deque的尾元素。删除成功后Deque的元素个数减少1。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

ArkTS-Dyn示例：

```TypeScript
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(6);
deque.insertFront(5);
deque.insertFront(2);
deque.insertFront(4);
// 删除并返回双端队列的尾元素
let result = deque.popLast();
console.info("result:", result);  // result: 6
```

ArkTS-Sta示例：

```TypeScript
let deque: Deque<int> = new Deque<int>();
deque.insertFront(2);
deque.insertEnd(6);
deque.insertFront(5);
deque.insertFront(2);
deque.insertFront(4);
let result = deque.popLast();
```

## [index: int]

```TypeScript
[index: int]: T
```

获取指定索引值对应位置的元素。

**类型：** T

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Deque的元素个数。

**类型：** number

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
