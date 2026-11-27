# @ohos.fileio(文件管理)

该模块提供文件存储管理能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

> **使用说明：**

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取沙箱路径的方式及其接口用法可参考：[应用上下文Context-获取应用文件路径](../../../application-models/application-context-stage.md#获取应用文件路径)。

## 导入模块

```TypeScript
import fileIO from '@ohos.fileio';
```

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [fileIO](arkts-corefile-fileio-depr-fileio-n.md) | 该模块提供文件存储管理能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。 |

### 函数

| 名称 | 说明 |
| --- | --- |
| [access](arkts-corefile-fileio-depr--f.md#access-1) | 检查当前进程是否可访问某文件，使用Promise异步回调。 |
| [access](arkts-corefile-fileio-depr--f.md#access-2) | 检查当前进程是否可访问某文件，使用callback异步回调。 |
| [access](arkts-corefile-fileio-depr--f.md#access-3) | 检查当前进程是否可访问某文件，使用callback异步回调。 |
| [accessSync](arkts-corefile-fileio-depr--f.md#accesssync) | 以同步方法检查当前进程是否可访问某文件。 |
| [chmod](arkts-corefile-fileio-depr--f.md#chmod-1) | 改变文件权限，使用Promise异步回调。 |
| [chmod](arkts-corefile-fileio-depr--f.md#chmod-2) | 改变文件权限，使用callback异步回调。 |
| [chmodSync](arkts-corefile-fileio-depr--f.md#chmodsync) | 以同步方法改变文件权限。 |
| [chown](arkts-corefile-fileio-depr--f.md#chown-1) | 基于文件路径改变文件所有者，使用Promise异步回调。 |
| [chown](arkts-corefile-fileio-depr--f.md#chown-2) | 基于文件路径改变文件所有者，使用callback异步回调。 |
| [chownSync](arkts-corefile-fileio-depr--f.md#chownsync) | 以同步的方法基于文件路径改变文件所有者。 |
| [close](arkts-corefile-fileio-depr--f.md#close-1) | 关闭文件，使用Promise异步回调。 |
| [close](arkts-corefile-fileio-depr--f.md#close-2) | 关闭文件，使用callback异步回调。 |
| [closeSync](arkts-corefile-fileio-depr--f.md#closesync-1) | 以同步方法关闭文件。 |
| [copyFile](arkts-corefile-fileio-depr--f.md#copyfile-1) | 复制文件，使用Promise异步回调。 |
| [copyFile](arkts-corefile-fileio-depr--f.md#copyfile-2) | copyFile. |
| [copyFile](arkts-corefile-fileio-depr--f.md#copyfile-3) | 复制文件，使用callback异步回调。 |
| [copyFileSync](arkts-corefile-fileio-depr--f.md#copyfilesync) | 以同步方法复制文件。 |
| [createStream](arkts-corefile-fileio-depr--f.md#createstream-1) | 基于文件路径打开文件流，使用Promise异步回调。 |
| [createStream](arkts-corefile-fileio-depr--f.md#createstream-2) | 基于文件路径打开文件流，使用callback异步回调。 |
| [createStreamSync](arkts-corefile-fileio-depr--f.md#createstreamsync) | 以同步方法基于文件路径打开文件流。 |
| [createWatcher](arkts-corefile-fileio-depr--f.md#createwatcher) | 监听文件或者目录的变化，使用callback异步回调。 |
| [fchmod](arkts-corefile-fileio-depr--f.md#fchmod-1) | 基于文件描述符改变文件权限，使用Promise异步回调。 |
| [fchmod](arkts-corefile-fileio-depr--f.md#fchmod-2) | 基于文件描述符改变文件权限，使用callback异步回调。 |
| [fchmodSync](arkts-corefile-fileio-depr--f.md#fchmodsync) | 以同步方法基于文件描述符改变文件权限。 |
| [fchown](arkts-corefile-fileio-depr--f.md#fchown-1) | 基于文件描述符改变文件所有者，使用Promise异步回调。 |
| [fchown](arkts-corefile-fileio-depr--f.md#fchown-2) | 基于文件描述符改变文件所有者，使用callback异步回调。 |
| [fchownSync](arkts-corefile-fileio-depr--f.md#fchownsync) | 以同步方法基于文件描述符改变文件所有者。 |
| [fdatasync](arkts-corefile-fileio-depr--f.md#fdatasync-1) | 实现文件内容数据同步，使用Promise异步回调。 |
| [fdatasync](arkts-corefile-fileio-depr--f.md#fdatasync-2) | 实现文件内容数据同步，使用callback异步回调。 |
| [fdatasyncSync](arkts-corefile-fileio-depr--f.md#fdatasyncsync) | 以同步方法实现文件内容数据同步。 |
| [fdopenStream](arkts-corefile-fileio-depr--f.md#fdopenstream-1) | 基于文件描述符打开文件流，使用Promise异步回调。 |
| [fdopenStream](arkts-corefile-fileio-depr--f.md#fdopenstream-2) | 基于文件描述符打开文件流，使用callback异步回调。 |
| [fdopenStreamSync](arkts-corefile-fileio-depr--f.md#fdopenstreamsync) | 以同步方法基于文件描述符打开文件流。 |
| [fstat](arkts-corefile-fileio-depr--f.md#fstat-1) | 基于文件描述符获取文件状态信息，使用Promise异步回调。 |
| [fstat](arkts-corefile-fileio-depr--f.md#fstat-2) | 基于文件描述符获取文件状态信息，使用callback异步回调。 |
| [fstatSync](arkts-corefile-fileio-depr--f.md#fstatsync) | 以同步方法基于文件描述符获取文件状态信息。 |
| [fsync](arkts-corefile-fileio-depr--f.md#fsync-1) | 同步文件数据，使用Promise异步回调。 |
| [fsync](arkts-corefile-fileio-depr--f.md#fsync-2) | 同步文件数据，使用callback异步回调。 |
| [fsyncSync](arkts-corefile-fileio-depr--f.md#fsyncsync) | 以同步方法同步文件数据。 |
| [ftruncate](arkts-corefile-fileio-depr--f.md#ftruncate-1) | 基于文件描述符截断文件，使用Promise异步回调。 |
| [ftruncate](arkts-corefile-fileio-depr--f.md#ftruncate-2) | 基于文件描述符截断文件，使用callback异步回调。 |
| [ftruncate](arkts-corefile-fileio-depr--f.md#ftruncate-3) | 基于文件描述符截断文件，使用callback异步回调。 |
| [ftruncateSync](arkts-corefile-fileio-depr--f.md#ftruncatesync) | 以同步方法基于文件描述符截断文件。 |
| [hash](arkts-corefile-fileio-depr--f.md#hash-1) | 计算文件的哈希值，使用Promise异步回调。 |
| [hash](arkts-corefile-fileio-depr--f.md#hash-2) | 计算文件的哈希值，使用callback异步回调。 |
| [lchown](arkts-corefile-fileio-depr--f.md#lchown-1) | 基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是符号链接所指向的实际文件，使用Promise异步回调。 |
| [lchown](arkts-corefile-fileio-depr--f.md#lchown-2) | 基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件，使用callback异步回调。 |
| [lchownSync](arkts-corefile-fileio-depr--f.md#lchownsync) | 以同步方法基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件。 |
| [lstat](arkts-corefile-fileio-depr--f.md#lstat-1) | 获取链接信息，使用Promise异步回调。 |
| [lstat](arkts-corefile-fileio-depr--f.md#lstat-2) | 获取链接信息，使用callback异步回调。 |
| [lstatSync](arkts-corefile-fileio-depr--f.md#lstatsync) | 以同步方法获取链接信息。 |
| [mkdir](arkts-corefile-fileio-depr--f.md#mkdir-1) | 创建目录，使用Promise异步回调。 |
| [mkdir](arkts-corefile-fileio-depr--f.md#mkdir-2) | 创建目录，使用callback异步回调。 |
| [mkdir](arkts-corefile-fileio-depr--f.md#mkdir-3) | 创建目录，使用callback异步回调。 |
| [mkdirSync](arkts-corefile-fileio-depr--f.md#mkdirsync) | 以同步方法创建目录。 |
| [mkdtemp](arkts-corefile-fileio-depr--f.md#mkdtemp-1) | 创建临时目录，使用Promise异步回调。 |
| [mkdtemp](arkts-corefile-fileio-depr--f.md#mkdtemp-2) | 创建临时目录，使用callback异步回调。 |
| [mkdtempSync](arkts-corefile-fileio-depr--f.md#mkdtempsync) | 以同步的方法创建临时目录。 |
| [open](arkts-corefile-fileio-depr--f.md#open-1) | 打开文件，使用Promise异步回调。 |
| [open](arkts-corefile-fileio-depr--f.md#open-2) | 打开文件，使用callback异步回调。 |
| [open](arkts-corefile-fileio-depr--f.md#open-3) | 打开文件，使用callback异步回调。 |
| [open](arkts-corefile-fileio-depr--f.md#open-4) | 打开文件，使用callback异步回调。 |
| [opendir](arkts-corefile-fileio-depr--f.md#opendir-1) | 打开文件目录，使用Promise异步回调。 |
| [opendir](arkts-corefile-fileio-depr--f.md#opendir-2) | 打开文件目录，使用callback异步回调。 |
| [opendirSync](arkts-corefile-fileio-depr--f.md#opendirsync) | 以同步方法打开文件目录。 |
| [openSync](arkts-corefile-fileio-depr--f.md#opensync) | 以同步方法打开文件。 |
| [read](arkts-corefile-fileio-depr--f.md#read-1) | 从文件读取数据，使用Promise异步回调。 |
| [read](arkts-corefile-fileio-depr--f.md#read-2) | 从文件读取数据，使用callback异步回调。 |
| [read](arkts-corefile-fileio-depr--f.md#read-3) | 从文件读取数据，使用callback异步回调。 |
| [readSync](arkts-corefile-fileio-depr--f.md#readsync-1) | 以同步方法从文件读取数据。 |
| [readText](arkts-corefile-fileio-depr--f.md#readtext-1) | 基于文本方式读取文件（即直接读取文件的文本内容），使用Promise异步回调。 |
| [readText](arkts-corefile-fileio-depr--f.md#readtext-2) | 基于文本方式读取文件（即直接读取文件的文本内容），使用callback异步回调。 |
| [readTextSync](arkts-corefile-fileio-depr--f.md#readtextsync) | 以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。 |
| [rename](arkts-corefile-fileio-depr--f.md#rename-1) | 重命名文件，使用Promise异步回调。 |
| [rename](arkts-corefile-fileio-depr--f.md#rename-2) | 重命名文件，使用callback异步回调。 |
| [renameSync](arkts-corefile-fileio-depr--f.md#renamesync) | 以同步方法重命名文件。 |
| [rmdir](arkts-corefile-fileio-depr--f.md#rmdir-1) | 删除目录，使用Promise异步回调。 |
| [rmdir](arkts-corefile-fileio-depr--f.md#rmdir-2) | 删除目录，使用callback异步回调。 |
| [rmdirSync](arkts-corefile-fileio-depr--f.md#rmdirsync) | 以同步方法删除目录。 |
| [stat](arkts-corefile-fileio-depr--f.md#stat-1) | 获取文件信息，使用Promise异步回调。 |
| [stat](arkts-corefile-fileio-depr--f.md#stat-2) | 获取文件信息，使用callback异步回调。 |
| [statSync](arkts-corefile-fileio-depr--f.md#statsync) | 以同步方法获取文件的信息。 |
| [symlink](arkts-corefile-fileio-depr--f.md#symlink-1) | 基于文件路径创建符号链接，使用Promise异步回调。 |
| [symlink](arkts-corefile-fileio-depr--f.md#symlink-2) | 基于文件路径创建符号链接，使用callback异步回调。 |
| [symlinkSync](arkts-corefile-fileio-depr--f.md#symlinksync) | 以同步的方法基于文件路径创建符号链接。 |
| [truncate](arkts-corefile-fileio-depr--f.md#truncate-1) | 基于文件路径截断文件，使用Promise异步回调。 |
| [truncate](arkts-corefile-fileio-depr--f.md#truncate-2) | 基于文件路径截断文件，使用callback异步回调。 |
| [truncate](arkts-corefile-fileio-depr--f.md#truncate-3) | 基于文件路径截断文件，使用callback异步回调。 |
| [truncateSync](arkts-corefile-fileio-depr--f.md#truncatesync) | 以同步方法基于文件路径截断文件。 |
| [unlink](arkts-corefile-fileio-depr--f.md#unlink-1) | 删除文件，使用Promise异步回调。 |
| [unlink](arkts-corefile-fileio-depr--f.md#unlink-2) | 删除文件，使用callback异步回调。 |
| [unlinkSync](arkts-corefile-fileio-depr--f.md#unlinksync) | 以同步方法删除文件。 |
| [write](arkts-corefile-fileio-depr--f.md#write-1) | 将数据写入文件，使用Promise异步回调。 |
| [write](arkts-corefile-fileio-depr--f.md#write-2) | 将数据写入文件，使用callback异步回调。 |
| [write](arkts-corefile-fileio-depr--f.md#write-3) | 将数据写入文件，使用callback异步回调。 |
| [writeSync](arkts-corefile-fileio-depr--f.md#writesync-1) | 以同步方法将数据写入文件。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [Dir](arkts-corefile-fileio-depr-dir-i.md) | 管理目录，在调用Dir的方法前，需要先通过opendir方法（同步或异步）来构建一个Dir实例。 |
| [Dirent](arkts-corefile-fileio-depr-dirent-i.md) | 在调用Dirent的方法前，需要先通过[dir.read()](arkts-corefile-fileio-depr--f.md#read)方法（同步或异步）来构建一个Dirent实例。 |
| [ReadOut](arkts-corefile-fileio-depr-readout-i.md) | 仅用于read方法，获取文件的读取结果。 |
| [Stat](arkts-corefile-fileio-depr-stat-i.md) | 文件具体信息，在调用Stat的方法前，需要先通过[stat()](arkts-corefile-fileio-depr--f.md#stat)方法（同步或异步）来构建一个Stat实例。 |
| [Stream](arkts-corefile-fileio-depr-stream-i.md) | 文件流，在调用Stream的方法前，需要先通过createStream()方法（同步或异步）来构建一个Stream实例。 |
| [Watcher](arkts-corefile-fileio-depr-watcher-i.md) | Watcher是文件变化监听的实例，调用Watcher.stop()方法（同步或异步）来停止文件监听。 |
