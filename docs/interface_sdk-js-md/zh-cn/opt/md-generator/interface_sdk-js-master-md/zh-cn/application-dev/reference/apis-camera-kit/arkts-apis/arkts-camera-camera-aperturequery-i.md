# ApertureQuery

Provides the aperture query capability.

**起始版本：** 24

<!--Device-camera-interface ApertureQuery--><!--Device-camera-interface ApertureQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getSupportedPhysicalApertures

```TypeScript
getSupportedPhysicalApertures(): Array<PhysicalAperture>
```

Gets the supported physical apertures.Move to ApertureQuery interface from Aperture since 12.

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ApertureQuery-getSupportedPhysicalApertures(): Array<PhysicalAperture>--><!--Device-ApertureQuery-getSupportedPhysicalApertures(): Array<PhysicalAperture>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;PhysicalAperture&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSupportedVirtualApertures

```TypeScript
getSupportedVirtualApertures(): Array<number>
```

Obtains the supported virtual apertures.

**起始版本：** 11

<!--Device-ApertureQuery-getSupportedVirtualApertures(): Array<double>--><!--Device-ApertureQuery-getSupportedVirtualApertures(): Array<double>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function getSupportedVirtualApertures(session: camera.PortraitPhotoSession): Array<number> {
  let virtualApertures: Array<number> = session.getSupportedVirtualApertures();
  return virtualApertures;
}
```
