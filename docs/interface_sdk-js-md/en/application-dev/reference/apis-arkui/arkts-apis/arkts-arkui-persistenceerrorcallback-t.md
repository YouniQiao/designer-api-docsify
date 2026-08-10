# PersistenceErrorCallback

```TypeScript
export declare type PersistenceErrorCallback = (key: string, reason: string, message: string, 
    oldValue?: string) => void
```

持久化失败时返回错误原因的回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type PersistenceErrorCallback = (key: string, reason: string, message: string,     oldValue?: string) => void--><!--Device-unnamed-export declare type PersistenceErrorCallback = (key: string, reason: string, message: string,     oldValue?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 出错的键值。 |
| reason | string | Yes | 出错的原因类型。 |
| message | string | Yes | 出错的更多消息。 |
| oldValue | string | No | 反序列化失败时返回原始序列化数据。 |

