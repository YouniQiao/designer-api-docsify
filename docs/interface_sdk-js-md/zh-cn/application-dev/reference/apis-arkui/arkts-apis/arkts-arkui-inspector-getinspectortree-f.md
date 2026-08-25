# getInspectorTree

## 导入模块

```TypeScript
import { inspector } from '@kit.ArkUI';
```

## getInspectorTree

```TypeScript
function getInspectorTree(): RecordData
```

获取组件树及组件属性。此接口仅用于对应用的测试。由于耗时长，不建议测试之外的场景使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md) |
