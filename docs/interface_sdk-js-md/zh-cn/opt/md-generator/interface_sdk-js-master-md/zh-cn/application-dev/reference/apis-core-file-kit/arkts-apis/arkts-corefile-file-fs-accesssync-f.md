# accessSync

## accessSync

```TypeScript
declare function accessSync(path: string, mode?: AccessModeType): boolean
```

以同步方法检查文件或目录是否存在，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function accessSync(path: string, mode?: AccessModeType): boolean--><!--Device-unnamed-declare function accessSync(path: string, mode?: AccessModeType): boolean-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900005 |
| 13900023 |
| 13900033 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900008 |
| 13900042 |
| 13900011 |


## accessSync

```TypeScript
declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean
```

以同步方法检查文件或目录是否在本地，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**起始版本：** 12

<!--Device-unnamed-declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean--><!--Device-unnamed-declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | 是 |
| flag | [AccessFlagType](arkts-corefile-file-fs-accessflagtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| 13900005 |
| 13900023 |
| 13900033 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900011 |
