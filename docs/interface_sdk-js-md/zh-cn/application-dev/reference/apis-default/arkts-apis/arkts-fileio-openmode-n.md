# OpenMode

open接口flags参数常量，用于指定文件打开模式（如只读、只写、读写、创建等）。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-fileIo-namespace OpenMode--><!--Device-fileIo-namespace OpenMode-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## 汇总

### 常量

| 名称 | 说明 |
| --- | --- |
| [READ_ONLY](arkts-openmode-con.md#read_only) | 只读打开。值为 0o0。 |
| [WRITE_ONLY](arkts-openmode-con.md#write_only) | 只写打开。值为 0o1。 |
| [READ_WRITE](arkts-openmode-con.md#read_write) | 读写打开。值为 0o2。 |
| [CREATE](arkts-openmode-con.md#create) | 若文件不存在，则创建文件。值为 0o100。 |
| [TRUNC](arkts-openmode-con.md#trunc) | 如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。值为 0o1000 |
| [APPEND](arkts-openmode-con.md#append) | 以追加方式打开，后续写将追加到文件末尾。值为 0o2000。 |
| [NONBLOCK](arkts-openmode-con.md#nonblock) | 如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。值为 0o4000。 |
| [DIR](arkts-openmode-con.md#dir) | 如果path不指向目录，则出错。值为 0o200000。 |
| [NOFOLLOW](arkts-openmode-con.md#nofollow) | 如果path指向符号链接，则出错。值为 0o400000。 |
| [SYNC](arkts-openmode-con.md#sync) | 以同步IO的方式打开文件。值为 0o4010000。 |
| [UNCACHE](arkts-openmode-con.md#uncache) | 读写文件不进行页缓存。值为 0o10000000000。 |

