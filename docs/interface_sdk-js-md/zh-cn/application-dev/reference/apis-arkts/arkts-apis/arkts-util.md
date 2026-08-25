# @ohos.util

该模块主要提供常用的工具函数，实现字符串编解码（[TextEncoder](arkts-arkts-util-textencoder-c.md)，[TextDecoder](arkts-arkts-util-textdecoder-c.md)）、 有理数运算（[RationalNumber&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkts-util-rationalnumber-c.md)）、缓冲区管理（[LRUCache&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkts-util-lrucache-c.md)）、 范围判断（[ScopeHelper&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkts-util-scopehelper-c.md)）、 Base64编解码（[Base64Helper&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkts-util-base64helper-c.md)）、 内置对象类型检查（[types&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkts-util-types-c.md)）、对方法进行插桩和替换（[Aspect&lt;sup&gt;11+&lt;/sup&gt;](arkts-arkts-util-aspect-c.md)）、 虚拟机维测能力（[ArkTSVM&lt;sup&gt;23+&lt;/sup&gt;](arkts-arkts-util-arktsvm-c.md)）、二进制流解码（[StringDecoder&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkts-util-stringdecoder-c.md)）、 堆内存阈值配置（[HeapMemoryThreshold&lt;sup&gt;24+&lt;/sup&gt;](arkts-arkts-util-heapmemorythreshold-i.md)）等功能。 此外还提供获取对象Hash值（[util.getHash&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkts-util-gethash-f.md)）、 获取主线程栈追踪信息（[util.getMainThreadStackTrace&lt;sup&gt;20+&lt;/sup&gt;](arkts-arkts-util-getmainthreadstacktrace-f.md)）等工具函数。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from '@kit.ArkTS';
```

## 汇总

### 函数

| 名称 |
| --- |
| [callbackWrapper](arkts-arkts-util-callbackwrapper-f.md) |
| [errnoToString](arkts-arkts-util-errnotostring-f.md) |
| [format](arkts-arkts-util-format-f.md) |
| [generateRandomBinaryUUID](arkts-arkts-util-generaterandombinaryuuid-f.md) |
| [generateRandomUUID](arkts-arkts-util-generaterandomuuid-f.md) |
| [getErrorString](arkts-arkts-util-geterrorstring-f.md) |
| [getHash](arkts-arkts-util-gethash-f.md) |
| [getMainThreadStackTrace](arkts-arkts-util-getmainthreadstacktrace-f.md) |
| [parseUUID](arkts-arkts-util-parseuuid-f.md) |
| [printf](arkts-arkts-util-printf-f.md) |
| [promiseWrapper](arkts-arkts-util-promisewrapper-f.md) |
| [promisify](arkts-arkts-util-promisify-f.md) |

### 类

| 名称 |
| --- |
| [ArkTSVM](arkts-arkts-util-arktsvm-c.md) |
| [Aspect](arkts-arkts-util-aspect-c.md) |
| [AutoFinalizerCleaner](arkts-arkts-util-autofinalizercleaner-c.md) |
| [Base64](arkts-arkts-util-base64-c.md) |
| [Base64Helper](arkts-arkts-util-base64helper-c.md) |
| [LruBuffer](arkts-arkts-util-lrubuffer-c.md) |
| [LRUCache](arkts-arkts-util-lrucache-c.md) |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |
| [Scope](arkts-arkts-util-scope-c.md) |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |
| [StringDecoder](arkts-arkts-util-stringdecoder-c.md) |
| [TextDecoder](arkts-arkts-util-textdecoder-c.md) |
| [TextEncoder](arkts-arkts-util-textencoder-c.md) |
| [types](arkts-arkts-util-types-c.md) |

### 接口

| 名称 |
| --- |
| [AutoFinalizer](arkts-arkts-util-autofinalizer-i.md) |
| [DecodeToStringOptions](arkts-arkts-util-decodetostringoptions-i.md) |
| [DecodeWithStreamOptions](arkts-arkts-util-decodewithstreamoptions-i.md) |
| [EncodeIntoUint8ArrayInfo](arkts-arkts-util-encodeintouint8arrayinfo-i.md) |
| [HeapMemoryInfo](arkts-arkts-util-heapmemoryinfo-i.md) |
| [HeapMemoryThreshold](arkts-arkts-util-heapmemorythreshold-i.md) |
| [MultithreadingDetectionOptions](arkts-arkts-util-multithreadingdetectionoptions-i.md) |
| [ScopeComparable](arkts-arkts-util-scopecomparable-i.md) |
| [TextDecoderOptions](arkts-arkts-util-textdecoderoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [Type](arkts-arkts-util-type-e.md) |

### 类型

| 名称 |
| --- |
| [PromisifiedFunc](arkts-arkts-util-promisifiedfunc-t.md) |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |
