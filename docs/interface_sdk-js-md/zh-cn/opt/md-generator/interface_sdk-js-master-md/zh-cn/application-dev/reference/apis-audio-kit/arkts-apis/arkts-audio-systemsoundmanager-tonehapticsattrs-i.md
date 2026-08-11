# ToneHapticsAttrs

系统铃音的振动属性。在调用ToneHapticsAttrs&lt;sup&gt;14+&lt;/sup&gt;的接口前，需要先通过  
[getToneHapticsList](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#gettonehapticslist)或  
[getHapticsAttrsSyncedWithTone](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#gethapticsattrssyncedwithtone)方法获取实例。

**起始版本：** 14

<!--Device-systemSoundManager-interface ToneHapticsAttrs--><!--Device-systemSoundManager-interface ToneHapticsAttrs-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

## getFileName

```TypeScript
getFileName(): string
```

获取振动文件名。

**起始版本：** 14

<!--Device-ToneHapticsAttrs-getFileName(): string--><!--Device-ToneHapticsAttrs-getFileName(): string-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
toneHapticsAttrs.getFileName();
```

## getGentleFileName

```TypeScript
getGentleFileName(): string | null
```

获取柔和振动文件名。

**起始版本：** 22

<!--Device-ToneHapticsAttrs-getGentleFileName(): string | null--><!--Device-ToneHapticsAttrs-getGentleFileName(): string | null-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
toneHapticsAttrs.getGentleFileName();
```

## getGentleTitle

```TypeScript
getGentleTitle(): string | null
```

获取柔和振动标题。

**起始版本：** 22

<!--Device-ToneHapticsAttrs-getGentleTitle(): string | null--><!--Device-ToneHapticsAttrs-getGentleTitle(): string | null-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
toneHapticsAttrs.getGentleTitle();
```

## getGentleUri

```TypeScript
getGentleUri(): string | null
```

获取柔和振动资源路径。

**起始版本：** 22

<!--Device-ToneHapticsAttrs-getGentleUri(): string | null--><!--Device-ToneHapticsAttrs-getGentleUri(): string | null-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
toneHapticsAttrs.getGentleUri();
```

## getTitle

```TypeScript
getTitle(): string
```

获取振动标题。

**起始版本：** 14

<!--Device-ToneHapticsAttrs-getTitle(): string--><!--Device-ToneHapticsAttrs-getTitle(): string-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
toneHapticsAttrs.getTitle();
```

## getUri

```TypeScript
getUri(): string
```

获取振动资源路径。

**起始版本：** 14

<!--Device-ToneHapticsAttrs-getUri(): string--><!--Device-ToneHapticsAttrs-getUri(): string-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
toneHapticsAttrs.getUri();
```
