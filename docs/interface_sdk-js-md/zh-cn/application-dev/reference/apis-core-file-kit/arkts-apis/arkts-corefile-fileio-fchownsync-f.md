# fchownSync

## 导入模块

```TypeScript
```

## fchownSync

```TypeScript
declare function fchownSync(fd: number, uid: number, gid: number): void
```

以同步方法基于文件描述符改变文件所有者。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| uid | number | 是 |
| gid | number | 是 |
