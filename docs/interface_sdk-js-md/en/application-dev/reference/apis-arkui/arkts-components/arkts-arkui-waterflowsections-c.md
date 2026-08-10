# WaterFlowSections

瀑布流分组信息。

> **说明：**
> 
> 使用splice、push、update修改分组信息后需要保证所有分组子组件总数与瀑布流实际子组件总数一致，否则会出现瀑布流因为不能正常布局而无法滑动的问题。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class WaterFlowSections--><!--Device-unnamed-declare class WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

创建一个瀑布流分组。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-constructor()--><!--Device-WaterFlowSections-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## length

```TypeScript
length(): number
```

获取瀑布流中分组数量。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-length(): number--><!--Device-WaterFlowSections-length(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 瀑布流中分组数量。 |

## push

```TypeScript
push(section: SectionOptions): boolean
```

将指定分组添加到瀑布流末尾。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-push(section: SectionOptions): boolean--><!--Device-WaterFlowSections-push(section: SectionOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| section | [SectionOptions](../arkts-apis/arkts-arkui-waterflow-sectionoptions-c.md) | Yes | 添加到瀑布流末尾的分组，包含该分组的FlowItem数量、列数/行数、间距、外边距和主轴大小回调等配置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 分组添加成功返回true，添加失败（新分组的itemsCount不是非负数）返回false。 |

## splice

```TypeScript
splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean
```

移除或者替换已存在的分组和/或添加新分组。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean--><!--Device-WaterFlowSections-splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | 从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。&lt;br/&gt;**说明：** &lt;br/&gt;1. 如果索引是负数，则从末尾开始计算，使用 `start + WaterFlowSections.length()`。&lt;br/&gt;2. 如果 `start &lt; -WaterFlowSections.length()`，则使用0。<br/>3. 如果 `start &gt;&lt;br/&gt;3. 如果 `start >= WaterFlowSections.length()`，则在最后添加新分组。 |
| deleteCount | number | No | 表示要从start开始删除的分组数量。&lt;br/&gt;**说明：** &lt;br/&gt;1. 如果省略了deleteCount，或者其值大于或等于由start指定的位置到 WaterFlowSections末尾的分组数量，那么从start到WaterFlowSections末尾的所有分组将被删除。&lt;br/&gt;2. 如果deleteCount是0或者负数，则不会删除任何分组。 |
| sections | Array&lt;SectionOptions&gt; | No | 表示要从start开始加入的分组。如果不指定，`splice()`将只从瀑布流中删除分组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 分组修改成功返回true；修改失败（要加入的分组中有任意分组的itemsCount不是非负数）返回false。 |

## update

```TypeScript
update(sectionIndex:number, section: SectionOptions): boolean
```

修改指定索引分组的配置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-update(sectionIndex:number, section: SectionOptions): boolean--><!--Device-WaterFlowSections-update(sectionIndex:number, section: SectionOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sectionIndex | number | Yes | 从0开始计算的索引，会转换为整数，表示要修改的分组的位置。&lt;br/&gt;**说明：** &lt;br/&gt;1. 如果索引是负数，则从末尾开始计算，使用 `sectionIndex + WaterFlowSections.length()`。&lt;br/&gt;2. 如果`sectionIndex &lt; -WaterFlowSections.length()`，则使用0。<br/>3. 如果`sectionIndex &gt;&lt;br/&gt;3. 如果`sectionIndex >= WaterFlowSections.length()`，则在最后添加新分组。 |
| section | [SectionOptions](../arkts-apis/arkts-arkui-waterflow-sectionoptions-c.md) | Yes | 新的分组信息，用于替换指定索引位置的FlowItem分组配置，包括FlowItem数量、列数/行数、间距、外边距和主轴大小回调等。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 分组是否更新成功。分组更新成功返回true，更新失败（新分组的itemsCount不是非负数）返回false。 |

## values

```TypeScript
values(): Array<SectionOptions>
```

获取瀑布流中所有分组配置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-values(): Array<SectionOptions>--><!--Device-WaterFlowSections-values(): Array<SectionOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;SectionOptions&gt; | 瀑布流中所有分组配置信息。 |

