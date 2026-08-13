# getLocalName

## getLocalName

```TypeScript
function getLocalName(): string
```

获取本地设备的名称。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-manager-function getLocalName(): string--><!--Device-manager-function getLocalName(): string-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
