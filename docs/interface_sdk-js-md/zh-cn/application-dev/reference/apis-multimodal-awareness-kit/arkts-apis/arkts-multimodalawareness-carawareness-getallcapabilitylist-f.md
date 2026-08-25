# getAllCapabilityList

## 导入模块

```TypeScript
import { carAwareness } from '@kit.MultimodalAwarenessKit';
```

## getAllCapabilityList

```TypeScript
function getAllCapabilityList(): Promise<Capability[]>
```

返回所有能力列表

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalAwareness.CarAwareness

**返回值：**

| 类型 |
| --- |
| Promise & lt;Capability[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000001](../errorcode-carAwareness.md#34000001-服务异常) |
