# OIS

OIS (Optical Image Stabilization) interface.

**继承/实现关系：** OIS extends [OISQuery](arkts-camera-camera-oisquery-i.md)

**起始版本：** 24

<!--Device-camera-interface OIS extends OISQuery--><!--Device-camera-interface OIS extends OISQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## setOISMode

```TypeScript
setOISMode(mode: OISMode): void
```

Sets the OIS mode.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-OIS-setOISMode(mode: OISMode): void--><!--Device-OIS-setOISMode(mode: OISMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [OISMode](arkts-camera-camera-oismode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setOISModeCustom

```TypeScript
setOISModeCustom(pitch: number, yaw: number): void
```

Sets custom OIS bias values for each axis.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-OIS-setOISModeCustom(pitch: double, yaw: double): void--><!--Device-OIS-setOISModeCustom(pitch: double, yaw: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pitch | number | 是 |
| yaw | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
