# Nullable

```TypeScript
declare type Nullable<T> = T | undefined
```

The value of this type can be the type specified by the generic parameter **T**, or **undefined**.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| T | Type specified by the generic parameter T. |
| undefined | The object is **undefined**. |
