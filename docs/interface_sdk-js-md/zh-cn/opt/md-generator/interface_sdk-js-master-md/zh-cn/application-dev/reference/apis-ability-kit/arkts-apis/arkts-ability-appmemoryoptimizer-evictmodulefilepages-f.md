# evictModuleFilePages

## evictModuleFilePages

```TypeScript
function evictModuleFilePages(moduleNames: Array<string>): Promise<void>
```

向系统发出释放指定模块的文件页缓存请求，系统会根据当前内存状况决定是否真正执行释放，不保证一定释放成功。系统会读取对应模块中的memory_optimizer.json配置文件，获取evictFilePages数组，然后对数组中的文件执行文件页缓存释放操作。

配置文件路径：{模块目录}/src/main/resources/rawfile/memory_optimizer.json配置文件中evictFilePages数组里的文件名必须以 .so、.hap 或 .hsp 结尾。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-appMemoryOptimizer-function evictModuleFilePages(moduleNames: Array<string>): Promise<void>--><!--Device-appMemoryOptimizer-function evictModuleFilePages(moduleNames: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleNames | Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000164](../errorcode-ability.md#16000164-解析配置文件失败) |
| [16000163](../errorcode-ability.md#16000163-文件类型错误) |
