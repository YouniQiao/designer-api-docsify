# isFusionFenceSupported（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isFusionFenceSupported

```TypeScript
function isFusionFenceSupported(): boolean
```

判断系统是否支持融合围栏能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
