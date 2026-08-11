# createCustomizedToneAttrs

## createCustomizedToneAttrs

```TypeScript
function createCustomizedToneAttrs(): ToneAttrs
```

创建自定义铃声属性。

**起始版本：** 12

<!--Device-systemSoundManager-function createCustomizedToneAttrs(): ToneAttrs--><!--Device-systemSoundManager-function createCustomizedToneAttrs(): ToneAttrs-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let toneAttrs: systemSoundManager.ToneAttrs = systemSoundManager.createCustomizedToneAttrs();
```
