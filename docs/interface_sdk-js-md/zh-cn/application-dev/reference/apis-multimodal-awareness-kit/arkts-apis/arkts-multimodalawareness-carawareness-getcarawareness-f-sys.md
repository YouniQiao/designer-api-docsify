# getCarAwareness（系统接口）

## 导入模块

```TypeScript
import { carAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## getCarAwareness

```TypeScript
function getCarAwareness(capability: Capability, options?: CarAwarenessOptions): Promise<CarAwarenessInfo[]>
```

/** 关闭汽车感知，订阅汽车感知结果。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalAwareness.CarAwareness

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capability | [Capability](arkts-multimodalawareness-carawareness-capability-e.md) | 是 |
| options | [CarAwarenessOptions](arkts-multimodalawareness-carawareness-carawarenessoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CarAwarenessInfo](arkts-multimodalawareness-carawareness-carawarenessinfo-i-sys.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000001](../errorcode-carAwareness.md#34000001-服务异常) |
| [34000002](../errorcode-carAwareness.md#34000002-指定能力不支持) |
