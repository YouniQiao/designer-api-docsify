# createSystemSoundPlayer

## 导入模块

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## createSystemSoundPlayer

```TypeScript
function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>
```

创建系统音效播放器对象。使用Promise异步回调。

**起始版本：** 23

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;SystemSoundPlayer \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-内存分配失败) |
