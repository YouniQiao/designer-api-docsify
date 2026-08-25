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

## getPhysicalAperture

ArkTS-Dyn:
```TypeScript
getPhysicalAperture(): number
```

ArkTS-Sta:
```TypeScript
getPhysicalAperture(): double
```

获取当前物理光圈值。

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |

## setPhysicalAperture

ArkTS-Dyn:
```TypeScript
setPhysicalAperture(aperture: number): void
```

ArkTS-Sta:
```TypeScript
setPhysicalAperture(aperture: double): void
```

设置物理光圈值。需要先通过getSupportedPhysicalApertures接口获取不同焦段支持的可设置光圈值，再通过调整焦段范围，设置支持的物理光圈值。

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [aperture](arkts-camera-camera-apertureinfo-i-sys.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
