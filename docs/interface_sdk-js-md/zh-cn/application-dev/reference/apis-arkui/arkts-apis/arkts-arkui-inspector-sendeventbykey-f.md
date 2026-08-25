# sendEventByKey

## 导入模块

```TypeScript
import { inspector } from '@kit.ArkUI';
```

## sendEventByKey

```TypeScript
function sendEventByKey(id: string, action: int, params: string): boolean
```

给指定id的组件发送事件。此接口仅用于对应用的测试。由于耗时长，不建议测试之外的场景使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| action | int | 是 |
| params | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
