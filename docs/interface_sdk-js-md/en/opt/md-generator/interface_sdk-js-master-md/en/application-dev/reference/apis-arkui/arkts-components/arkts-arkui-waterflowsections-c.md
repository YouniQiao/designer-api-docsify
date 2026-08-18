# WaterFlowSections

Describes the water flow item sections. > **NOTE：**> > After the section information is modified using **splice**, **push**, and **update**, ensure that the total number > of child nodes in all sections matches the actual total number of child nodes in the **WaterFlow** component. Any > failure to do so may result in layout issues that prevent the **WaterFlow** component from scrolling properly.

**Since:** 12

<!--Device-unnamed-declare class WaterFlowSections--><!--Device-unnamed-declare class WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **WaterFlowSections** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-constructor()--><!--Device-WaterFlowSections-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## length

```TypeScript
length(): number
```

Obtains the number of sections in the **WaterFlow** component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-length(): number--><!--Device-WaterFlowSections-length(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## push

```TypeScript
push(section: SectionOptions): boolean
```

Adds the specified sections to the end of the **WaterFlow** component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-push(section: SectionOptions): boolean--><!--Device-WaterFlowSections-push(section: SectionOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| section | [SectionOptions](arkts-arkui-sectionoptions-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## splice

```TypeScript
splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean
```

Changes sections by removing or replacing an existing section and/or adding a section.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean--><!--Device-WaterFlowSections-splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| deleteCount | number | No |
| sections | Array&lt;[SectionOptions](arkts-arkui-sectionoptions-c.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## update

```TypeScript
update(sectionIndex:number, section: SectionOptions): boolean
```

Updates the configuration of a specified water flow item section.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-update(sectionIndex:number, section: SectionOptions): boolean--><!--Device-WaterFlowSections-update(sectionIndex:number, section: SectionOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sectionIndex | number | Yes |
| section | [SectionOptions](arkts-arkui-sectionoptions-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## values

```TypeScript
values(): Array<SectionOptions>
```

Obtains the configuration of all sections in the **WaterFlow** component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowSections-values(): Array<SectionOptions>--><!--Device-WaterFlowSections-values(): Array<SectionOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[SectionOptions](arkts-arkui-sectionoptions-c.md)&gt; |
