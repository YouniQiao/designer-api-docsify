# debug

## 导入模块

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## debug

```TypeScript
function debug(domain: number, tag: string, format: string, ...args: any[]): void
```

打印DEBUG级别的日志。DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domain | number | 是 |
| tag | string | 是 |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any[] | 是 |
