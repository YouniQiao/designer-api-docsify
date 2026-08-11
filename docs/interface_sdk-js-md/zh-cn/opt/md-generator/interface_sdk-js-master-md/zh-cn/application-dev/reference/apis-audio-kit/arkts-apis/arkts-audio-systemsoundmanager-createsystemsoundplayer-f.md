# createSystemSoundPlayer

## createSystemSoundPlayer

```TypeScript
function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>
```

创建系统音效播放器对象。使用Promise异步回调。

**起始版本：** 23

<!--Device-systemSoundManager-function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>--><!--Device-systemSoundManager-function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;SystemSoundPlayer \| null&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-内存分配失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
  console.info('Succeeded in creating the system sound player.');
  systemSoundPlayer = systemSoundPlayerInstance;
}).catch((err: BusinessError) => {
  console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
});
```
