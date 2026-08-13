# Initializer

```TypeScript
export type Initializer<T> = (...params: FixedArray<RecordData>) => T
```

function that returns by the function updateConstructorParams.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type Initializer<T> = (...params: FixedArray<RecordData>) => T--><!--Device-unnamed-export type Initializer<T> = (...params: FixedArray<RecordData>) => T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | FixedArray&lt;[RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T | - |

