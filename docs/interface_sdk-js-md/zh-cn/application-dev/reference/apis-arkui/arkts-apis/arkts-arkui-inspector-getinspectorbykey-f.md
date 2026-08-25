# getInspectorByKey

## 导入模块

```TypeScript
import { inspector } from '@kit.ArkUI';
```

## getInspectorByKey

```TypeScript
function getInspectorByKey(id: string): string
```

获取指定id组件的所有属性，不包括子组件信息。此接口仅用于对应用的测试，使用时建议等应用启动且布局完成后再调用。由于耗时长，不建议测试之外的场景使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |
