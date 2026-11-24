# PhotoQualityPrioritization

```TypeScript
enum PhotoQualityPrioritization
```

枚举，拍照画质优先策略。

**起始版本：** 21

<!--Device-camera-enum PhotoQualityPrioritization--><!--Device-camera-enum PhotoQualityPrioritization-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## HIGH_QUALITY

```TypeScript
HIGH_QUALITY = 0
```

画质优先，拍照需要较长的时间，以输出高画质的图片。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务中使用。

<!--Device-PhotoQualityPrioritization-HIGH_QUALITY = 0--><!--Device-PhotoQualityPrioritization-HIGH_QUALITY = 0-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## LOW_QUALITY

```TypeScript
LOW_QUALITY = 2
```

专注于低开销，在降低图像质量的情况下优先获得最短的捕获时间。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-PhotoQualityPrioritization-LOW_QUALITY = 2--><!--Device-PhotoQualityPrioritization-LOW_QUALITY = 2-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## SPEED

```TypeScript
SPEED = 1
```

性能优先，会降低画质来提升拍照的速度。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务中使用。

<!--Device-PhotoQualityPrioritization-SPEED = 1--><!--Device-PhotoQualityPrioritization-SPEED = 1-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core
