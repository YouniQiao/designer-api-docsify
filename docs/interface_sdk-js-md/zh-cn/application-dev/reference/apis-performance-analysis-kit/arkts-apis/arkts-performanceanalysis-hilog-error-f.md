# error

## 导入模块

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## error

```TypeScript
function error(domain: number, tag: string, format: string, ...args: any[]): void
```

打印ERROR级别的日志。

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
