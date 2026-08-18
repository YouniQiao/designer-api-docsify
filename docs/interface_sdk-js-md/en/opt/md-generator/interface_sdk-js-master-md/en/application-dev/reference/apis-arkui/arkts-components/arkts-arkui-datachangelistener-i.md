# DataChangeListener

Listener for data changes. > **NOTE：**> > In APIs of **DataChangeListener** other than **onDatasetChange**, if the value of **index** is negative, the value > is treated as **0** by default. In **onDatasetChange**, if the specified index in a **DataOperation** is outside > the data source index range, the corresponding **DataOperation** does not take effect. (In **DataAddOperation**, > the value of **index** can equal the data source length.)

**Since:** 7

<!--Device-unnamed-declare interface DataChangeListener--><!--Device-unnamed-declare interface DataChangeListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## onDataAdd

```TypeScript
onDataAdd(index: number): void
```

Invoked when data is added to the position indicated by the specified index.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DataChangeListener-onDataAdd(index: number): void--><!--Device-DataChangeListener-onDataAdd(index: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## onDataAdded

```TypeScript
onDataAdded(index: number): void
```

Invoked when data is added to the position indicated by the specified index. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 8. Use > [onDataAdd](#ondataadd) instead.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [onDataAdd](#ondataadd)

<!--Device-DataChangeListener-onDataAdded(index: number): void--><!--Device-DataChangeListener-onDataAdded(index: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## onDataChange

```TypeScript
onDataChange(index: number): void
```

Invoked when data in the position indicated by the specified index is changed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DataChangeListener-onDataChange(index: number): void--><!--Device-DataChangeListener-onDataChange(index: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## onDataChanged

```TypeScript
onDataChanged(index: number): void
```

Invoked when data in the position indicated by the specified index is changed. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 8. Use > [onDataChange](#ondatachange) instead.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [onDataChange](#ondatachange)

<!--Device-DataChangeListener-onDataChanged(index: number): void--><!--Device-DataChangeListener-onDataChanged(index: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## onDataDelete

```TypeScript
onDataDelete(index: number): void
```

Invoked when data is deleted from the position indicated by the specified index. LazyForEach will update the displayed content accordingly. > **NOTE：**> > Before **onDataDelete** is called, ensure that the corresponding data in **dataSource** has been deleted. > Otherwise, undefined behavior will occur during page rendering.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DataChangeListener-onDataDelete(index: number): void--><!--Device-DataChangeListener-onDataDelete(index: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## onDataDeleted

```TypeScript
onDataDeleted(index: number): void
```

Invoked when data is deleted from the position indicated by the specified index. LazyForEach will update the displayed content accordingly. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 8. Use > [onDataDelete](#ondatadelete) instead.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [onDataDelete](#ondatadelete)

<!--Device-DataChangeListener-onDataDeleted(index: number): void--><!--Device-DataChangeListener-onDataDeleted(index: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## onDataMove

```TypeScript
onDataMove(from: number, to: number): void
```

Invoked when data is moved, that is, when data is swapped between the **from** and **to** positions. > **NOTE：**> > The ID must remain unchanged before and after data movement. If the ID changes, APIs for deleting and adding data > must be called.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DataChangeListener-onDataMove(from: number, to: number): void--><!--Device-DataChangeListener-onDataMove(from: number, to: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | number | Yes |
| to | number | Yes |

## onDataMoved

```TypeScript
onDataMoved(from: number, to: number): void
```

Invoked when data is moved, that is, when data is swapped between the **from** and **to** positions. > **NOTE：**> > - This API is supported since API version 7 and deprecated since API version 8. Use > [onDataMove](#ondatamove) instead. > > - The ID must remain unchanged before and after data movement. If the ID changes, APIs for deleting and adding > data must be called.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [onDataMove](#ondatamove)

<!--Device-DataChangeListener-onDataMoved(from: number, to: number): void--><!--Device-DataChangeListener-onDataMoved(from: number, to: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | number | Yes |
| to | number | Yes |

## onDataReloaded

```TypeScript
onDataReloaded(): void
```

Invoked when all data is reloaded. For data items whose key remains unchanged, the original child component is used. For data items whose key changes, a new child component is created.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DataChangeListener-onDataReloaded(): void--><!--Device-DataChangeListener-onDataReloaded(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDataReloaded

```TypeScript
onDataReloaded(reuseImmediately: boolean): void
```

Invoked when all data is reloaded. When \@Reuseable or \@ReuseableV2 is used and recycle pool is empty, old child components will be recycled and then be reused as new child components. If no old child component can be reused, new child components will be created.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DataChangeListener-onDataReloaded(reuseImmediately: boolean): void--><!--Device-DataChangeListener-onDataReloaded(reuseImmediately: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [reuseImmediately](arkts-arkui-datareloadoperation-i.md) | boolean | Yes |

## onDatasetChange

```TypeScript
onDatasetChange(dataOperations: DataOperation[]): void
```

Invoked when data is processed in batches to notify the component of refreshing. > **NOTE：**> > This API cannot be used together with other data operation APIs of **DataChangeListener**. For example, in the > same **LazyForEach**, if you have called **onDataAdd**, do not call **onDatasetChange**; if you have called > **onDatasetChange**, do not call **onDataAdd** or other data operation APIs. Different **LazyForEach** instances > on the page do not affect each other. When data is processed in batches within the same **onDatasetChange** > callback, if multiple **DataOperation** instances target the same index, only the first **DataOperation** will > take effect.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataChangeListener-onDatasetChange(dataOperations: DataOperation[]): void--><!--Device-DataChangeListener-onDatasetChange(dataOperations: DataOperation[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataOperations | [DataOperation](arkts-arkui-dataoperation-t.md)[] | Yes |
