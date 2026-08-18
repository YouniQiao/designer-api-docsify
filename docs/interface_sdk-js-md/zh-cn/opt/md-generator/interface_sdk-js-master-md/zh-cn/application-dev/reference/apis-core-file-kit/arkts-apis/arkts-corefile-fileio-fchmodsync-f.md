# fchmodSync

## 导入模块

```TypeScript
```

## fchmodSync

```TypeScript
declare function fchmodSync(fd: number, mode: number): void
```

以同步方法基于文件描述符改变文件权限。

**起始版本：** 7

**废弃版本：** 9

<!--Device-unnamed-declare function fchmodSync(fd: number, mode: number): void--><!--Device-unnamed-declare function fchmodSync(fd: number, mode: number): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | number | 是 |
