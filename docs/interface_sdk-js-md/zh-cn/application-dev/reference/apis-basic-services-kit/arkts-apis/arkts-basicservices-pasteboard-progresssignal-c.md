# ProgressSignal

定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md)设置为NONE时此参数才生效。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## cancel

```TypeScript
cancel(): void
```

取消正在进行的拷贝粘贴任务。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard
