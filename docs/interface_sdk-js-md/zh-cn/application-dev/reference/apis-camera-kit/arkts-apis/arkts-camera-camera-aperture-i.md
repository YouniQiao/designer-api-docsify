# Aperture

Provides the APIs for aperture settings. It inherits from [ApertureQuery](arkts-camera-camera-aperturequery-i.md).

**继承/实现关系：** Aperture extends [ApertureQuery](arkts-camera-camera-aperturequery-i.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-camera-interface Aperture extends ApertureQuery--><!--Device-camera-interface Aperture extends ApertureQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getPhysicalAperture

ArkTS-Dyn:
```TypeScript
getPhysicalAperture(): number
```

ArkTS-Sta:
```TypeScript
getPhysicalAperture(): double
```

Gets current physical aperture value.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-Aperture-getPhysicalAperture(): double--><!--Device-Aperture-getPhysicalAperture(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | The current physical aperture value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal.<br>**适用版本：** 24+ |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**适用版本：** 11 - 23 |

## getVirtualAperture

ArkTS-Dyn:
```TypeScript
getVirtualAperture(): number
```

ArkTS-Sta:
```TypeScript
getVirtualAperture(): double
```

Obtains the virtual aperture in use.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-Aperture-getVirtualAperture(): double--><!--Device-Aperture-getVirtualAperture(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Virtual aperture. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 202 | Not System Application. |

## 示例

```TypeScript
function getVirtualAperture(session: camera.PortraitPhotoSession): number {
  let virtualAperture: number = session.getVirtualAperture();
  return virtualAperture;
}
```

## setPhysicalAperture

ArkTS-Dyn:
```TypeScript
setPhysicalAperture(aperture: number): void
```

ArkTS-Sta:
```TypeScript
setPhysicalAperture(aperture: double): void
```

Sets physical aperture value.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-Aperture-setPhysicalAperture(aperture: double): void--><!--Device-Aperture-setPhysicalAperture(aperture: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aperture | ArkTS-Dyn: number  <br>ArkTS-Sta：double | 是 | physical aperture value. The supported physical aperture range can be obtained by calling [getSupportedPhysicalApertures](arkts-camera-camera-aperturequery-i.md#getsupportedphysicalapertures) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal.<br>**适用版本：** 24+ |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**适用版本：** 11 - 23 |

## setVirtualAperture

ArkTS-Dyn:
```TypeScript
setVirtualAperture(aperture: number): void
```

ArkTS-Sta:
```TypeScript
setVirtualAperture(aperture: double): void
```

Sets a virtual aperture. Before the setting, call  
[getSupportedVirtualApertures](arkts-camera-camera-aperturequery-i.md#getsupportedvirtualapertures) to obtain the supported virtual apertures.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-Aperture-setVirtualAperture(aperture: double): void--><!--Device-Aperture-setVirtualAperture(aperture: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aperture | ArkTS-Dyn: number  <br>ArkTS-Sta：double | 是 | virtual aperture value |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 202 | Not System Application. |

## 示例

```TypeScript
function setVirtualAperture(session: camera.PortraitPhotoSession, virtualAperture: number): void {
  session.setVirtualAperture(virtualAperture);
}
```

