# Stack

Stack is implemented based on the array data structure.It follows the principle Last In First Out (LIFO) and supports data insertion and removal at one end.

**Since:** 8

<!--Device-unnamed-declare class Stack<T>--><!--Device-unnamed-declare class Stack<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Stack } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

returns an ES6 iterator.Each item of the iterator is a Javascript Object

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-[Symbol.iterator](): IterableIterator<T>--><!--Device-Stack-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;T&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);

// Method 1:
for (let value of stack) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// Method 2:
let iter = stack[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next().value;
while(temp != undefined) {
  console.info("value: " + temp);
  temp = iter.next().value;
}
// value: 2
// value: 4
// value: 5
// value: 4
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Stack** instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-constructor()--><!--Device-Stack-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## Examples

```TypeScript
let stack = new Stack<number | string | Object>();
```

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse each element in the **Stack** instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void, thisArg?: Object): void--><!--Device-Stack-forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, stack?: Stack&lt;T&gt;) =&gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);
stack.forEach((value : number, index: number) :void => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this Stack is empty (contains no elements).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-isEmpty(): boolean--><!--Device-Stack-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);
let result = stack.isEmpty();
console.info("result:", result);  // result: false
```

## locate

```TypeScript
locate(element: T): number
```

Obtains the index of the first occurrence of the specified element in this Stack.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-locate(element: T): int--><!--Device-Stack-locate(element: T): int-End-->

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

## Examples

```TypeScript
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
let result = stack.locate(5);
console.info("result:", result);  // result: 2
```

## peek

```TypeScript
peek(): T
```

Obtains the top element of this Stack. If the Stack is empty, **undefined** is returned.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-peek(): T--><!--Device-Stack-peek(): T-End-->

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

## Examples

```TypeScript
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
let result = stack.peek();
console.info("result:", result);  // result: 2
```

## pop

```TypeScript
pop(): T
```

Removes the top element from this Stack.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-pop(): T--><!--Device-Stack-pop(): T-End-->

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

## Examples

```TypeScript
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
stack.push(4);
let result = stack.pop(); 
console.info("result = " + result); // result = 4
```

## push

```TypeScript
push(item: T): T
```

Adds an element at the top of this Stack.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-push(item: T): T--><!--Device-Stack-push(item: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
class C1 {
  name: string = ""
  age: string = ""
}
let stack = new Stack<number | string | C1>();
let result = stack.push("a");
let result1 = stack.push(1);
let c : C1  = {name : "Dylan", age : "13"};
let result2 = stack.push(c);
console.info("length:", stack.length);  // length: 3
```

## length

```TypeScript
length: number
```

Number of elements in a Stack.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Stack-length: number--><!--Device-Stack-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
