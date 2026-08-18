# mkdirSync

## 导入模块

```TypeScript
```

## mkdirSync

```TypeScript
declare function mkdirSync(path: string): void
```

以同步方法创建目录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function mkdirSync(path: string): void--><!--Device-unnamed-declare function mkdirSync(path: string): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900018 |
| 13900028 |
| 13900030 |
| 13900025 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## mkdirSync

```TypeScript
declare function mkdirSync(path: string, recursion: boolean): void
```

以同步方法创建目录。当recursion指定为true，可递归创建目录。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function mkdirSync(path: string, recursion: boolean): void--><!--Device-unnamed-declare function mkdirSync(path: string, recursion: boolean): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| recursion | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900018 |
| 13900028 |
| 13900030 |
| 13900025 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
