# getInspectorTree

## Modules to Import

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## getInspectorTree

```TypeScript
function getInspectorTree(): RecordData
```

获取组件树及组件属性。

此接口仅用于对应用的测试。由于耗时长，不建议测试之外的场景使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inspector-function getInspectorTree(): RecordData--><!--Device-inspector-function getInspectorTree(): RecordData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | 组件树及组件属性列表的JSON对象。组件中每个字段的含义请参考getInspectorInfo的返回值说明。 |

