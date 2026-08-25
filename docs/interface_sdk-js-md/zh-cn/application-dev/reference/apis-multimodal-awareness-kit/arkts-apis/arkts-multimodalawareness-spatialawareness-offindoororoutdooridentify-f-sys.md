# offIndoorOrOutdoorIdentify（系统接口）

## 导入模块

```TypeScript
import { spatialAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## offIndoorOrOutdoorIdentify

```TypeScript
function offIndoorOrOutdoorIdentify(configParams: DistanceMeasurementConfigParams,
    callback?: Callback<DoorPositionResponse>): void
```

取消订阅门内外识别接口。停止运行已订阅的门内外识别算法。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_SENSING_WITH_ULTRASOUND

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configParams | [DistanceMeasurementConfigParams](arkts-multimodalawareness-spatialawareness-distancemeasurementconfigparams-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DoorPositionResponse](arkts-multimodalawareness-spatialawareness-doorpositionresponse-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35100001](../errorcode-spatialAwareness.md#35100001-服务异常) |
| [35100003](../errorcode-spatialAwareness.md#35100003-取消订阅失败) |
| [35100004](../errorcode-spatialAwareness.md#35100004-无效参数) |
