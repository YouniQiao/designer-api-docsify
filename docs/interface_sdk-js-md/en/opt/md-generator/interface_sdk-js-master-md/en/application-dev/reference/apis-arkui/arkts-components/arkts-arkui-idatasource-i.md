# IDataSource

Data source of **LazyForEach**.

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-declare interface IDataSource--><!--Device-unnamed-declare interface IDataSource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getData

```TypeScript
getData(index: number): any
```

Obtains the data item that matches the specified index.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IDataSource-getData(index: number): any--><!--Device-IDataSource-getData(index: number): any-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

## registerDataChangeListener

```TypeScript
registerDataChangeListener(listener: DataChangeListener): void
```

Registers a listener for data changes.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listener | [DataChangeListener](arkts-arkui-datachangelistener-i.md) | Yes |

## totalCount

```TypeScript
totalCount(): number
```

Obtains the total number of data items.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IDataSource-totalCount(): number--><!--Device-IDataSource-totalCount(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## unregisterDataChangeListener

```TypeScript
unregisterDataChangeListener(listener: DataChangeListener): void
```

Unregisters the listener for data changes.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listener | [DataChangeListener](arkts-arkui-datachangelistener-i.md) | Yes |
