# ToneHapticsAttrs（系统接口）

系统铃音的振动属性。在调用ToneHapticsAttrs&lt;sup&gt;14+&lt;/sup&gt;的接口前，需要先通过 [getToneHapticsList](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md#gettonehapticslist)或 [getHapticsAttrsSyncedWithTone](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md#gethapticsattrssyncedwithtone)方法获取实例。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## getFileName

```TypeScript
getFileName(): string
```

获取振动文件名。

**起始版本：** 14

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

## getGentleFileName

```TypeScript
getGentleFileName(): string | null
```

获取柔和振动文件名。

**起始版本：** 22

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string \| null |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getGentleTitle

```TypeScript
getGentleTitle(): string | null
```

获取柔和振动标题。

**起始版本：** 22

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string \| null |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getGentleUri

```TypeScript
getGentleUri(): string | null
```

获取柔和振动资源路径。

**起始版本：** 22

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string \| null |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getTitle

```TypeScript
getTitle(): string
```

获取振动标题。

**起始版本：** 14

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

获取振动资源路径。

**起始版本：** 14

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
