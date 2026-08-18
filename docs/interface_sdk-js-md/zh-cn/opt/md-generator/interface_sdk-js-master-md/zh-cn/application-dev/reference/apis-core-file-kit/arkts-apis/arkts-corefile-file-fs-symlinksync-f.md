# symlinkSync

## 导入模块

```TypeScript
```

## symlinkSync

```TypeScript
declare function symlinkSync(target: string, srcPath: string): void
```

以同步的方法基于文件路径创建符号链接。 > **说明：** > > 从API version 11开始，不支持三方应用使用。

**起始版本：** 9

<!--Device-unnamed-declare function symlinkSync(target: string, srcPath: string): void--><!--Device-unnamed-declare function symlinkSync(target: string, srcPath: string): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | string | 是 |
| srcPath | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
