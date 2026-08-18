# destroyPort

## 导入模块

```TypeScript
```

## destroyPort

```TypeScript
function destroyPort(uuid: string): void
```

根据UUID销毁监听端口并释放相关资源。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataTransfer-function destroyPort(uuid: string): void--><!--Device-dataTransfer-function destroyPort(uuid: string): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [36100022](../errorcode-nearlink-service.md#36100022-端口未注册) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [36100044](../errorcode-nearlink-service.md#36100044-禁止使用星闪标准服务uuid) |
| [36100043](../errorcode-nearlink-service.md#36100043-无效uuid) |
