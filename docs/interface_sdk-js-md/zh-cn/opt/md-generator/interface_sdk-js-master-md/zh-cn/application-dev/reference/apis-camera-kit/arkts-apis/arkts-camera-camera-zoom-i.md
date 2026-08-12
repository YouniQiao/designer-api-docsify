# Zoom

Zoom继承自[ZoomQuery](arkts-camera-camera-zoomquery-i.md#ZoomQuery)。

变焦类，对设备变焦操作。

**继承/实现关系：** Zoom extends [ZoomQuery](arkts-camera-camera-zoomquery-i.md#ZoomQuery)

**起始版本：** 11

<!--Device-camera-interface Zoom extends ZoomQuery--><!--Device-camera-interface Zoom extends ZoomQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getZoomRatio

```TypeScript
getZoomRatio(): number
```

获取当前的变焦比。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Zoom-getZoomRatio(): double--><!--Device-Zoom-getZoomRatio(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [7400201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-相机服务异常) |

## setSmoothZoom

```TypeScript
setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void
```

触发平滑变焦。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Zoom-setSmoothZoom(targetRatio: double, mode?: SmoothZoomMode): void--><!--Device-Zoom-setSmoothZoom(targetRatio: double, mode?: SmoothZoomMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetRatio | number | 是 |
| mode | [SmoothZoomMode](arkts-camera-camera-smoothzoommode-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |

## setZoomRatio

```TypeScript
setZoomRatio(zoomRatio: number): void
```

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Zoom-setZoomRatio(zoomRatio: double): void--><!--Device-Zoom-setZoomRatio(zoomRatio: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [zoomRatio](arkts-camera-camera-zoompointinfo-i.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
