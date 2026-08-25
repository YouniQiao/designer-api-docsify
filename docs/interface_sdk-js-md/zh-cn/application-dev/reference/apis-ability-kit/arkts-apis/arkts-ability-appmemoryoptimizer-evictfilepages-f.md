# evictFilePages

## 导入模块

```TypeScript
import { appMemoryOptimizer } from 'kits/@kit.AbilityKit';
```

## evictFilePages

```TypeScript
function evictFilePages(fileNames: Array<string>): Promise<void>
```

向系统发出释放指定文件的文件页缓存请求，系统会根据当前内存状况决定是否真正执行释放，不保证一定释放成功。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileNames | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000163](../errorcode-ability.md#16000163-文件类型错误) |
