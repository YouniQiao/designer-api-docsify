# @ohos.util.Queue

Queue遵循先进先出原则：在尾部增加元素，在头部删除元素。Queue基于循环队列的数据结构实现。
 Queue和[Deque](arkts-util-deque.md)相比，Queue在尾部增加元素，在头部删除元素；而Deque支持在两端进行增删操作。
 **推荐使用场景：** 一般符合先进先出的场景可以使用Queue。
 文档中使用了泛型，涉及以下泛型标记符：
 - T：Type，类型
 > **说明**
 >
 > - 容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。


## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [Queue](arkts-arkts-util-queue-queue-c.md) | Queue遵循先进先出原则：在尾部增加元素，在头部删除元素。Queue基于循环队列的数据结构实现。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [QueueForEachCb](arkts-arkts-queueforeachcb-t.md) | Queue的回调函数类型。 |

