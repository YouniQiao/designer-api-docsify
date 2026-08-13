# getMediaKeySystemUuid

## getMediaKeySystemUuid

```TypeScript
function getMediaKeySystemUuid(name: string): string
```

Get a MediaKeySystem's UUID.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-drm-function getMediaKeySystemUuid(name: string): string--><!--Device-drm-function getMediaKeySystemUuid(name: string): string-End-->

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
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## 示例

```TypeScript
import { drm } from '@kit.DrmKit';

let uuid: string = drm.getMediaKeySystemUuid('com.clearplay.drm');
console.info("getMediaKeySystemUuid: ", uuid);
```
