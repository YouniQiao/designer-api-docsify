# deleteGroup

## 导入模块

```TypeScript
```

## deleteGroup

```TypeScript
function deleteGroup(gid: string): Promise<void>
```

移除指定分组，后续不能再往该分组中添加任务id。使用Promise异步回调。 当分组中的所有任务处于完成、失败或移除状态，并且分组被移除时，显示该分组的完成或失败通知。

**起始版本：** 23

<!--Device-agent-function deleteGroup(gid: string): Promise<void>--><!--Device-agent-function deleteGroup(gid: string): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gid | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900008](../../apis-basic-services-kit/errorcode-request.md#21900008-任务分组不存在或已移除) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
