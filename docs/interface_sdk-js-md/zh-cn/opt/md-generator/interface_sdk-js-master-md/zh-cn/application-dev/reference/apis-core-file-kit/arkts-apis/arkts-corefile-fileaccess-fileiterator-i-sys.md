# FileIterator（系统接口）

表示文件夹的迭代器对象。

**起始版本：** 9

**废弃版本：** 23

<!--Device-fileAccess-interface FileIterator--><!--Device-fileAccess-interface FileIterator-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## next

```TypeScript
next(): { value: FileInfo, done: boolean }
```

可以通过next同步方法获取下一级文件(夹)信息。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileIterator-next(): { value: FileInfo, done: boolean }--><!--Device-FileIterator-next(): { value: FileInfo, done: boolean }-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| { value: FileInfo, done: boolean } |

**错误码：**

| 错误码ID |
| --- |
| 14000004 |
| 13900038 |
| 14000001 |
| 13900033 |
| 13900034 |
| 14000003 |
| 14000002 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 13900013 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 14300004 |
| 13900011 |
