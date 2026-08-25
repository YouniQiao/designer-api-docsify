# getMediaKeySystemUuid

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## getMediaKeySystemUuid

```TypeScript
function getMediaKeySystemUuid(name: string): string
```

获取DRM解决方案支持的DRM内容保护系统唯一标识。

**起始版本：** 12

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
