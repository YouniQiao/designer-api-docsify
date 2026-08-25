# StateContext

Context of a state, keeping track of changes in the given scope.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scope

```TypeScript
scope<T>(id: int, paramCount: int): IncrementalScope<T>
```

The scope which is used to track the changes of state context.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | int | 是 |
| paramCount | int | 是 |

**返回值：**

| 类型 |
| --- |
| [IncrementalScope](arkts-arkui-state-incrementalscope-i.md)&lt;T&gt; |
