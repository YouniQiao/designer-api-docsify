# WaterFlowSections

瀑布流分组信息。

> **说明：**
> 
> 使用splice、push、update修改分组信息后需要保证所有分组子组件总数与瀑布流实际子组件总数一致，否则会出现瀑布流因为不能正常布局而无法滑动的问题。

**起始版本：** 12

<!--Device-unnamed-declare class WaterFlowSections--><!--Device-unnamed-declare class WaterFlowSections-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

创建一个瀑布流分组。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WaterFlowSections-constructor()--><!--Device-WaterFlowSections-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## length

```TypeScript
length(): number
```

获取瀑布流中分组数量。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WaterFlowSections-length(): number--><!--Device-WaterFlowSections-length(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## push

```TypeScript
push(section: SectionOptions): boolean
```

将指定分组添加到瀑布流末尾。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WaterFlowSections-push(section: SectionOptions): boolean--><!--Device-WaterFlowSections-push(section: SectionOptions): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| section | [SectionOptions](arkts-arkui-sectionoptions-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## splice

```TypeScript
splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean
```

移除或者替换已存在的分组和/或添加新分组。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WaterFlowSections-splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean--><!--Device-WaterFlowSections-splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| deleteCount | number | 否 |
| sections | Array&lt;SectionOptions&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## update

```TypeScript
update(sectionIndex:number, section: SectionOptions): boolean
```

修改指定索引分组的配置信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WaterFlowSections-update(sectionIndex:number, section: SectionOptions): boolean--><!--Device-WaterFlowSections-update(sectionIndex:number, section: SectionOptions): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sectionIndex | number | 是 |
| section | [SectionOptions](arkts-arkui-sectionoptions-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## values

```TypeScript
values(): Array<SectionOptions>
```

获取瀑布流中所有分组配置信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WaterFlowSections-values(): Array<SectionOptions>--><!--Device-WaterFlowSections-values(): Array<SectionOptions>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Array&lt;SectionOptions&gt; |
