# SegmentButtonItemOptionsArray

用于保存按钮信息的数组。

> **说明：**
> 
> SegmentButtonItemOptionsArray仅支持保存2到5个按钮信息元素。

**继承/实现关系：** SegmentButtonItemOptionsArray extends Array<SegmentButtonItemOptions>

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-declare class SegmentButtonItemOptionsArray--><!--Device-unnamed-declare class SegmentButtonItemOptionsArray-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(elements: SegmentButtonItemTuple)
```

构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-constructor(elements: SegmentButtonItemTuple)--><!--Device-SegmentButtonItemOptionsArray-constructor(elements: SegmentButtonItemTuple)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](../../apis-arkui/arkts-apis/arkts-arkui-segmentbuttonitemtuple-t.md) | 是 | 按钮信息。 |

## create

```TypeScript
static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray
```

创建一个SegmentButtonItemOptionsArray对象。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray--><!--Device-SegmentButtonItemOptionsArray-static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](../../apis-arkui/arkts-apis/arkts-arkui-segmentbuttonitemtuple-t.md) | 是 | 按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptionsArray](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonitemoptionsarray-c.md) | 返回创建的SegmentButtonItemOptionsArray对象。 |

## pop

```TypeScript
pop(): SegmentButtonItemOptions | undefined
```

移除数组末尾最后一个元素，返回被移除的元素。

> **说明：**
> 
> 分段按钮组件数组仅支持保存2到5个按钮信息，若移除后按钮组件数量不在个数限制范围内，移除按钮信息元素失败。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-pop(): SegmentButtonItemOptions | undefined--><!--Device-SegmentButtonItemOptionsArray-pop(): SegmentButtonItemOptions | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonitemoptions-c.md) \| undefined | Returns the removed element. |

## push

```TypeScript
push(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int
```

在数组末尾添加一个新的元素，返回添加元素后数组的长度。

> **说明：**
> 
> SegmentButton是仅支持显示2到5个按钮的分段按钮组件，同时SegmentButtonItemOptionsArray也只保存这2到5个按钮的具体信息，当超过按钮信息个数限制此方法无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-push(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int--><!--Device-SegmentButtonItemOptionsArray-push(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 被添加的按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 添加元素后数组的长度。 |

## push

```TypeScript
push(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
  ): int
```

在数组末尾添加两个新的元素，返回添加元素后数组的长度。

> **说明：**
> 
> SegmentButton是仅支持显示2到5个按钮的分段按钮组件，同时SegmentButtonItemOptionsArray也只保存这2到5个按钮的具体信息，当超过按钮信息个数限制此方法无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 被添加的第二个按钮信息。 |
| item2 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 被添加的第二个按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 添加元素后数组的长度。 |

## push

```TypeScript
push(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
  ): int
```

在数组末尾添加三个新的元素，返回添加元素后数组的长度。

> **说明：**
> 
> SegmentButton是仅支持显示2到5个按钮的分段按钮组件，同时SegmentButtonItemOptionsArray也只保存这2到5个按钮的具体信息，当超过按钮信息个数限制此方法无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 被添加的第二个按钮信息。 |
| item2 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 被添加的第二个按钮信息。 |
| item3 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 被添加的第二个按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 添加元素后数组的长度。 |

## shift

```TypeScript
shift(): SegmentButtonItemOptions | undefined
```

移除数组开头第一个元素，返回被移除的元素。

> **说明：**
> 
> 分段按钮组件数组仅支持保存2到5个按钮信息，若移除后按钮组件数量不在个数限制范围内，移除按钮信息元素失败。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-shift(): SegmentButtonItemOptions | undefined--><!--Device-SegmentButtonItemOptionsArray-shift(): SegmentButtonItemOptions | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonitemoptions-c.md) \| undefined | Returns the removed element. |

## splice

```TypeScript
splice(start: int, deleteCount: int, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]
```

在数组中，删除从start位置开始的deleteCount数量的元素，并插入items中的元素，返回一个包含了被删除的元素的数组。

> **说明：**
> 
> SegmentButton是仅支持显示2到5个按钮的分段按钮组件，同时SegmentButtonItemOptionsArray也只保存这2到5个按钮的具体信息，当超过按钮信息个数限制此方法无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-splice(start: int, deleteCount: int, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]--><!--Device-SegmentButtonItemOptionsArray-splice(start: int, deleteCount: int, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | 删除元素的起始位置。 |
| deleteCount | int | 是 | 删除元素的数量。 |
| items | [SegmentButtonItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonitemoptions-c.md)[] | 是 | 从start开始要加入到数组中的元素。<br>默认值：不指定任何元素，将从数组中删除元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonitemoptions-c.md)[] | Returns a SegmentButtonItemOptions array containing the deleted elements. |

## unshift

```TypeScript
unshift(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int
```

在数组开头添加一个新的元素，返回添加元素后数组的长度。

> **说明：**
> 
> SegmentButton是仅支持显示2到5个按钮的分段按钮组件，同时SegmentButtonItemOptionsArray也只保存这2到5个按钮的具体信息，当超过按钮信息个数限制此方法无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-unshift(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int--><!--Device-SegmentButtonItemOptionsArray-unshift(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 添加的按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 添加元素后数组的长度。 |

## unshift

```TypeScript
unshift(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,

  ): int
```

在数组开头添加两个新的元素，返回添加元素后数组的长度。

> **说明：**
> 
> 分段按钮组件数组仅支持保存2到5个按钮信息，若超过分段按钮组件数量个数的限制，添加按钮信息元素失败。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 添加的第二个按钮信息。 |
| item2 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 添加的第二个按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 添加元素后数组的长度。 |

## unshift

```TypeScript
unshift(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
  ): int
```

在数组开头添加三个新的元素，返回添加元素后数组的长度。

> **说明：**
> 
> SegmentButton是仅支持显示2到5个按钮的分段按钮组件，同时SegmentButtonItemOptionsArray也只保存这2到5个按钮的具体信息，当超过按钮信息个数限制此方法无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 添加的第二个按钮信息。 |
| item2 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 添加的第二个按钮信息。 |
| item3 | [SegmentButtonTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonicontextitem-i.md) | 是 | 添加的第二个按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 添加元素后数组的长度。 |

