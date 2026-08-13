# PersistenceErrorCallback

```TypeScript
export declare type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown', 
    message: string, oldValue?: string) => void
```

Defines a callback used to return the cause of the persistence failure.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export declare type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown',     message: string, oldValue?: string) => void--><!--Device-unnamed-export declare type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown',     message: string, oldValue?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| reason | 'quota' \| 'serialization' \| 'unknown' | Yes |
| message | string | Yes |
| oldValue | string | No |
