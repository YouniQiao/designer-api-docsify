# updateSpatialActionEnableStatus（系统接口）

## 导入模块

```TypeScript
import { carAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## updateSpatialActionEnableStatus

```TypeScript
function updateSpatialActionEnableStatus(event: number): void
```

更新感知启用事件，当应用订阅功能时

**起始版本：** 26.1.0

**需要权限：** ohos.permission.vehicle.MMA_SPATIALACTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalAwareness.CarAwareness

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000001](../errorcode-carAwareness.md#34000001-服务异常) |
| [34000002](../errorcode-carAwareness.md#34000002-指定能力不支持) |
