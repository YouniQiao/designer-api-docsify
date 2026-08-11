# @ohos.fastbuffer

FastBuffer对象是比Buffer性能更优的Buffer容器，用于表示固定长度的字节序列，是专门存放二进制数据的缓冲区。

FastBuffer通过from构造时，仅支持FastBuffer、Uint8Array、string、Array、ArrayBuffer和SharedArrayBuffer类型的参数。

需要高效处理二进制数据（如图片、文件传输、网络通信等）时，推荐使用FastBuffer以获得更好的性能。

**起始版本：** 20

<!--Device-unnamed-declare namespace fastbuffer--><!--Device-unnamed-declare namespace fastbuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 函数

| 名称 |
| --- |
| [alloc](arkts-arkts-fastbuffer-alloc-f.md#alloc) |
| [allocUninitialized](arkts-arkts-fastbuffer-allocuninitialized-f.md#allocuninitialized) |
| [allocUninitializedFromPool](arkts-arkts-fastbuffer-allocuninitializedfrompool-f.md#allocuninitializedfrompool) |
| [byteLength](arkts-arkts-fastbuffer-bytelength-f.md#bytelength) |
| [compare](arkts-arkts-fastbuffer-compare-f.md#compare) |
| [concat](arkts-arkts-fastbuffer-concat-f.md#concat) |
| [from](arkts-arkts-fastbuffer-from-f.md#from) |
| [from](arkts-arkts-fastbuffer-from-f.md#from-1) |
| [from](arkts-arkts-fastbuffer-from-f.md#from-2) |
| [from](arkts-arkts-fastbuffer-from-f.md#from-3) |
| [isBuffer](arkts-arkts-fastbuffer-isbuffer-f.md#isbuffer) |
| [isEncoding](arkts-arkts-fastbuffer-isencoding-f.md#isencoding) |
| [transcode](arkts-arkts-fastbuffer-transcode-f.md#transcode) |

### 类

| 名称 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

### 接口

| 名称 |
| --- |
| [TypedArray](arkts-arkts-fastbuffer-typedarray-i.md) |

### 类型

| 名称 |
| --- |
| [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) |
