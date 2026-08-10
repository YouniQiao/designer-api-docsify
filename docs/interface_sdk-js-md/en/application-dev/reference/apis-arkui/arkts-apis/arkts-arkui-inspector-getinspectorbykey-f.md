# getInspectorByKey

## Modules to Import

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## getInspectorByKey

```TypeScript
function getInspectorByKey(id: string): string
```

获取指定id组件的所有属性，不包括子组件信息。

此接口仅用于对应用的测试，使用时建议等应用启动且布局完成后再调用。由于耗时长，不建议测试之外的场景使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inspector-function getInspectorByKey(id: string): string--><!--Device-inspector-function getInspectorByKey(id: string): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 要获取属性的组件id。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 组件属性列表的JSON字符串。字符串信息包含组件的tag、id、位置信息（相对于窗口左上角的坐标）以及用于测试检查的组件所包含的相关属性信息。 组件中每个字段的含义请参考getInspectorInfo的返回值说明。 |

