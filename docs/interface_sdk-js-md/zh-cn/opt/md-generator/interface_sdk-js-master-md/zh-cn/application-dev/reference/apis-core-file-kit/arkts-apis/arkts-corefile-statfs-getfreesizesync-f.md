# getFreeSizeSync

## getFreeSizeSync

```TypeScript
function getFreeSizeSync(path: string): number
```

以同步方法获取指定文件系统空闲字节数。

**起始版本：** 10

<!--Device-statfs-function getFreeSizeSync(path: string): long--><!--Device-statfs-function getFreeSizeSync(path: string): long-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
let freeSize = statfs.getFreeSizeSync(path);
console.info("Succeeded in getting free size: " + freeSize);
```
