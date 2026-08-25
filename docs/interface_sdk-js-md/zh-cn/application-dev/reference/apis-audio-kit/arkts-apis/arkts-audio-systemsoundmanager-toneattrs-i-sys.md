# ToneAttrs（系统接口）

管理铃声属性。在调用ToneAttrs&lt;sup&gt;12+&lt;/sup&gt;的接口前，需要先通过 [createCustomizedToneAttrs](arkts-audio-systemsoundmanager-createcustomizedtoneattrs-f-sys.md)或 [getDefaultRingtoneAttrs](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md#getdefaultringtoneattrs)、 [getRingtoneAttrList](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md#getringtoneattrlist)等方法获取实例。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## getCategory

```TypeScript
getCategory(): number
```

获取铃声类别。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCustomizedType

```TypeScript
getCustomizedType(): ToneCustomizedType
```

获取铃声自定义类型。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [ToneCustomizedType](arkts-audio-systemsoundmanager-tonecustomizedtype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getFileName

```TypeScript
getFileName(): string
```

获取铃声文件名。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getMediaType

```TypeScript
getMediaType():MediaType
```

获取铃声类型。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [MediaType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediatype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getTitle

```TypeScript
getTitle(): string
```

获取铃声标题。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getUri

```TypeScript
getUri(): string
```

获取铃声资源路径。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setCategory

```TypeScript
setCategory(category: number): void
```

设置铃声类别。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| category | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setFileName

```TypeScript
setFileName(name: string): void
```

设置铃声文件名。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setMediaType

```TypeScript
setMediaType(type:MediaType):void
```

设置铃声类型。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [MediaType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediatype-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setTitle

```TypeScript
setTitle(title: string): void
```

设置铃声标题。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| title | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
