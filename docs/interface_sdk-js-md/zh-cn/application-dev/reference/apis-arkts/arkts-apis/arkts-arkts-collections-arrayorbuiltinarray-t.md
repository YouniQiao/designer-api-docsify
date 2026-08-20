# ArrayOrBuiltinArray

```TypeScript
type ArrayOrBuiltinArray<T> = Array<T> | BuiltinArray<T>
```

ArkTS Array接口参数类型，表示ArkTS Array或内建Array。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务API中使用。

<!--Device-collections-type ArrayOrBuiltinArray<T> = Array<T> | BuiltinArray<T>--><!--Device-collections-type ArrayOrBuiltinArray<T> = Array<T> | BuiltinArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | ArkTS Array. |
| BuiltinArray&lt;T&gt; | 内建Array. |

