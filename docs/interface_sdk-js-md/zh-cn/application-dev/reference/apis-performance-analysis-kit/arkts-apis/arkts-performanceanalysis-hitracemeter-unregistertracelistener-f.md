# unregisterTraceListener

## 导入模块

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## unregisterTraceListener

```TypeScript
function unregisterTraceListener(index: number): number
```

注销通过registerTraceListener()注册的trace捕获开关通知回调函数。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |
