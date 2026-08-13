# getMediaKeySystems

## getMediaKeySystems

```TypeScript
function getMediaKeySystems(): MediaKeySystemDescription[]
```

Get all media key systems supported.

**起始版本：** 12

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-drm-function getMediaKeySystems(): MediaKeySystemDescription[]--><!--Device-drm-function getMediaKeySystems(): MediaKeySystemDescription[]-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [MediaKeySystemDescription](arkts-drm-drm-mediakeysystemdescription-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [24700201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-服务异常) |
| [24700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-未知错误) |

## 示例

```TypeScript
import { drm } from '@kit.DrmKit';

let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
// 验证返回结果，description为插件信息列表，包含插件名称和唯一标识。
if (description.length > 0) {
  console.info(`getMediaKeySystems success, count: ${description.length}`);
  for (let i = 0; i < description.length; i++) {
    console.info(`name: ${description[i].name}, uuid: ${description[i].uuid}`);
  }
} else {
  console.info('No DRM system available');
}
```
