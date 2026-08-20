# WaterFlowSections

Describes the water flow item sections.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class WaterFlowSections--><!--Device-unnamed-export declare class WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a &lt;em&gt;WaterFlowSections&lt;/em&gt; object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowSections-constructor()--><!--Device-WaterFlowSections-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## length

```TypeScript
length(): int
```

Obtains the number of sections in the &lt;em&gt;WaterFlow&lt;/em&gt; component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowSections-length(): int--><!--Device-WaterFlowSections-length(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns section counts in the WaterFlow. |

## push

```TypeScript
push(section: SectionOptions): boolean
```

Adds the specified sections to the end of the &lt;em&gt;WaterFlow&lt;/em&gt; component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowSections-push(section: SectionOptions): boolean--><!--Device-WaterFlowSections-push(section: SectionOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| section | [SectionOptions](arkts-waterflow-sectionoptions-c.md) | Yes | Sections to add to the end of the &lt;em&gt;WaterFlow&lt;/em&gt; component. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the push was successful. |

## splice

```TypeScript
splice(start: int, deleteCount?: int, sections?: Array<SectionOptions>): boolean
```

Changes sections by removing or replacing an existing section and/or adding a section.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowSections-splice(start: int, deleteCount?: int, sections?: Array<SectionOptions>): boolean--><!--Device-WaterFlowSections-splice(start: int, deleteCount?: int, sections?: Array<SectionOptions>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | Zero-based index at which the changing starts. The value is converted to an integer. <br>The value should be an integer. <br>&lt;em&gt;NOTE&lt;/em&gt; <br>1. A negative index counts back from the end of the section list. If -&lt;em&gt;WaterFlowSections.length()&lt;/em&gt; &lt;= &lt;em&gt;start&lt;/em&gt; &lt; &lt;em&gt;0&lt;/em&gt;, &lt;em&gt;start&lt;/em&gt; + &lt;em&gt;array.length&lt;/em&gt; is used. <br>2. If &lt;em&gt;start&lt;/em&gt; &lt; -<em>WaterFlowSections.length()</em>, <em>0</em> is used. <br>3. If <em>start</em> &gt;= &lt;em&gt;WaterFlowSections.length()&lt;/em&gt;, a new section is added at the end. |
| deleteCount | int | No | Number of sections to be deleted from the position specified by &lt;em&gt;start&lt;/em&gt;. <br>The value should be an integer. <br>&lt;em&gt;NOTE&lt;/em&gt; <br>1. If &lt;em&gt;deleteCount&lt;/em&gt; is omitted, or if its value is greater than or equal to the number of sections from the position specified by &lt;em&gt;start&lt;/em&gt; to the end of the &lt;em&gt;WaterFlowSections&lt;/em&gt;, then all sections from the position specified by &lt;em&gt;start&lt;/em&gt; to the end of the &lt;em&gt;WaterFlowSections&lt;/em&gt; will be deleted. <br>2. If &lt;em&gt;deleteCount&lt;/em&gt; is &lt;em&gt;0&lt;/em&gt; or a negative number, no sections are deleted. |
| sections | Array&lt;[SectionOptions](arkts-waterflow-sectionoptions-c.md)&gt; | No | Sections to add to the section list, beginning from the position specified by &lt;em&gt;start&lt;/em&gt;. If no section is specified, &lt;em&gt;splice()&lt;/em&gt; will only delete sections from the &lt;em&gt;WaterFlow&lt;/em&gt; component. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the splice was successful. |

## update

```TypeScript
update(sectionIndex: int, section: SectionOptions): boolean
```

Updates the configuration of a specified water flow item section.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowSections-update(sectionIndex: int, section: SectionOptions): boolean--><!--Device-WaterFlowSections-update(sectionIndex: int, section: SectionOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sectionIndex | int | Yes | Zero-based index of the water flow item section to update. The value is converted to an integer. <br>The value should be an integer. <br>&lt;em&gt;NOTE&lt;/em&gt; <br>1. A negative index counts back from the end of the section list. If -&lt;em&gt;WaterFlowSections.length()&lt;/em&gt; &lt;= &lt;em&gt;sectionIndex&lt;/em&gt; &lt; &lt;em&gt;0&lt;/em&gt;, &lt;em&gt;sectionIndex&lt;/em&gt; + &lt;em&gt;array.length&lt;/em&gt; is used. <br>2. If &lt;em&gt;sectionIndex&lt;/em&gt; &lt; -<em>WaterFlowSections.length()</em>, <em>0</em> is used.<br>3. If <em> sectionIndex</em> &gt;= &lt;em&gt;WaterFlowSections.length()&lt;/em&gt;, a new section is added at the end. |
| section | [SectionOptions](arkts-waterflow-sectionoptions-c.md) | Yes | New section configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the update was successful. |

## values

```TypeScript
values(): Array<SectionOptions>
```

Obtains the configuration of all sections in the &lt;em&gt;WaterFlow&lt;/em&gt; component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowSections-values(): Array<SectionOptions>--><!--Device-WaterFlowSections-values(): Array<SectionOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[SectionOptions](arkts-waterflow-sectionoptions-c.md)&gt; | Returns all the section options in the WaterFlow. |

