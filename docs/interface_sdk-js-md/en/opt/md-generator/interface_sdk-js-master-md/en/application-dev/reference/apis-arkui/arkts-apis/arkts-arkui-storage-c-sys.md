# Storage (System API)

Defines the base class of storage.

**Since:** 7

<!--Device-unnamed-declare class Storage--><!--Device-unnamed-declare class Storage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## clear

```TypeScript
clear(): void
```

Called when data is cleared.

**Since:** 7

<!--Device-Storage-clear(): void--><!--Device-Storage-clear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## constructor

```TypeScript
constructor(needCrossThread?: boolean, file?: string)
```

Constructor parameters.

**Since:** 7

<!--Device-Storage-constructor(needCrossThread?: boolean, file?: string)--><!--Device-Storage-constructor(needCrossThread?: boolean, file?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needCrossThread | boolean | No |
| file | string | No |

## delete

```TypeScript
delete(key: string): void
```

Called when data is deleted.

**Since:** 7

<!--Device-Storage-delete(key: string): void--><!--Device-Storage-delete(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

## get

```TypeScript
get(key: string): string | undefined
```

Called when data is obtained.

**Since:** 7

<!--Device-Storage-get(key: string): string | undefined--><!--Device-Storage-get(key: string): string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## set

```TypeScript
set(key: string, val: any): void
```

Called when setting.

**Since:** 7

<!--Device-Storage-set(key: string, val: any): void--><!--Device-Storage-set(key: string, val: any): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| val | any | Yes |
