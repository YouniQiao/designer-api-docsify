# SourceCloseCallback

```TypeScript
type SourceCloseCallback = (uuid: long) => void
```

由应用实现此回调函数，应用应释放相关资源。

> **注意：**&gt;
> 客户端在处理完请求后应立刻返回。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |

**示例**

```TypeScript
import { HashMap } from '@kit.ArkTS';

let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();

let sourceCloseCallback: media.SourceCloseCallback = (uuid: number) => {
  console.info(`Closing resource with handle ${uuid}`);
  // 清除当前uuid相关资源。
  requests.remove(uuid);
};
```
