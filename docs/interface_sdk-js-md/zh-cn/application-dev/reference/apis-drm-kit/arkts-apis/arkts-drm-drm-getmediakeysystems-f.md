# getMediaKeySystems

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## getMediaKeySystems

```TypeScript
function getMediaKeySystems(): MediaKeySystemDescription[]
```

获取设备支持的插件信息列表。

**起始版本：** 12

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [MediaKeySystemDescription](arkts-drm-drm-mediakeysystemdescription-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
