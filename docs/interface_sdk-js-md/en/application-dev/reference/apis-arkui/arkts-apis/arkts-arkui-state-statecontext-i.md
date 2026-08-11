# StateContext

Context of a state, keeping track of changes in the given scope.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface StateContext--><!--Device-unnamed-export declare interface StateContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scope

```TypeScript
scope<T>(id: int, paramCount: int): IncrementalScope<T>
```

The scope which is used to track the changes of state context.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StateContext-scope<T>(id: int, paramCount: int): IncrementalScope<T>--><!--Device-StateContext-scope<T>(id: int, paramCount: int): IncrementalScope<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | state context id |
| paramCount | int | Yes | the count of param |

**Return value:**

| Type | Description |
| --- | --- |
| [IncrementalScope](arkts-arkui-state-incrementalscope-i.md)&lt;T&gt; | return state scope |

