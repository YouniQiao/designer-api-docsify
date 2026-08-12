# @ohos.util

该模块主要提供常用的工具函数，实现字符串编解码（[TextEncoder](arkts-arkts-util-textencoder-c.md#TextEncoder)，[TextDecoder](arkts-arkts-util-textdecoder-c.md#TextDecoder)）、有理数运算（[RationalNumber&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkts-util-rationalnumber-c.md#RationalNumber)）、缓冲区管理（[LRUCache&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkts-util-lrucache-c.md#LRUCache)）、范围判断（[ScopeHelper&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkts-util-scopehelper-c.md#ScopeHelper)）、Base64编解码（[Base64Helper&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkts-util-base64helper-c.md#Base64Helper)）、内置对象类型检查（[types&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkts-util-types-c.md#types)）、对方法进行插桩和替换（[Aspect&lt;sup&gt;11+&lt;/sup&gt;](arkts-arkts-util-aspect-c.md#Aspect)）、虚拟机维测能力（[ArkTSVM&lt;sup&gt;23+&lt;/sup&gt;](arkts-arkts-util-arktsvm-c.md#ArkTSVM)）、二进制流解码（[StringDecoder&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkts-util-stringdecoder-c.md#StringDecoder)）、堆内存阈值配置（[HeapMemoryThreshold&lt;sup&gt;24+&lt;/sup&gt;](arkts-arkts-util-heapmemorythreshold-i.md#HeapMemoryThreshold)）等功能。此外还提供获取对象Hash值（[util.getHash&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkts-util-gethash-f.md#getHash)）、获取主线程栈追踪信息（[util.getMainThreadStackTrace&lt;sup&gt;20+&lt;/sup&gt;](arkts-arkts-util-getmainthreadstacktrace-f.md#getMainThreadStackTrace)）等工具函数。

**起始版本：** 7

<!--Device-unnamed-declare namespace util--><!--Device-unnamed-declare namespace util-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 函数

| 名称 |
| --- |
| [callbackWrapper](arkts-arkts-util-callbackwrapper-f.md#callbackwrapper) |
| [errnoToString](arkts-arkts-util-errnotostring-f.md#errnotostring) |
| [format](arkts-arkts-util-format-f.md#format) |
| [generateRandomBinaryUUID](arkts-arkts-util-generaterandombinaryuuid-f.md#generaterandombinaryuuid) |
| [generateRandomUUID](arkts-arkts-util-generaterandomuuid-f.md#generaterandomuuid) |
| [getErrorString](arkts-arkts-util-geterrorstring-f.md#geterrorstring) |
| [getHash](arkts-arkts-util-gethash-f.md#gethash) |
| [getMainThreadStackTrace](arkts-arkts-util-getmainthreadstacktrace-f.md#getmainthreadstacktrace) |
| [parseUUID](arkts-arkts-util-parseuuid-f.md#parseuuid) |
| [printf](arkts-arkts-util-printf-f.md#printf) |
| [promiseWrapper](arkts-arkts-util-promisewrapper-f.md#promisewrapper) |
| [promisify](arkts-arkts-util-promisify-f.md#promisify) |

### 类

| 名称 |
| --- |
| [ArkTSVM](arkts-arkts-util-arktsvm-c.md) |
| [Aspect](arkts-arkts-util-aspect-c.md) |
| [AutoFinalizerCleaner](arkts-arkts-util-autofinalizercleaner-c.md) |
| [Base64](arkts-arkts-util-base64-c.md) |
| [Base64Helper](arkts-arkts-util-base64helper-c.md) |
| [LRUCache](arkts-arkts-util-lrucache-c.md) |
| [LruBuffer](arkts-arkts-util-lrubuffer-c.md) |
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
| [ScopeType](arkts-arkts-util-scopetype-t.md) |
