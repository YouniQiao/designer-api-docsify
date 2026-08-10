# ChildrenMainSize

维护List组件或ListItemGroup组件的子组件在主轴方向的大小信息，仅支持一对一绑定到List组件或ListItemGroup组件。

> **说明：**
> 
> - 提供的主轴方向大小信息必须与子组件实际在主轴方向的大小一致，子组件在主轴方向大小变化或者增删子组件时都必须通过ChildrenMainSize对象方法通知List组件或ListItemGroup组件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class ChildrenMainSize--><!--Device-unnamed-declare class ChildrenMainSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(childDefaultSize: number)
```

ChildrenMainSize有参构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-constructor(childDefaultSize: number)--><!--Device-ChildrenMainSize-constructor(childDefaultSize: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| childDefaultSize | number | Yes | 子组件在主轴方向的默认大小。&lt;br/&gt;单位：vp&lt;br/&gt;**说明：** &lt;br/&gt;必须是有限的非负数值，否则抛出异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## splice

```TypeScript
splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void
```

批量增删改子组件在主轴方向的大小信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void--><!--Device-ChildrenMainSize-splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | 从0开始计算的索引值，表示要开始修改子组件在主轴方向大小信息的位置。&lt;br/&gt;**说明：** &lt;br/&gt;1. 必须是有限的非负数值，否则抛出异常。&lt;br/&gt;2. 非整数会被截断为 整数。&lt;br/&gt;3. 超过最大索引值不生效。&lt;br/&gt;取值范围：[0, +∞) |
| deleteCount | number | No | 从start开始删除的大小信息的数量。&lt;br/&gt;**说明：** &lt;br/&gt;1. 必须是有限的非负数值，否则处理为0。&lt;br/&gt;2. 非整数会被截断为整数。&lt;br /&gt;3. start + deleteCount - 1可以超过最大索引值，会删除索引值start开始之后的所有子组件的大小信息。&lt;br/&gt;默认值为+∞。 &lt;br/&gt;取值范围：[0, +∞) |
| childrenSize | Array&lt;number&gt; | No | 要在start位置插入的所有子组件的主轴方向的大小。&lt;br/&gt;Array中各个数值单位：vp &lt;br/&gt;**说明：** &lt;br/&gt;1.数组中数值如 果是有限的非负值，则认为是指定的大小，后续不随默认大小的变化而变化。&lt;br/&gt;2. 数组中数值如果不是有限的非负值，会被处理成默认大小，后续会随默认大小的变化而变化。&lt;br/&gt;默认值为空数组。 &lt;br/&gt;取值范围： [0, +∞) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## update

```TypeScript
update(index: number, childSize: number): void
```

修改指定索引值对应的子组件的主轴方向的大小信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-update(index: number, childSize: number): void--><!--Device-ChildrenMainSize-update(index: number, childSize: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 从0开始计算的索引值，表示要开始修改子组件在主轴方向大小信息的位置。&lt;br/&gt;**说明：** &lt;br/&gt;1. 必须是有限的非负数值，否则抛出异常。&lt;br/&gt;2. 非整数会被截断为 整数。&lt;br/&gt;3. 超过最大索引值不生效。 &lt;br/&gt;取值范围：[0, +∞) |
| childSize | number | Yes | 要更新成的大小。&lt;br/&gt;单位：vp &lt;br/&gt;**说明：** &lt;br/&gt;1.数值如果是有限的非负值，则认为是指定的大小，后续不随默认大小的变化而变化。&lt;br/&gt;2. 数 值如果不是有限的非负值，会被处理成默认大小，后续会随默认大小的变化而变化。 &lt;br/&gt;取值范围：[0, +∞) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## childDefaultSize

```TypeScript
get childDefaultSize(): number
```

Get default size

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-get childDefaultSize(): number--><!--Device-ChildrenMainSize-get childDefaultSize(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

