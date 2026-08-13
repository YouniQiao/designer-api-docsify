# getSystemSoundManager（系统接口）

## getSystemSoundManager

```TypeScript
function getSystemSoundManager(): SystemSoundManager
```

获取系统声音管理器。

**起始版本：** 23

**废弃版本：** -1

<!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager--><!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [SystemSoundManager](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md) |

## 示例

```TypeScript
let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
```
