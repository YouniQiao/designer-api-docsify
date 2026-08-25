# Aperture

物理光圈对象。Aperture继承自ApertureQuery。

**继承/实现关系：** Aperture extends [ApertureQuery](arkts-camera-camera-aperturequery-i.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getVirtualAperture

ArkTS-Dyn:
```TypeScript
getVirtualAperture(): number
```

ArkTS-Sta:
```TypeScript
getVirtualAperture(): double
```

获取当前设置的虚拟光圈值。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

**示例**

```TypeScript
function getVirtualAperture(session: camera.PortraitPhotoSession): number {
  let virtualAperture: number = session.getVirtualAperture();
  return virtualAperture;
}
```

## setVirtualAperture

ArkTS-Dyn:
```TypeScript
setVirtualAperture(aperture: number): void
```

ArkTS-Sta:
```TypeScript
setVirtualAperture(aperture: double): void
```

设置虚拟光圈。可以先通过getSupportedVirtualApertures获取当前设备所支持的虚拟光圈列表。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [aperture](arkts-camera-camera-apertureinfo-i-sys.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

**示例**

```TypeScript
function setVirtualAperture(session: camera.PortraitPhotoSession, virtualAperture: number): void {
  session.setVirtualAperture(virtualAperture);
}
```
