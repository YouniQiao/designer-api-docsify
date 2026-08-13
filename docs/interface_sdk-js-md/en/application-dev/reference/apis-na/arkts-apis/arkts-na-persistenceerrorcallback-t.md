# PersistenceErrorCallback

```TypeScript
export declare type PersistenceErrorCallback = (key: string, reason: string, message: string, 
    oldValue?: string) => void
```

Function that returns the reason type when an error occurs.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type PersistenceErrorCallback = (key: string, reason: string, message: string,     oldValue?: string) => void--><!--Device-unnamed-export declare type PersistenceErrorCallback = (key: string, reason: string, message: string,     oldValue?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | persisted key when an error occurs |
| reason | string | Yes | reason type when an error occurs, possible values are 'quota', 'serialization', 'unknown' |
| message | string | Yes | Additional message when an error occurs. |
| oldValue | string | No | value in storage that cannot be deserialized. |

