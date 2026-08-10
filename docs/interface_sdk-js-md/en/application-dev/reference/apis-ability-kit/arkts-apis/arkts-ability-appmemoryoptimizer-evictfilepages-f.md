# evictFilePages

## Modules to Import

```TypeScript
import { appMemoryOptimizer } from 'kits/@kit.AbilityKit';
```

## evictFilePages

```TypeScript
function evictFilePages(fileNames: Array<string>): Promise<void>
```

向系统发出释放指定文件的文件页缓存请求，系统会根据当前内存状况决定是否真正执行释放，不保证一定释放成功。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-appMemoryOptimizer-function evictFilePages(fileNames: Array<string>): Promise<void>--><!--Device-appMemoryOptimizer-function evictFilePages(fileNames: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fileNames | Array&lt;string&gt; | Yes | 需要释放文件页缓存的文件名数组，文件名必须以.so、.hap 或.hsp结尾。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000163 | 文件类型错误。文件名未以.so、.hap或.hsp结尾。 |

