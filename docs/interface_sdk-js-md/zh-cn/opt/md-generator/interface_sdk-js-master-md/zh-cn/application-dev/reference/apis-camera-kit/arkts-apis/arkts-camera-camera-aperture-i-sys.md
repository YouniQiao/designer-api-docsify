# Aperture（系统接口）

Provides the APIs for aperture settings. It inherits from [ApertureQuery](arkts-camera-camera-aperturequery-i-sys.md#ApertureQuery（系统接口）).

**继承/实现关系：** Aperture extends [ApertureQuery](arkts-camera-camera-aperturequery-i-sys.md#ApertureQuery（系统接口）)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface Aperture--><!--Device-camera-interface Aperture-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getPhysicalAperture

```TypeScript
getPhysicalAperture(): number
```

Gets current physical aperture value.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-Aperture-getPhysicalAperture(): double--><!--Device-Aperture-getPhysicalAperture(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getVirtualAperture

```TypeScript
getVirtualAperture(): number
```

Obtains the virtual aperture in use.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Aperture-getVirtualAperture(): double--><!--Device-Aperture-getVirtualAperture(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function getVirtualAperture(session: camera.PortraitPhotoSession): number {
  let virtualAperture: number = session.getVirtualAperture();
  return virtualAperture;
}
```

## setPhysicalAperture

```TypeScript
setPhysicalAperture(aperture: number): void
```

Sets physical aperture value.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-Aperture-setPhysicalAperture(aperture: double): void--><!--Device-Aperture-setPhysicalAperture(aperture: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [aperture](arkts-camera-camera-apertureinfo-i-sys.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setVirtualAperture

```TypeScript
setVirtualAperture(aperture: number): void
```

Sets a virtual aperture. Before the setting, call [getSupportedVirtualApertures](arkts-camera-camera-aperturequery-i-sys.md#getSupportedVirtualApertures) to obtain the supported virtual apertures.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Aperture-setVirtualAperture(aperture: double): void--><!--Device-Aperture-setVirtualAperture(aperture: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [aperture](arkts-camera-camera-apertureinfo-i-sys.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function setVirtualAperture(session: camera.PortraitPhotoSession, virtualAperture: number): void {
  session.setVirtualAperture(virtualAperture);
}
```
