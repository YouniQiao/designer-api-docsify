# @ohos.fastbuffer

FastBuffer对象是比Buffer性能更优的Buffer容器，用于表示固定长度的字节序列，是专门存放二进制数据的缓冲区。FastBuffer通过from构造时，仅支持FastBuffer、Uint8Array、string、Array、ArrayBuffer和SharedArrayBuffer类型的参数。需要高效处理二进制数据（如图片、文件传输、网络通信等）时，推荐使用FastBuffer以获得更好的性能。@namespace fastbuffer

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { fastbuffer } from '@kit.ArkTS';
```

## 汇总

### 函数

| 名称 |
| --- |
| [alloc](arkts-arkts-fastbuffer-alloc-f.md) |
| [allocUninitialized](arkts-arkts-fastbuffer-allocuninitialized-f.md) |
| [allocUninitializedFromPool](arkts-arkts-fastbuffer-allocuninitializedfrompool-f.md) |
| [byteLength](arkts-arkts-fastbuffer-bytelength-f.md) |
| [compare](arkts-arkts-fastbuffer-compare-f.md) |
| [concat](arkts-arkts-fastbuffer-concat-f.md) |
| [from](arkts-arkts-fastbuffer-from-f.md) |
| [from](arkts-arkts-fastbuffer-from-f.md) |
| [from](arkts-arkts-fastbuffer-from-f.md) |
| [from](arkts-arkts-fastbuffer-from-f.md) |
| [isBuffer](arkts-arkts-fastbuffer-isbuffer-f.md) |
| [isEncoding](arkts-arkts-fastbuffer-isencoding-f.md) |
| [transcode](arkts-arkts-fastbuffer-transcode-f.md) |

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
