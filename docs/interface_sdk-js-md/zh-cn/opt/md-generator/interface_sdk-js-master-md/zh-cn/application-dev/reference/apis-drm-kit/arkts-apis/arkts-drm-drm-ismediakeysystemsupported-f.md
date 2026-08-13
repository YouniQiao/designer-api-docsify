# isMediaKeySystemSupported

## isMediaKeySystemSupported

```TypeScript
function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean
```

Judge whether a system that specifies name, mimetype and content protection level is supported.

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean--><!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| mimeType | string | 是 |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [24700201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-服务异常) |
| [24700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-未知错误) |

## 示例

```TypeScript
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.clearplay.drm', 'video/avc', drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
console.info("isMediaKeySystemSupported: ", supported);
```


## isMediaKeySystemSupported

```TypeScript
function isMediaKeySystemSupported(name: string, mimeType: string): boolean
```

Judge whether a system that specifies name, mimetype is supported.

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string): boolean--><!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| mimeType | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [24700201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-服务异常) |
| [24700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-未知错误) |

## 示例

```TypeScript
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.clearplay.drm', 'video/avc');
console.info("isMediaKeySystemSupported: ", supported);
```


## isMediaKeySystemSupported

```TypeScript
function isMediaKeySystemSupported(name: string): boolean
```

Judge whether a system that specifies name is supported.

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-drm-function isMediaKeySystemSupported(name: string): boolean--><!--Device-drm-function isMediaKeySystemSupported(name: string): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [24700201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-服务异常) |
| [24700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-未知错误) |

## 示例

```TypeScript
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.clearplay.drm');
console.info("isMediaKeySystemSupported: ", supported);
```
