# FlashQuery

提供了查询设备的闪光灯状态和模式的能力。

> **说明：**
> 
> - 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

**起始版本：** 12

<!--Device-camera-interface FlashQuery--><!--Device-camera-interface FlashQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## hasFlash

```TypeScript
hasFlash(): boolean
```

检测是否有闪光灯，返回是否支持闪光灯。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-FlashQuery-hasFlash(): boolean--><!--Device-FlashQuery-hasFlash(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## isFlashModeSupported

```TypeScript
isFlashModeSupported(flashMode: FlashMode): boolean
```

检测闪光灯模式是否支持。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-FlashQuery-isFlashModeSupported(flashMode: FlashMode): boolean--><!--Device-FlashQuery-isFlashModeSupported(flashMode: FlashMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
