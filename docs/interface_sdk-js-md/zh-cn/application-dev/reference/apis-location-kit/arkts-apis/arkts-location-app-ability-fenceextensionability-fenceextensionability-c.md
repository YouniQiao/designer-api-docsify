# FenceExtensionAbility

FenceExtensionAbility为开发者提供的地理围栏相关的能力。

**起始版本：** 14

**系统能力：** SystemCapability.Location.Location.Geofence

## 导入模块

```TypeScript
import { FenceExtensionAbility } from 'kits/@kit.LocationKit';
```

## onDestroy

```TypeScript
onDestroy(): void
```

接收FenceExtensionAbility的销毁事件并处理，会在FenceExtensionAbility销毁前回调。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Location.Location.Geofence

## onFenceStatusChange

```TypeScript
onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void
```

接收系统通知的地理围栏事件，根据围栏事件类型和数据进行相应处理。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transition | geoLocationManager.GeofenceTransition | 是 |
| additions | Record & lt;string, string & gt; | 是 |

## context

```TypeScript
context: FenceExtensionContext
```

表示围栏的的上下文环境。

**类型：** [FenceExtensionContext](arkts-location-app-ability-fenceextensioncontext-fenceextensioncontext-c-sys.md)

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Location.Location.Geofence
