# Container

定义场景对象的容器。容器提供了一种将场景对象分组到层次结构中的方法。

**起始版本：** 23

<!--Device-unnamed-export interface Container--><!--Device-unnamed-export interface Container-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## append

```TypeScript
append(item: T): void
```

追加一个对象到容器。如果追加的对象已存在于容器中，容器会先移除该对象再插入，因此数量不会增加。

**起始版本：** 23

<!--Device-Container-append(item: T): void--><!--Device-Container-append(item: T): void-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | T | 是 |

## clear

```TypeScript
clear(): void
```

清空容器内的所有对象。

**起始版本：** 23

<!--Device-Container-clear(): void--><!--Device-Container-clear(): void-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## count

```TypeScript
count(): number
```

获取容器中对象的数量。

**起始版本：** 23

<!--Device-Container-count(): int--><!--Device-Container-count(): int-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| number |

## get

```TypeScript
get(index: number): T | null
```

获取特定下标对象，获取不到则返回空。

**起始版本：** 23

<!--Device-Container-get(index: int): T | null--><!--Device-Container-get(index: int): T | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## insertAfter

```TypeScript
insertAfter(item: T, sibling: T | null): void
```

在兄弟节点后面插入对象。如果插入的对象已存在于容器中，容器会先移除该对象再插入，因此数量不会增加。

**起始版本：** 23

<!--Device-Container-insertAfter(item: T, sibling: T | null): void--><!--Device-Container-insertAfter(item: T, sibling: T | null): void-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | T | 是 |
| sibling | T \| null | 是 |

## remove

```TypeScript
remove(item: T): void
```

移除指定对象。

**起始版本：** 23

<!--Device-Container-remove(item: T): void--><!--Device-Container-remove(item: T): void-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | T | 是 |
