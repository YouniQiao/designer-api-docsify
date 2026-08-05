# AbstractProperty

Provides a reference to properties stored in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface AbstractProperty<T>--><!--Device-unnamed-declare interface AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## get

```TypeScript
get(): T
```

Reads data of the referenced property from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbstractProperty-get(): T--><!--Device-AbstractProperty-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | Data of the referenced property in AppStorage or LocalStorage. |

## info

```TypeScript
info(): string
```

Reads the property name of the referenced property from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbstractProperty-info(): string--><!--Device-AbstractProperty-info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Property name of the referenced property in AppStorage or LocalStorage. |

## set

```TypeScript
set(newValue: T): void
```

Updates the data of the referenced property in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_. The value of **newValue** must be of the **T** type and can be **null** or **undefined**. > **NOTE** > Since API version 12, AppStorage and LocalStorage support the Map, Set, Date types, as well as **null**, > **undefined**, and union types.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbstractProperty-set(newValue: T): void--><!--Device-AbstractProperty-set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | New data to update. The value can be **null** or **undefined**. |

