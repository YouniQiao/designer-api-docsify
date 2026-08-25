# OnProcess（系统接口）

```TypeScript
type OnProcess = (bundleName: string, process: string) => void
```

返回应用备份数据量信息的回调函数。 备份服务返回结果或进度信息时触发的回调。 返回应用的处理结果或进度信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| process | string | 是 |
