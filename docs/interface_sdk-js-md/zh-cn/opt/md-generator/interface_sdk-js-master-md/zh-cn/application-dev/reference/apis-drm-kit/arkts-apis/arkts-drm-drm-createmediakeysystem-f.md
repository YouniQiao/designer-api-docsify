# createMediaKeySystem

## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem
```

Creates a MediaKeySystem instance.

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem--><!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700103](../errorcode-drm.md#24700103-mediakeysystem数量达到极限) |

## 示例

```TypeScript
import { drm } from '@kit.DrmKit';
// name为DRM解决方案名称，可通过drm.getMediaKeySystems接口获取设备支持的DRM解决方案名称，如"com.clearplay.drm"。
let name = 'com.clearplay.drm';
let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem(name);
console.info(`createMediaKeySystem success, name: ${name}`);
```


## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem | undefined
```

Creates a MediaKeySystem instance.

**起始版本：** 23

**废弃版本：** -1

<!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem | undefined--><!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700103](../errorcode-drm.md#24700103-mediakeysystem数量达到极限) |
