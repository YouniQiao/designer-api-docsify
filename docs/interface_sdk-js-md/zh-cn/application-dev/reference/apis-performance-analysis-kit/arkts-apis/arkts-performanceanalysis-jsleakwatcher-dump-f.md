# dump

## 导入模块

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## dump

```TypeScript
function dump(filePath: string): Array<string>
```

导出泄漏列表和虚拟机内存快照。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |
