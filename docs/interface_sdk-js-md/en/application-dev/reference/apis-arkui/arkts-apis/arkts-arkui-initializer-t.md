# Initializer

```TypeScript
export type Initializer<T> = (...params: FixedArray<RecordData>) => T
```

可以将属性更新到本地的修饰器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type Initializer<T> = (...params: FixedArray<RecordData>) => T--><!--Device-unnamed-export type Initializer<T> = (...params: FixedArray<RecordData>) => T-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | FixedArray&lt;RecordData&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

