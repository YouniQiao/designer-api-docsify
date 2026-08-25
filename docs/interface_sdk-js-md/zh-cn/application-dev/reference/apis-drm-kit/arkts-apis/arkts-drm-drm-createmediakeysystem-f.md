# createMediaKeySystem

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem
```

创建MediaKeySystem实例。最多可以创建64个MediaKeySystem实例。超过上限时，会抛出错误码24700103。建议及时调用[destroy](arkts-drm-drm-mediakeysystem-i.md#destroy)接口释放不再使用的MediaKeySystem实例。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

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
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700103](../errorcode-drm.md#24700103-mediakeysystem数量达到极限) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
